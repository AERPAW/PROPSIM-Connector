"""
PROPSim Configuration Generator

Generates .smu configuration files for PROPSim simulations given the IDs of N radio nodes.
Each RF-Chain of a USRP is considered a radio, e.g. FN1_B210-RFA or FN1_B210-RFB
"""

import json
from typing import List, Dict, Optional


def generate_propsim_config(
    radio_names: List[str],
    connector_config_file: Optional[str] = None
) -> str:
    """Generate a PROPSim simulation configuration file."""

    connector_config: Dict = {}
    if connector_config_file:
        with open(connector_config_file, "r") as f:
            connector_config = json.load(f)

    n_radios = len(radio_names)
    n_channels = n_radios * (n_radios - 1)

    config: List[str] = []

    config.append("; PROPSim Simulation File, version 3.0")
    config.append("")

    config.extend(_generate_simulation_section())
    config.extend(_generate_multi_group_section())
    config.extend(_generate_channel_group_section(n_channels))
    config.extend(_generate_subgroup_section())
    config.extend(_generate_channel_sections(radio_names))
    config.extend(_generate_input_sections(radio_names, connector_config))
    config.extend(_generate_output_sections(radio_names, connector_config))

    # Windows CRLF line endings
    config = "\r\n".join(config)
    print(config)
    return config


# ---------------------------------------------------------------------------
# SECTIONS
# ---------------------------------------------------------------------------

def _generate_simulation_section() -> List[str]:
    return [
        "[Simulation]",
        "Description = ",
        "Creator = SimulationEditor",
        "RealTimeSampleClock = 200000000 Hz",
        "ClosedRoute = true",
        "RFLOAutoSet = false",
        "FadingMargin = 10 dB",
        "SplitTime = 8",
        "CombinedBands = 1",
        "AllocationType = NORMAL",
        "SimulationUsageType = NORMAL",
        "DBBClockMode = ASYNC_CLOCK",
        "FixedInsertionDelay = 0",
        "InterpolationMode = Coeff Interpolation",
        "EmulatorType = Platform2",
        "",
    ]


def _generate_multi_group_section() -> List[str]:
    return [
        "[Multi Group 0]",
        "Channel groups = 0",
        "CombinedBands = 1",
        "SplitTime = 8",
        "",
    ]


def _generate_channel_group_section(n_channels: int) -> List[str]:
    channel_list = ", ".join(str(i) for i in range(n_channels))
    return [
        "[Channel Group 0]",
        "SubGroups = 10000",
        f"Channels = {channel_list}",
        "CenterFrequency = 2000000000 Hz",
        "Immutable = false",
        "Direction = UPLINK",
        "Group type = NOT DEFINED",
        "Group name = ",
        "",
    ]


def _generate_subgroup_section() -> List[str]:
    return [
        "[SubGroup 10000]",
        "LinkLevel = -72.9829 dBm",
        "ShadowingEnabled = true",
        "BypassState = false",
        "OutputFrequency = 2000000000 Hz",
        "InputFrequency = 2000000000 Hz",
        "SpeedFactor = 1",
        "InputConnectorDuplexMode = DUPLEX",
        "OutputConnectorDuplexMode = DUPLEX",
        "",
    ]


# ---------------------------------------------------------------------------
# CHANNELS
# ---------------------------------------------------------------------------

def _generate_channel_sections(radio_names: List[str]) -> List[str]:
    sections: List[str] = []
    n_radios = len(radio_names)
    channel_id = 0

    for i in range(n_radios):
        for j in range(n_radios):
            if i == j:
                continue
            CIR_FILE = "One tap constant_0.ir"
            CIR_CONTROL = f"One tap constant_0_{channel_id}_F.sim"
            direction = "UL"
            CIR_UPDATE_RATE = 2.668512762

            sections.extend([
                f"[Channel {channel_id}]",
                f"Input = {i}",
                f"Output = {j}",
                "CirUpdateRate = {CIR_UPDATE_RATE} Hz",
                "SubGroup = 10000",
                f"CirSourceFile = ..\\NCSU\\{CIR_FILE}",
                f"CirControlFile = {CIR_CONTROL}",
                "",
            ])

            channel_id += 1

    return sections


# ---------------------------------------------------------------------------
# INPUTS
# ---------------------------------------------------------------------------

def _generate_input_sections(
    radio_names: List[str],
    connector_config: Dict,
) -> List[str]:
    sections: List[str] = []

    for i, radio_name in enumerate(radio_names):
        input_name = f"{radio_name}-TX"

        input_key = f"{radio_name}_IN_OUT"
        if connector_config and input_key in connector_config:
            unit = connector_config[input_key].get("Unit", 2)
            connector = connector_config[input_key].get("Connector", f"COMMON {i + 1}")
        elif connector_config:
            raise Exception(f"Key not present in the connector config: {input_key}")
        else:
            unit = 2
            connector = f"COMMON {i + 1}"

        sections.extend([
            f"[Input {i}]",
            f"InputName = {input_name}",
            "AvgInputLevel = -15 dBm",
            "CrestFactor = 6 dB",
            "InLoss = 0 dB",
            "SpectralInversion = 0",
            "InputType = rf",
            "MeasurementMode = Continous",
            "MeasurementOffset = 0 dB",
            "BurstTrigLevelRelative = -30 dB",
            "BurstMeasurementLength = 200000",
            "Emulator = 0",
            f"Unit = {unit}",
            f"Connector = {connector}",
            f"InternalConnector = {connector}",
            "CombiningMode = 1",
            "SubGroups = 10000",
            "",
        ])

    return sections


# ---------------------------------------------------------------------------
# OUTPUTS
# ---------------------------------------------------------------------------

def _generate_output_sections(
    radio_names: List[str],
    connector_config: Dict,
) -> List[str]:
    sections: List[str] = []

    shadowing_source = r"..\Emulation21.wiz\profile_link_1_0_DL.shd"

    for i, radio_name in enumerate(radio_names):
        output_name = f"{radio_name}-RX"

        output_key = f"{radio_name}_OUT"
        if connector_config and output_key in connector_config:
            unit = connector_config[output_key].get("Unit", 2)
            connector = connector_config[output_key].get("Connector", f"OUTPUT {i + 1}")
        elif connector_config:
            raise Exception(f"Key not present in the connector config: {output_key}")
        else:
            unit = 2
            connector = f"OUTPUT {i + 1}"

        sections.extend([
            f"[Output {i}]",
            f"OutputName = {output_name}",
            "Gain = 0 dB",
            "ExternalGain = 0 dB",
            "OutputType = rf",
            "SpectralInversion = 0",
            "Emulator = 0",
            f"Unit = {unit}",
            f"Connector = {connector}",
            f"InternalConnector = {connector}",
            "CombiningMode = 1",
            f"ShadowingSourceFile = {shadowing_source}",
            "SubGroups = 10000",
            "",
        ])

    return sections


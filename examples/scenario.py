import sys, time
import json
import numpy as np
import math
import argparse
from pyproj import Proj, transform, Transformer

sys.path.append("../")

# from pchem import client as pchem_client
# from pchem.constants import *

TIME_STEP = 1 # seconds
SCENARIO_CONFIG = "./scenario_config.json"
EARTH_RADIUS = 6378000 # meters (at equator)
bPRINT_LEVEL = "DETAILED"
SPEED_OF_LIGHT = 3 * 10E8

def _print(message, level):
    pass

def haversine(angle_rad):
    _haversine = (math.sin(angle_rad*0.5))**2
    return _haversine

# def ecef_to_lla(ecef):
    X = ecef[0]
    Y = ecef[1]
    Z = ecef[2]

    # WGS84 parameters
    a = 6378137.0  # semi-major axis
    f_inv = 298.257223563  # inverse flattening
    f = 1.0 / f_inv
    e2 = 1 - (1 - f) * (1 - f)
    eps = 1e-9  # convergence criteria
    
    # Calculate distance from point to Earth's center
    rho = math.sqrt(X**2 + Y**2 + Z**2)

    # Calculate longitude
    lon = math.atan2(Y, X)

    # Iteratively calculate latitude and altitude
    lat0 = math.atan2(Z, math.sqrt(X**2 + Y**2))
    alt0 = 0
    converged = False
    while not converged:
        N = a / math.sqrt(1 - e2 * math.sin(lat0)**2)
        alt = rho / math.cos(lat0) - N
        lat = math.atan2(Z + e2 * N * math.sin(lat0), math.sqrt(X**2 + Y**2))
        if abs(lat - lat0) < eps and abs(alt - alt0) < eps:
            converged = True
        lat0 = lat
        alt0 = alt

    # Convert latitude and longitude to degrees
    lat = math.degrees(lat)
    lon = math.degrees(lon)

    return [lat, lon, alt]

def lla_to_ned(ecef):
    pass

def lla_to_ecef(lla):
    # Convert latitude and longitude to radians
    lat_rad = math.radians(lla[0])
    lon_rad = math.radians(lla[1])

    # WGS84 parameters
    a = 6378137.0  # semi-major axis
    f_inv = 298.257223563  # inverse flattening
    f = 1.0 / f_inv
    e2 = 1 - (1 - f) * (1 - f)

    # Radius of curvature in the prime vertical
    N = a / math.sqrt(1 - e2 * math.sin(lat_rad)**2)

    # Convert LLA to ECEF
    X = (N + lla[2]) * math.cos(lat_rad) * math.cos(lon_rad)
    Y = (N + lla[2]) * math.cos(lat_rad) * math.sin(lon_rad)
    Z = (N * (1 - e2) + lla[2]) * math.sin(lat_rad)
    return [X, Y, Z]

def calculate_distance_lla(position_1, position_2):
    position_1_ecef = lla_to_ecef(position_1)
    position_2_ecef = lla_to_ecef(position_2)
    distance = math.sqrt(abs(position_2_ecef[0] - position_1_ecef[0])**2.0 + abs(position_2_ecef[1] - position_1_ecef[1])**2.0 + abs(position_2_ecef[2] - position_1_ecef[2])**2.0)
    return distance

def calculate_distance_ecef(position_1_ecef, position_2_ecef):
    distance = math.sqrt(abs(position_2_ecef[0] - position_1_ecef[0])**2.0 + abs(position_2_ecef[1] - position_1_ecef[1])**2.0 + abs(position_2_ecef[2] - position_1_ecef[2])**2.0)
    return distance

def calculate_distance2(position_1, position_2):   
    # Use the Haversine formula to calculate spherical distance, on earth's surface. Then, account for the difference in altitude using Pythagoras Theorem
    lat1_rad = math.radians(position_1[0])
    lat2_rad = math.radians(position_2[0])
    delta_lat_rad = math.radians(position_2[0] - position_1[0])
    delta_lon_rad = math.radians(position_2[1] - position_2[1])
    hav_theta = haversine(delta_lat_rad) + math.cos(lat2_rad)*math.cos(lat1_rad)*haversine(delta_lon_rad)
    theta = 2*math.asin(math.sqrt(hav_theta))
    dist_on_earth = theta*EARTH_RADIUS

    # Account for difference in altitude using Pythagoras Theorem
    delta_alt = abs(position_2[2] - position_1[2])
    dist = math.sqrt(dist_on_earth**2  + delta_alt**2)
    return dist

def ecef_to_lla(ecef):
    # Define the ECEF and LLA projections
    ecef_to_lla_transformer = Transformer.from_crs({"proj":"geocent", "ellps":"WGS84", "datum":"WGS84"},
                                                 {"proj":"latlong", "ellps":"WGS84", "datum":"WGS84"})

    # Convert ECEF coordinates to LLA
    lon, lat, alt = ecef_to_lla_transformer.transform(ecef[0], ecef[1], ecef[2])
    return lat, lon, alt


def move_towards_waypoint(position_1, position_2, distance):
    ecef_x1, ecef_y1, ecef_z1 = lla_to_ecef(position_1)
    ecef_x2, ecef_y2, ecef_z2 = lla_to_ecef(position_2)
    norm_displacement_vec = [ecef_x2 - ecef_x1, ecef_y2 - ecef_y1, ecef_z2 - ecef_z1]
    mag_displacement_vec = math.sqrt(sum([component**2 for component in norm_displacement_vec]))
    norm_displacement_vec = [component/ mag_displacement_vec for component in norm_displacement_vec]
    new_position_ecef = [ecef_x1 + norm_displacement_vec[0]*distance, ecef_y1 + norm_displacement_vec[1]*distance, ecef_z1 + norm_displacement_vec[2]*distance]     
    new_position_lla = ecef_to_lla(new_position_ecef)
    return new_position_ecef, new_position_lla

def calculate_heading(position_1, position_2):
    pass

def init_scenario_state(scenario_state):
    for ue_name in scenario_state["ue"]:
        ue = scenario_state["ue"][ue_name]
        ue["current_position_lla"] = ue["waypoints"][0]["waypoint"]
        ue['current_position_ecef'] = lla_to_ecef(ue["current_position_lla"])
        # ue["current_heading"] = calculate_heading(ue["waypoints"][1], ue["waypoints"][0])
        ue["current_speed"] = ue["waypoints"][0]["speed"]
        ue["next_waypoint_index"] = 1
        ue["dist_to_next_waypoint"] = calculate_distance_lla(ue["waypoints"][0]["waypoint"], ue["waypoints"][1]["waypoint"])
        ue["bEnd"] = False

    num_ue = len(scenario_state["ue"])
    num_bs = len(scenario_state["bs"])
    scenario_state["channel_matrix"] = np.zeros((num_ue + num_bs, num_ue + num_bs))
    scenario_state["bEnd"] = False

    scenario_state["path_loss_matrix"] = {}
    for ue_name in scenario_state["ue"]:
        for bs_name in scenario_state["bs"]:
            scenario_state["path_loss_matrix"][ue_name] = {}
            scenario_state["path_loss_matrix"][bs_name] = {}

    for bs_name in scenario_state["bs"]:
        bs = scenario_state["bs"][bs_name]
        bs["position_ecef"] = lla_to_ecef(bs["position"])

        
# Validate a scenario config: atleast two waypoints per UE, each BS must have a position
def validate_config():
    return True, ""
    pass

def print_state():
    pass

def calculate_path_loss(bs_position_ecef, ue_position_ecef, center_frequency, path_loss_exponent):
    distance = calculate_distance_ecef(bs_position_ecef, ue_position_ecef)
    path_loss = (4 * math.pi * distance * center_frequency / SPEED_OF_LIGHT)**path_loss_exponent
    path_loss_dB = 10 * math.log10(path_loss)
    return path_loss_dB

# Update scenario state: positions of UEs and path loss
def update_scenario_state(t, scenario_state):
    for ue_name in scenario_state["ue"]:
        ue = scenario_state["ue"][ue_name]
        # Calculate distance to next waypoint
        next_waypoint = ue["waypoints"][ue["next_waypoint_index"]]["waypoint"]
        current_waypoint = ue["current_position_lla"]
        ue["dist_to_next_waypoint"]  = calculate_distance_lla(current_waypoint, next_waypoint)
        print("--------------------------------")
        print(ue_name)
        print(ue["dist_to_next_waypoint"])
        # print(ue["current_position_ecef"])
        print("-------------------------------")
        # Check if the next waypoint was reached in the previous time step
        if ue["dist_to_next_waypoint"] <= TIME_STEP*ue["current_speed"]:
            # move to next waypoint
            ue["current_position_lla"] = ue["waypoints"][ue["next_waypoint_index"]]["waypoint"]
            ue["current_position_ecef"] = lla_to_ecef(ue["current_position_lla"] )

            if len(ue["waypoints"]) > (ue["next_waypoint_index"] + 1):
                ue["next_waypoint_index"] +=1
            else:
                ue["bEnd"] = True
        else:
            # Else, calculate UE positions at given time instant
            ue["current_position_ecef"], ue["current_position_lla"] = move_towards_waypoint(current_waypoint, next_waypoint, ue["current_speed"]*TIME_STEP)
    

    print("Path Loss:")
    # Path loss    
    for ue_name in scenario_state["ue"]:
        for bs_name in scenario_state["bs"]:
            ue = scenario_state["ue"][ue_name]
            bs = scenario_state["bs"][bs_name]
            print(ue_name, bs_name)
            path_loss = calculate_path_loss(ue["current_position_ecef"], bs["position_ecef"], scenario_state["center_frequency"], scenario_state["path_loss_exponent"]) 
            print(path_loss)
            print("---------")
            # Uplink
            scenario_state["path_loss_matrix"][ue_name][bs_name] = path_loss
            # Downlink
            scenario_state["path_loss_matrix"][bs_name][ue_name] = path_loss  

    # Check for scenario end
    scenario_state["bEnd"] = True
    for ue_name in scenario_state["ue"]:
        if not scenario_state["ue"][ue_name]["bEnd"]:
            scenario_state["bEnd"] = False
            break

# Simulator
def run_simulator(options):
    # Read BS, UE config
    with open(SCENARIO_CONFIG) as f: 
        scenario_state = json.load(f)
        t = 0

        # Validate config file
        bValid, errors = validate_config()
        if not bValid:
            print("Error in scenario config:" + errors)
            return 
        
        init_scenario_state(scenario_state)

        # Start ticking
        while not scenario_state["bEnd"]:
            # Modify PCHEM state
            # if options.pchem:
            #     pass

            # Sleep 
            time.sleep(TIME_STEP)
            
            # Update simulator state for next time step
            update_scenario_state(t, scenario_state)
            
            # tick
            t += TIME_STEP 
    pass

if __name__ == "__main__":
    options = argparse.ArgumentParser("Path loss simulator")
    options.add_argument("--pchem", "-p", action=argparse.BooleanOptionalAction, default=False, help= "Start PROPSIM and modify its channel state from the simulator")
    run_simulator(options)
    print("not main")
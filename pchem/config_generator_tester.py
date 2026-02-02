from propsim_config_generator import generate_propsim_config
radio_names = ["LPN-1_B205-1", "FN-1_B210-1-RFA", "FN-2_B205-1"]
config = generate_propsim_config(radio_names, "port_mapping.json")

with open("output.smu", "w") as f:
    print(config)
    f.write(config)

def create_connection(obj_dict):
    # create a duplicate of the obj_dict so that the original isn't modified
    device = obj_dict.copy()
    # pop a platform as this is an invalid kwarg to NAPALM
    platform = device.pop("device_type")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn

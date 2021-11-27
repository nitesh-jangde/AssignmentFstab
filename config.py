import yaml

def format_configuration(device_name,raw_data):
    data_list = []
    if raw_data['type'] == 'nfs':
        device_name = device_name+":"+raw_data['export']
    data_list.append(device_name)
    data_list.append(raw_data['mount'])
    data_list.append(raw_data['type'])
    if 'options' in raw_data:
        data_list.append(",".join(raw_data['options']))
    config_val = ("\t".join(data_list))
    return config_val


def create_config_file(file_name,yaml_data):
    print("Creating new config file {}".format(file_name))
    newfile = open(file_name, 'w')
    print("Updating {} configuration file".format(file_name))
    for device_name in yaml_data[file_name]:
        config_val = format_configuration(device_name,yaml_data[file_name][device_name])
        print("Adding device {} entry to {}".format(device_name, file_name))
        newfile.write(config_val + "\n")
    newfile.close()
    return 0


if __name__ == "__main__":
    with open('fsfile.yaml') as yaml_dump:
        yaml_data = yaml.safe_load(yaml_dump)
    for file_name in yaml_data:
        create_config_file(file_name,yaml_data)

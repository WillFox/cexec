import os
import yaml
def get_resource_list():
    home=os.environ.get('HOME')
    config_folder=os.path.join(home,".cexec")
    config_file=os.path.join(config_folder,"resources.yaml")
    if not os.path.isdir(config_folder):
        os.mkdir(config_folder)
    if not os.path.isfile(config_file):
        f=open(config_file,'w')
        f.close()
    with open(config_file,'r') as f:
        resources=yaml.load(f)
    return(resources)

def print_resource_list():
    resource_dict=get_resource_list()
    print("\n-----------------------------------------------------")
    print("{0:10}|{1:5}|{2:15}|{3:20}".format(
        "name",
        "type",
        "uname",
        "hostname"))
    print("----------|-----|---------------|--------------------")
    for i in list(resource_dict):
        sub_dict=resource_dict.get(i)
        print("{0:10}|{1:5}|{2:15}|{3:20}".format(
            i,
            sub_dict.get('type'),
            sub_dict.get('uname'),
            sub_dict.get('hostname')))
    print("-----------------------------------------------------\n")
    


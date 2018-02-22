import os
import yaml
import settings
import sys
import logging
import subprocess
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_resource_list():
    if not os.path.isdir(settings.CONFIG_DIR):
        os.mkdir(settings.CONFIG_DIR)
    if not os.path.isfile(settings.CONFIG_FILE):
        f=open(settings.CONFIG_FILE,'w')
        f.close()
    with open(settings.CONFIG_FILE,'r') as f:
        resources=yaml.load(f)
    return(resources)

def write_resource_list(resource_dict):
    with open(settings.CONFIG_FILE, 'w') as f:
        yaml.dump(resource_dict, f, default_flow_style=False)

def print_resource_list():
    resource_dict=get_resource_list()
    if resource_dict!=None:
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
    else:
        print("No Configured Connections Found:\n\t"+
                        " Try [cexec configure] to add a new resource")

def get_resource(name):
    resources=get_resource_list()
    resource=resources.get(name,None)
    print(resource)
    if resource==None:
        logger.error("This resource does not exist: Exiting")
        sys.exit()    
    return resource

def ssh_execute(command):
    logger.info("Calling command: {}".format(command))
    p=subprocess.Popen([command],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
    p.wait()
    return p
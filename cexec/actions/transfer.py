import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import subprocess
import os
import sys
from ..utils import settings
from ..utils.resource_interpreter import get_resource
from ..utils.ssh_handler import ssh_execute
from .status import status_ssh

def transfer_ssh(resource,args):
    #Get external project Directory
    with open(settings.DISTRIBUTED_PIDS,'r') as f:
        lines=f.readlines()
    for line in lines:
        if line.split(":")[0]==args.name:
            external_dir=line.split(":")[1]
            local_dir=external_dir.split("cexec_exec_directory")[1]
            command='rsync -r '+\
                resource['uname']+'@'+resource['hostname']+":"+\
                external_dir+'/* '+local_dir+"/."
            #print(command)
            p=subprocess.Popen(command,
                shell=True)
            p.wait()
            if status_ssh(resource,args,verbose=False):
                print("Collected all results, removing from active list")
                with open(settings.DISTRIBUTED_PIDS,'r') as f:
                    lines2=f.readlines()
                new_lines=[]
                for line2 in lines2:
                    if line2.split(':')[1]!=external_dir:
                        new_lines.append(line2)
                with open(settings.DISTRIBUTED_PIDS,'w') as f:
                    f.writelines(new_lines)
            else:
                print("Process is currently running on resource")
                print("\tNot removing from running resources")


def transfer_slurm(resource):
    pass

def transfer_torque(resource):
    pass

def transfer_aws(resource):
    pass

def transfer_google_cloud(resource):
    pass

def transfer_azure(resource):
    pass

def transfer_openstack(resource):
    pass

    
def main(args):
    resource=get_resource(args.name)
    logger.info("Args Called: {}|".format(args.name))
    if resource['type'] == 'ssh':
        logger.info("Grabbed resource: {}|{}|{}@{}".format(args.name,resource['type'],resource['uname'],resource['hostname']))
        transfer_ssh(resource,args)
    elif resource['type'] == 'slurm':
        transfer_ssh(resource)
    elif resource['type'] == 'torque':
        transfer_ssh(resource)
    elif resource['type'] == 'aws':
        transfer_ssh(resource)
    elif resource['type'] == 'google_cloud':
        transfer_ssh(resource)
    elif resource['type'] == 'azure':
        transfer_ssh(resource)
    elif resource['type'] == 'openstack':
        transfer_openstack(resource)    
    else:
        print("Option "+resource['type']+" not supported")
        print("\tChoose from {ssh | slurm | torque | aws |"+
                            " google_cloud | azure | openstack}")
    
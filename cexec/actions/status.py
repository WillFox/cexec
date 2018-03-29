import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import subprocess
import os
import sys
from ..utils import settings
from ..utils.resource_interpreter import get_resource
from ..utils.ssh_handler import ssh_execute

def status_ssh(resource,args):
    #grab pid/execution dir
    with open(settings.DISTRIBUTED_PIDS,'r') as f:
        lines=f.readlines()
    run_list=[]
    for line in lines:
        if line.split(":")[0]==args.name:
            run_list.append(line.split("\n")[0].split(":"))
    #Request ps status from external server
    for process in run_list:
        pid=process[2]
        p=ssh_execute("ssh "+resource['uname']+"@"+resource['hostname']+" 'ps -F {}'".format(pid))
        error=p.stderr.readlines()
        if error!=[]:
            print(p.stderr.readlines())
        process_lines=p.stdout.readlines()
        if len(process_lines)>1:
            print("\tProcess [{}] RUNNING on [{}]".format(pid,args.name))
        else:
            print("\tProcess [{}] COMPLETED on [{}]".format(pid,args.name))
            print("Run [cexec transfer -n {}] to retrieve results".format(args.name))
        
def status_slurm(resource):
    pass

def status_torque(resource):
    pass

def status_aws(resource):
    pass

def status_google_cloud(resource):
    pass

def status_azure(resource):
    pass

def status_openstack(resource):
    pass

    
def main(args):
    resource=get_resource(args.name)
    logger.info("Args Called: {}|".format(args.name))
    if resource['type'] == 'ssh':
        logger.info("Grabbed resource: {}|{}|{}@{}".format(args.name,resource['type'],resource['uname'],resource['hostname']))
        status_ssh(resource,args)
    elif resource['type'] == 'slurm':
        status_ssh(resource)
    elif resource['type'] == 'torque':
        status_ssh(resource)
    elif resource['type'] == 'aws':
        status_ssh(resource)
    elif resource['type'] == 'google_cloud':
        status_ssh(resource)
    elif resource['type'] == 'azure':
        status_ssh(resource)
    elif resource['type'] == 'openstack':
        status_openstack(resource)    
    else:
        print("Option "+resource['type']+" not supported")
        print("\tChoose from {ssh | slurm | torque | aws |"+
                            " google_cloud | azure | openstack}")
    
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import subprocess
import os
import sys
from ..utils import settings
from ..utils.resource_interpreter import get_resource
from ..utils.ssh_handler import ssh_execute

def status_ssh(resource,args,verbose=True):
    #grab pid/execution dir
    with open(settings.DISTRIBUTED_PIDS,'r') as f:
        lines=f.readlines()
    run_list=[]
    run_dir=[]
    for line in lines:
        if line.split(":")[0]==args.name:
            run_list.append(line.split("\n")[0].split(":"))
    #Request ps status from external server
    done=True
    for process in run_list:
        pid=process[2]
        p=ssh_execute("ssh "+resource['uname']+"@"+resource['hostname']+" 'ps -f {}'".format(pid), verbose=verbose)
        error=p.stderr.readlines()
        if error!=[]:
            print(p.stderr.readlines())
        process_lines=p.stdout.readlines()
        if len(process_lines)>1:
            if verbose: print("\tProcess [{}] RUNNING on [{}]".format(pid,args.name))
            done=False
        else:
            if verbose: print("\tProcess [{}] COMPLETED on [{}]".format(pid,args.name))
            if verbose: print("Run [cexec transfer -n {}] to retrieve results".format(args.name))
    p=ssh_execute("ssh "+resource['uname']+"@"+resource['hostname']+" 'cat "+process[1]+"/cexec.out'",verbose=verbose)
    error=p.stderr.readlines()
    if error!=[]:
        print(p.stderr.readlines())
    file_lines=p.stdout.readlines()
    #if pid=="-1": done=True
    return [done,file_lines]

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

    
def main(args,verbose=True):
    resource=get_resource(args.name)
    if verbose: logger.info("Args Called: {}".format(args.name))
    done=True
    if resource['type'] == 'ssh':
        if verbose: logger.info("Grabbed resource: {} | {} | {}@{}".format(args.name,resource['type'],resource['uname'],resource['hostname']))
        done=status_ssh(resource,args,verbose=verbose)
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
    return(done)
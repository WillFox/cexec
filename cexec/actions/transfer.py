import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import subprocess
import os
import sys
from ..utils import settings
from ..utils.resource_interpreter import get_resource
from ..utils.ssh_handler import ssh_execute

def transfer_ssh(resource,args):
    #Get external project Directory
    p=ssh_execute("ssh "+resource['uname']+"@"+resource['hostname']+" 'printf $HOME' | cut -d\\\\ -f2")
    error=p.stderr.readlines()
    if error!=[]:
        print(p.stderr.readlines())
    home=p.stdout.readlines()[0].decode('ASCII').strip('\n')
    logger.info("External $HOME directory is {}".format(home))
    #Copy Files
    local_dir=os.environ.get('PWD',None)
    if local_dir==None:
        logger.error("$PWD not in environment and needed for execution")
        sys.exit()
    external_dir=os.path.join(home,cexec.settings.DISTRIBUTED_DIR_BASE)
    external_dir=external_dir+local_dir
    logger.info("External execution directory is: {}".format(external_dir))
    p=ssh_execute('ssh '+resource['uname']+'@'+resource['hostname']+' "mkdir -p '+external_dir+'"')
    error=p.stderr.readlines()
    if error!=[]:
        print(p.stderr.readlines())
    p=ssh_execute('rsync -r * '+resource['uname']+'@'+resource['hostname']+':'+external_dir)
    error=p.stderr.readlines()
    if error!=[]:
        print(p.stderr.readlines())
    #Execute Script
    p=ssh_execute('ssh '+resource['uname']+'@'+resource['hostname']+' "cd '+external_dir+";"+args.execution_command+' > cexec.out 2>&1 & "')
    out=p.stdout.readlines()
    print(out)
    error=p.stderr.readlines()
    print(p.stderr.readlines())
    if error!=[]:
        print(p.stderr.readlines())
    
    #Add status and PID

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
    logger.info("Args Called: {}|{}".format(args.name,args.execution_command))
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
    
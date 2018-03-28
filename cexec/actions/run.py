import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import subprocess
import os
import sys
from ..utils import settings
from ..utils.ssh_handler import ssh_execute, ssh_execute_no_wait
from ..utils.resource_interpreter import get_resource

def run_ssh(resource,args):
    #Get external project Directory
    p=ssh_execute("ssh "+resource['uname']+"@"+resource['hostname']+
                                    " 'printf $HOME' | cut -d\\\\ -f2")
    error=p.stderr.readlines()
    if error!=[]:
        print(p.stderr.readlines())
    home=p.stdout.readlines()[0].decode('ASCII').strip('\n')
    logger.info("External $HOME directory is [{}]".format(home))
    #Copy Files
    local_dir=os.environ.get('PWD',None)
    if local_dir==None:
        logger.error("$PWD not in environment and needed for execution")
        sys.exit()
    external_dir=os.path.join(home,settings.DISTRIBUTED_DIR_BASE)
    external_dir=external_dir+local_dir
    logger.info("External execution directory is [{}]".format(external_dir))
    p=ssh_execute('ssh '+resource['uname']+'@'+resource['hostname']+
                                            ' "mkdir -p '+external_dir+'"')
    error=p.stderr.readlines()
    if error!=[]:
        print(p.stderr.readlines())
    p=ssh_execute('rsync -r * '+resource['uname']+'@'+resource['hostname']+
                                                        ':'+external_dir)
    error=p.stderr.readlines()
    if error!=[]:
        print(p.stderr.readlines())
    #Execute Script by calling cexec worker
    if '"' in args.execution_command:
        logger.warn('Command includes a double quote (") and may cause '+
            'undesirable results. Swith to single quotes to avoid this '+
            'warning and undesirable outcomes')
    ssh_out_file="ssh_out.txt"
    #print(resource)
    p=ssh_execute_no_wait('ssh '+
        resource['uname']+'@'+resource['hostname']+
        ' "'+resource['exec_dir']+'/cexec_worker '+
        'run '+"'"+external_dir+"' '" +
        args.execution_command+"'"+'" > '+ssh_out_file)
    import time
    time.sleep(1) 
    #wait for some output (this might need to be adjusted based on ssh connect time)
    with open(ssh_out_file,'r') as f:
        lines=f.readlines()
    os.remove(ssh_out_file)
    for line in lines:
        if "PID" in line:
            pid_launched=line.split(":")[1]
    logger.info("Pid on resource {} is {}".format(args.name,pid_launched))
    #Store PID as currently being executed
    with open(settings.DISTRIBUTED_PIDS,'a') as f:
        f.writelines([line])

    #Add status and PID

    

def run_slurm(resource):
    pass

def run_torque(resource):
    pass

def run_aws(resource):
    pass

def run_google_cloud(resource):
    pass

def run_azure(resource):
    pass

def run_openstack(resource):
    pass

    
def main(args):
    resource=get_resource(args.name)
    logger.info("Args Called: {}|{}".format(args.name,args.execution_command))
    if resource['type'] == 'ssh':
        logger.info("Grabbed resource: {}|{}|{}@{}".format(
            args.name,
            resource['type'],
            resource['uname'],
            resource['hostname']
            ))
        run_ssh(resource,args)
    elif resource['type'] == 'slurm':
        run_ssh(resource)
    elif resource['type'] == 'torque':
        run_ssh(resource)
    elif resource['type'] == 'aws':
        run_ssh(resource)
    elif resource['type'] == 'google_cloud':
        run_ssh(resource)
    elif resource['type'] == 'azure':
        run_ssh(resource)
    elif resource['type'] == 'openstack':
        run_openstack(resource)    
    else:
        print("Option "+resource['type']+" not supported")
        print("\tChoose from {ssh | slurm | torque | aws |"+
                            " google_cloud | azure | openstack}")
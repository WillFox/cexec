import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#logging.disable(logging.CRITICAL)
import subprocess
import os
import sys
import psutil
import time
from ..utils import settings
from ..utils.ssh_handler import ssh_execute
from ..utils.resource_interpreter import get_resource, get_resource_type


def run_ssh(args):
    command=args.execution_command
    directory=args.directory
    logger.info("Running Command")
    pid=str(subprocess.Popen(["/bin/bash","-c",command+" > cexec.out 2>&1 &"],
        cwd=directory#,
        #shell=True
        ).pid)
    time.sleep(2)
    pid_matches=subprocess.Popen("pgrep -f '{}'".format(command),#.split()[0]),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    final_pid= -1
    lines=pid_matches.stdout.readlines()
    for line in lines:
        tmp_pid=line.decode('ASCII').split('\n')[0]
        if int(tmp_pid)>=int(pid) and int(tmp_pid)<=int(pid)+50:
            final_pid=tmp_pid
            break
    logger.info("Correlating the following id's {} & {}".format(pid,final_pid))
    pid=str(final_pid)
    cexec_dir=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    pid_file=settings.LOCAL_PIDS
    with open(settings.LOCAL_PIDS,'r') as f:
        lines=f.readlines()
    with open(pid_file,'a') as f:
        f.write(directory+":"+pid+'\n')    
    print("PIDOUT:"+pid)
    #print("PIDOUT:"+str(os.getppid()))

def run_slurm():
    pass

def run_torque():
    pass

def run_aws():
    pass

def run_google_cloud():
    pass

def run_azure():
    pass

def run_openstack():
    pass

def main(args):
    logger.info("Args Called| {}".format(args.execution_command))
    resource_type=get_resource_type()
    if resource_type == 'ssh':
        run_ssh(args)
    elif resource_type == 'slurm':
        run_ssh(resource_type)
    elif resource_type == 'torque':
        run_ssh()
    elif resource_type == 'aws':
        run_ssh()
    elif resource_type == 'google_cloud':
        run_ssh()
    elif resource_type == 'azure':
        run_ssh()
    elif resource_type == 'openstack':
        run_openstack()    
    else:
        print("Option "+resource_type+" not supported")
        print("\tChoose from {ssh | slurm | torque | aws |"+
                            " google_cloud | azure | openstack}")
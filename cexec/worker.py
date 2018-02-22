"""
Function to initiate various tasks on a remote host
    1. cexec_worker status
    2. cexec_worker transfer
    3. cexec_worker kill

"""
import subprocess
import sys
import logging
import os
from .worker_actions import run
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def worker_run(args):
    run.main()
    
def worker_status(args):
    cexec_dir=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    pid_file=os.path.join(cexec_dir,'externally_called_pids.txt')
    with open(pid_file,'r') as f:
        lines=f.readlines()
    for line in lines:

def worker_clean(args):
    cexec_dir=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    pid_file=os.path.join(cexec_dir,'externally_called_pids.txt')
    f=open(pid_file,'w')
    f.close()

def main(args):
    #execute command in desiganted directory
    logger.info("Worker call made:{}".format(args))    
    if args[1]=='run':
        worker_run(args)
    if args[1]=='status':
        worker_status(args)
    if args[1]=='clean':
        worker_clean(args)

if __name__=="__main__":
    main(sys.argv)
"""
Function to initiate various tasks on a remote host
    1. cexec_worker status
    2. cexec_worker transfer
    3. cexec_worker kill

"""
import sys
import logging
import os
import argparse
from .utils import version
from .worker_actions import run
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from .utils import settings
settings.init()
if not settings.SET_VERBOSE:
    logging.disable(logging.CRITICAL)


def worker_run(args):
    #print(args)
    run.main(args)
    
def worker_status(args):
    cexec_dir=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    pid_file=os.path.join(cexec_dir,'externally_called_pids.txt')
    with open(pid_file,'r') as f:
        lines=f.readlines()
    for line in lines:
        pass
def worker_clean(args):
    cexec_dir=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    pid_file=os.path.join(cexec_dir,'externally_called_pids.txt')
    f=open(pid_file,'w')
    f.close()

def worker_kill(args):
    cexec_dir=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    pid_file=os.path.join(cexec_dir,'externally_called_pids.txt')
    f=open(pid_file,'w')
    f.close()

####################
#WORKER MENU PARSER#
####################
def worker_menu_parser():
    parser = argparse.ArgumentParser(
        description="A command line interface to simplify distributed "+
                "execution\nYou know, do da stuffs in the cloud!   =)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="A FoxiDev Production")
    parser.add_argument(
        '--version', action='version', version=version.__version__)
    subparsers = parser.add_subparsers(
        dest="parser")
    
    _worker_run(subparsers)
    _worker_status(subparsers)
    _worker_clean(subparsers)
    _worker_kill(subparsers)
    return parser.parse_args()

def _worker_run(subparsers): 
    parse_run = subparsers.add_parser(
        "run", help="Let's make a cloud mull over some data!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse_run.set_defaults(func=worker_run)
    parse_run.add_argument(
        "directory", 
        type=str,
        metavar="dir",
        help="where to run command on resource")
    parse_run.add_argument(
        "execution_command", 
        type=str,
        metavar="command",
        help="command to be run on resource")

def _worker_status(subparsers): 
    con = subparsers.add_parser(
        "status", help="What's my sky stuff doing?",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=worker_status)
    con.add_argument(
        '-n',
        '--name', 
        type=str,
        metavar="resource_name",
        help="Specific resource to query status.")

def _worker_clean(subparsers): 
    con = subparsers.add_parser(
        "kill", help="Stormy clouds must die! All my results will be erased!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=worker_kill)

def _worker_kill(subparsers): 
    con = subparsers.add_parser(
        "kill", help="Stormy clouds must die! All my results will be erased!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=worker_kill)

def main():
    #execute command in desiganted directory
    args=worker_menu_parser()
    logger.info("Worker call made:{}".format(args))  
    
    if not args.parser==None:
        args.func(args)
    else:
        print("No input provided: Are you sure you want to call cexec_worker?")

if __name__=="__main__":
    main()
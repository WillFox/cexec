#!/usr/bin/env python

"""
Function to initiate the various steps of the program including
    1. cexec configure batch|ssh|aws <__user_given_name__>
    2. cexec "<command>" <__user_given_name__>
    3. cexec status <__user_given_name__>
    4. cexec transfer <__user_given_name__>
    5. cexec kill <__user_given_name__>

"""
from .actions import configure, run, transfer,status
from .utils.resource_interpreter import get_resource_list, print_resource_list
import logging
from .utils import version

import sys
import argparse
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.disable(logging.CRITICAL)
from .utils import settings
settings.init()
def configure_main(args):
    logger.info("We are setting up a cloud. | Do you feel like Zeus yet?")
    print(args)
    configure.main(args)

def run_main(args):
    logger.info("We are going to try to get a cloud to follow our orders!")
    #print(args)
    run.main(args)

def status_main(args):
    logger.info("Click your heels three times and wish"+
                                    " for the cloud to respond!")
    status.main(args)

def transfer_main(args):
    logger.info("Should we expect a drizzle or hurricane from this transfer")
    print(args)
    transfer.main(args)
def kill_main(args):
    logger.info("Clouds all go in time!  This one's"+
                                " time has come. RIP Cloud Willis!")
    print(args)
    #kill()

def resources_main(args):
    logger.info("Clouds! Sound off!")
    print_resource_list()

def menu_parser():
    parser = argparse.ArgumentParser(
        description="A command line interface to simplify distributed "+
                "execution. You know, do da stuffs in the cloud!   =)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="A FoxiDev Production")
    
    parser.add_argument(
        '--version', action='version', version=version.__version__)
    subparsers = parser.add_subparsers(
        dest="parser")
    
    _configure(subparsers)
    _run(subparsers)
    _status(subparsers)
    _transfer(subparsers)
    _kill(subparsers)
    _resources(subparsers)
    return parser.parse_args()

def _configure(subparsers): 
    con = subparsers.add_parser(
        "configure", help="Let's add a new cloud to the sky!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=configure_main)
    con.add_argument(
        '-t',
        '--type', 
        type=str,
        metavar="resource_type",
        help="Type of resource to configure {ssh | slurm | torque | aws |"+
                                    " google_cloud | azure | openstack}",
        default="ssh")
    con.add_argument( 
        "-n",
        "--name",
        type=str,
        metavar="resource_name",
        required=True,
        help="Unique name for resource")

def _run(subparsers): 
    parse_run = subparsers.add_parser(
        "run", help="Let's make a cloud mull over some data!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse_run.set_defaults(func=run_main)
    parse_run.add_argument(
        'name', 
        type=str,
        metavar="resource_name",
        help="Specific resource to run on.")
    parse_run.add_argument( 
        'execution_command',
        metavar="command",
        type=str,
        help="command to be run on resource")
    

def _status(subparsers): 
    con = subparsers.add_parser(
        "status", help="What's my sky stuff doing?",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=status_main)
    con.add_argument(
        '-n',
        '--name', 
        type=str,
        metavar="resource_name",
        help="Specific resource to query status.")

def _transfer(subparsers): 
    con = subparsers.add_parser(
        "transfer", help="Let's pull my results in from the cloud!  "+
                                                        "ITS RAINING!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=transfer_main)
    con.add_argument(
        '-n',
        '--name', 
        type=str,
        metavar="resource_name",
        help="Specific resource to query status.")

def _kill(subparsers): 
    con = subparsers.add_parser(
        "kill", help="Stormy clouds must die! All my results will be erased!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=kill_main)

def _resources(subparsers): 
    res_list = subparsers.add_parser(
        "resource", help="List all distributed devices available",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    res_list.set_defaults(func=resources_main)

def main():
    if len(sys.argv)==1:#pthon 2 tox compatability
        print("No input provided: try [cexec --help] for options")
        sys.exit()
    args=menu_parser()
    if not args.parser==None:
        args.func(args)
    else:
        print("No input provided: try [cexec --help] for options")

if __name__=="__main__":
    main()
#!/usr/bin/env python

"""
Function to initiate the various steps of the program including
    1. cexec configure batch|ssh|aws <__user_given_name__>
    2. cexec "<command>" <__user_given_name__>
    3. cexec status <__user_given_name__>
    4. cexec transfer <__user_given_name__>
    5. cexec kill <__user_given_name__>

"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import traceback
import os
import logging
import sys
import subprocess
import random
import re
import time
import yaml

from utils import get_resource_list, print_resource_list
from parsers import menu_parser
import actions.configure
import actions.kill
import actions.run
import actions.transfer

import settings

settings.init()
#from utils import extract_yaml_files

#from execution.driver import Workflow, Application
#from execution.submission import build_submission


def configure(args):
    logger.info("We are setting up a cloud. | Do you feel like Zeus yet?")
    actions.configure.main(args)

def run(args):
    logger.info("We are going to try to get a cloud to follow our orders!")
    actions.run.main(args)

def status(args):
    logger.info("Click your heels three times and wish"+
                                    " for the cloud to respond!")
    print(args)

def transfer(args):
    logger.info("Should we expect a drizzle or hurricane from this transfer")
    print(args)
    actions.transfer.main()
def kill(args):
    logger.info("Clouds all go in time!  This one's"+
                                " time has come. RIP Cloud Willis!")
    print(args)
    actions.kill.main()

def resources(args):
    logger.info("Clouds! Sound off!")
    print_resource_list()

def main():
    args=menu_parser(configure,run,status,transfer,kill,resources)
    #logger.info("MODE: "+args.subparser_name)
    if not args.parser==None:
        args.func(args)
    else:
        print("No input provided: try [cexec --help] for options")

if __name__=="__main__":
    main()
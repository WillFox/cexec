#!/usr/bin/env python

"""
Function to initiate the various steps of the program including
    1. cexec configure batch|ssh|aws <__user_given_name__>
    2. cexec "<command>" <__user_given_name__>
    3. cexec status <__user_given_name__>
    4. cexec transfer <__user_given_name__>
    5. cexec kill <__user_given_name__>

"""
from .utils.resource_interpreter import get_resource_list, print_resource_list
from .utils.parsers import menu_parser
from .actions import configure, run, transfer
from .utils import settings
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings.init()

def configure(ctype,name):
    logger.info("We are setting up a cloud. | Do you feel like Zeus yet?")
    actions.configure.main(ctype,name)

def run(name,command):
    logger.info("We are going to try to get a cloud to follow our orders!")
    actions.run.main(name,command)

def status(name):
    logger.info("Click your heels three times and wish"+
                                    " for the cloud to respond!")
    actions.run.status(name)
    print(args)

def transfer(name):
    logger.info("Should we expect a drizzle or hurricane from this transfer")
    print(args)
    actions.transfer.main(name)
def kill(name):
    logger.info("Clouds all go in time!  This one's"+
                                " time has come. RIP Cloud Willis!")
    print(args)
    actions.kill.main(name)

def resources(name=None):
    logger.info("Clouds! Sound off!")
    print_resource_list(name)

#!/usr/bin/env python

"""
Function to initiate the various steps of the program including
    1. cexec configure batch|ssh|aws <__user_given_name__>
    2. cexec "<command>" <__user_given_name__>
    3. cexec status <__user_given_name__>
    4. cexec transfer <__user_given_name__>
    5. cexec kill <__user_given_name__>

"""
from __init__.py import configure, run, status, transfer, kill, resources

def configure(args):
    logger.info("We are setting up a cloud. | Do you feel like Zeus yet?")
    configure(args)

def run(args):
    logger.info("We are going to try to get a cloud to follow our orders!")
    run(args)

def status(args):
    logger.info("Click your heels three times and wish"+
                                    " for the cloud to respond!")
    print(args)

def transfer(args):
    logger.info("Should we expect a drizzle or hurricane from this transfer")
    print(args)
    transfer()
def kill(args):
    logger.info("Clouds all go in time!  This one's"+
                                " time has come. RIP Cloud Willis!")
    print(args)
    kill()

def resources(args):
    logger.info("Clouds! Sound off!")
    print_resource_list()

def main():
    args=menu_parser(configure,run,status,transfer,kill,resources)
    if not args.parser==None:
        args.func(args)
    else:
        print("No input provided: try [cexec --help] for options")

if __name__=="__main__":
    main()
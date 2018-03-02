#!/usr/bin/env python

"""
Each function configures its respective cloud technology
"""
from ..utils import settings
import logging
from ..utils.resource_interpreter import get_resource_list, write_resource_list
from ..utils.ssh_handler import ssh_execute
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def configure_ssh(args):
    logger.info("Attempting to add| type-{}||name-{}".format(
                                                args.type,args.name))
    #UGLY PYTHON2 and PYTHON3 compatability solution
    try:
        input = raw_input
    except NameError:
        pass
    #Request info for configuration
    uname=raw_input("login id required for ssh [id in id@hostname]:")
    hostname=raw_input("Hostname for ssh [hostname in id@hostname]:")
    #Add to configuration file settings.CONFIG_FILE
    resource_dict=get_resource_list()
    if resource_dict==None:
        resource_dict={}
    resource_dict[args.name]={'uname':uname,'type':'ssh',
                                'hostname':hostname,'port':'22'}
    
    #Try to connect via ssh
    #p=subprocess.Popen(["ssh "+uname+"@"+hostname+' echo $USER'],
    p=ssh_execute("ssh-copy-id "+uname+"@"+hostname)
    print("Verifying passwordless login succeeded")
    p=ssh_execute("ssh "+uname+"@"+hostname+' echo $USER')
    success=False
    for line in p.stdout.readlines():
        if uname in str(line):
            success=True
    if not success:
        logger.error("Passwordless login has not been accepted,"+
                            " cexec will not work as currently configured")
    else:
        print("You ssh connection is now set up as passwordless:\n\t "+
            "You should only need to ever configure this once per resource")
    logger.info("Writing {0}@{1} to resouces".format(uname,hostname))
    #check if cexec installed on resource
    p=ssh_execute("ssh-copy-id "+uname+"@"+hostname+' "which cexec"')
    if p.stdout.readlines()==None:
        print(p.stdout.readlines())

    print(p.stdout.readlines())
    #install cexec in user directory (ask to do this)

    #append cexec path (ask to do this)

    #Verify cexec on resource

    #Add resource to list of available resources
    write_resource_list(resource_dict)

def configure_slurm(args):
    pass

def configure_torque(args):
    pass

def configure_aws(args):
    pass

def configure_google_cloud(args):
    pass

def configure_azure(args):
    pass

def configure_openstack(args):
    pass

def main(args):
    if args.type == 'ssh':
        configure_ssh(args)
    elif args.type == 'slurm':
        configure_ssh(args)
    elif args.type == 'torque':
        configure_ssh(args)
    elif args.type == 'aws':
        configure_ssh(args)
    elif args.type == 'google_cloud':
        configure_ssh(args)
    elif args.type == 'azure':
        configure_ssh(args)
    elif args.type == 'openstack':
        configure_openstack(args)    
    else:
        print("Option "+args.type+" not supported")
        print("\tChoose from {ssh | slurm | torque | aws |"+
                            " google_cloud | azure | openstack}")

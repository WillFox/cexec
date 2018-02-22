import argparse
def menu_parser(configure,run,status,transfer,kill,resources):
    parser = argparse.ArgumentParser(
        description="A command line interface to simplify distributed "+
                "execution\nYou know, do da stuffs in the cloud!   =)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="A FoxiDev Production")
    import version
    parser.add_argument(
        '--version', action='version', version=version.__version__)
    subparsers = parser.add_subparsers(
        dest="parser")
    
    _configure(subparsers,configure)
    _run(subparsers,run)
    _status(subparsers,status)
    _transfer(subparsers,transfer)
    _kill(subparsers,kill)
    _resources(subparsers,resources)
    return parser.parse_args()

def _configure(subparsers,configure): 
    con = subparsers.add_parser(
        "configure", help="Let's add a new cloud to the sky!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=configure)
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

def _run(subparsers,run): 
    parse_run = subparsers.add_parser(
        "run", help="Let's make a cloud mull over some data!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse_run.set_defaults(func=run)
    parse_run.add_argument('-e',"--execution-command", 
        type=str,
        metavar="command",
        required=True,
        help="command to be run on resource")
    parse_run.add_argument(
        '-n',
        '--name', 
        type=str,
        metavar="resource_name",
        required=True,
        help="Specific resource to run on.")

def _status(subparsers,status): 
    con = subparsers.add_parser(
        "status", help="What's my sky stuff doing?",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=status)
    con.add_argument(
        '-n',
        '--name', 
        type=str,
        metavar="resource_name",
        help="Specific resource to query status.")

def _transfer(subparsers,transfer): 
    con = subparsers.add_parser(
        "transfer", help="Let's pull my results in from the cloud!  "+
                                                        "ITS RAINING!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=transfer)

def _kill(subparsers,kill): 
    con = subparsers.add_parser(
        "kill", help="Stormy clouds must die! All my results will be erased!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=kill)

def _resources(subparsers,resources): 
    res_list = subparsers.add_parser(
        "resource", help="List all distributed devices available",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    res_list.set_defaults(func=resources)

####################
#WORKER MENU PARSER#
####################
def worker_menu_parser(configure,run,status,transfer,kill,resources):
    parser = argparse.ArgumentParser(
        description="A command line interface to simplify distributed "+
                "execution\nYou know, do da stuffs in the cloud!   =)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="A FoxiDev Production")
    import version
    parser.add_argument(
        '--version', action='version', version=version.__version__)
    subparsers = parser.add_subparsers(
        dest="parser")
    
    _worker_configure(subparsers,configure)
    _worker_run(subparsers,run)
    _worker_status(subparsers,status)
    _worker_transfer(subparsers,transfer)
    _worker_kill(subparsers,kill)
    _worker_resources(subparsers,resources)
    return parser.parse_args()

def _worker_configure(subparsers,configure): 
    con = subparsers.add_parser(
        "configure", help="Let's add a new cloud to the sky!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=configure)
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

def _worker_run(subparsers,run): 
    parse_run = subparsers.add_parser(
        "run", help="Let's make a cloud mull over some data!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse_run.set_defaults(func=run)
    parse_run.add_argument('-e',"--execution-command", 
        type=str,
        metavar="command",
        required=True,
        help="command to be run on resource")
    parse_run.add_argument(
        '-n',
        '--name', 
        type=str,
        metavar="resource_name",
        required=True,
        help="Specific resource to run on.")

def _worker_status(subparsers,status): 
    con = subparsers.add_parser(
        "status", help="What's my sky stuff doing?",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=status)
    con.add_argument(
        '-n',
        '--name', 
        type=str,
        metavar="resource_name",
        help="Specific resource to query status.")

def _worker_transfer(subparsers,transfer): 
    con = subparsers.add_parser(
        "transfer", help="Let's pull my results in from the cloud!  "+
                                                        "ITS RAINING!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=transfer)

def _worker_kill(subparsers,kill): 
    con = subparsers.add_parser(
        "kill", help="Stormy clouds must die! All my results will be erased!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    con.set_defaults(func=kill)

def _worker_resources(subparsers,resources): 
    res_list = subparsers.add_parser(
        "resource", help="List all distributed devices available",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    res_list.set_defaults(func=resources)
def run_ssh(args):
    name=args[2]
    directory=args[3]
    command=args[4]
    for arg in range(len(args)-5):
        command=command+" "+args[arg+5]
    pid=str(subprocess.Popen([command+" > cexec.out 2>&1"],
        cwd=directory,
        shell=True
        ).pid)
    #print (return to master process) and store pid
    cexec_dir=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    pid_file=os.path.join(cexec_dir,'externally_called_pids.txt')
    with open(pid_file,'r') as f:
        lines=f.readlines()
    for line in lines:
        if line.split(':')[0]==name:
            if line.split(':')[1]==directory:
                print("ERROR: Incomplete matching execution present in dir")
                print("If you believe this is a mistake, try [cexec_worker"+
                                " clean] on the resource: {}".format(name))
                sys.exit()    
    with open(pid_file,'a') as f:
        f.write(name+":"+directory+":"+pid+'\n')    
    print("PIDOUT:"+pid)

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
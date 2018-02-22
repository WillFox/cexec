"""
Function to initiate various tasks on a remote host
    1. cexec_worker status
    2. cexec_worker transfer
    3. cexec_worker kill

"""
import subprocess
import sys
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(args):
    #execute command in desiganted directory
    logger.info("Worker call made:{}".format(args))    
    directory=args[1]
    command=args[2]
    for arg in range(len(args)-3):
        command=command+" "+args[arg+3]
    print(command)
    pid=subprocess.Popen([command+" > cexec.out 2>&1"],
        cwd=directory,
        shell=True
        ).pid

    #print (return to master process) and store pid
    print(pid)
    cexec_dir=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    pid_file=os.path.join(cexec_dir,'externally_called_pids.txt')
    with open(pid_file,'w') as f:
        f.write(name+":"+directory+":"+pid)    
    
if __name__=="__main__":
    main(sys.argv)
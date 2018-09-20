import logging
import subprocess
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ssh_execute(command,verbose=True):
    if verbose: logger.info("Calling command [{}]".format(command))
    p=subprocess.Popen([command],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
    p.wait()
    return p

def ssh_execute_no_wait(command):
    logger.info("Calling command but not waiting [{}]".format(command))
    p=subprocess.Popen([command],
                shell=True,
                stdin=None,
                stdout=None,
                stderr=None,
                close_fds=True)
    
    return p
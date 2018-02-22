import logging
import subprocess
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ssh_execute(command):
    logger.info("Calling command: {}".format(command))
    p=subprocess.Popen([command],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
    p.wait()
    return p
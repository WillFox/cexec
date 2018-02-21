"""
Function to initiate various tasks on a remote host
    1. cexec_worker status
    2. cexec_worker transfer
    3. cexec_worker kill

"""

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Worker call made")    
    pass

if __name__=="__main__":
    main()
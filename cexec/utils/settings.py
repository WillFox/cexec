import os

def init():
    global CONFIG_DIR
    CONFIG_DIR=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    global CONFIG_FILE
    CONFIG_FILE=os.path.join(CONFIG_DIR,'resources.yaml')
    global DISTRIBUTED_DIR_BASE
    DISTRIBUTED_DIR_BASE="cexec_exec_directory"
    global RESOURCE_TYPE
    RESOURCE_TYPE=os.path.join(CONFIG_DIR,'resource.type')
    global DISTRIBUTED_PIDS
    DISTRIBUTED_PIDS=os.path.join(CONFIG_DIR,'pids.external')
    global LOCAL_PIDS
    LOCAL_PIDS=os.path.join(CONFIG_DIR,'pids.local')
    global SET_VERBOSE
    SET_VERBOSE=True
    
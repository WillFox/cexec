import os


def init():
    global CONFIG_DIR
    CONFIG_DIR=os.path.join(os.environ.get('HOME','/etc/cexec'),'.cexec')
    global CONFIG_FILE
    CONFIG_FILE=os.path.join(CONFIG_DIR,'resources.yaml')
    global DISTRIBUTED_DIR_BASE
    DISTRIBUTED_DIR_BASE="cexec_exec_directory"
import os
import sys
import subprocess
from cexec.utils.resource_interpreter import get_resource_list
from cexec.utils import settings
settings.init()
def install_src():
    home=os.environ.get("HOME",None)
    if home==None:
        print("Home directory needs to be in environment for installation")
        sys.exit()
    get_resource_list()
    with open(settings.LOCAL_PIDS,'w') as f:
        pass
    with open(settings.DISTRIBUTED_PIDS,'w') as f:
        pass

    #Build src file
    p=subprocess.Popen(
        ["./zip_n_store_src.sh;"+
        " mv cexec_src.zip "+os.path.join(settings.CONFIG_DIR,"cexec_src.zip")+";"
        " rm cexec_src.zip"],
        shell=True)
    p.wait()
    
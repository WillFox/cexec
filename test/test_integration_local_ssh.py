
from cexec.cexec import run_main, transfer_main, status_main

#from cexec import run_main, status_main, transfer_main
import os

#os.environ["HOME"]=os.path.realpath(__file__)


class fake_menu:
    def __init__(self):
        self.name="local"

def test_run():
    args=fake_menu()
    #run_main(args)

def test_status():
    args=fake_menu()
    #status_main(args)

def test_transfer():
    args=fake_menu()
    #transfer_main(args)





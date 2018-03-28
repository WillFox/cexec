#!/usr/bin/env python
import sys
#from setup_script import install_src
from setuptools import setup, find_packages

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

install_src()

with open("cexec/utils/version.py") as f:
    code = compile(f.read(), "cexec/utils/version.py", 'exec')
    exec(code)

install_requires = None
print(install_requires)
print(sys.version_info)
if sys.version_info.major < 3:
    install_requires=['cloud','pyyaml']
print("Install Requires", install_requires)

setup(name='cexec',
      version=__version__,
      description='Automation of distributed execution | assumes programs installed',
      author='William Fox',
      author_email='wfox413@gmail.com',
      url='https://www.github.com/WillFox/cexec/',
      #packages=find_packages(where='./', exclude=['test_runs','test_data'])+['cexec/templates'],
      packages=find_packages(where='./'),
      package_dir={'cexec': 'cexec'},
      keywords='workflow',
      license='LICENSE.txt',
      include_package_data=True,
      zip_safe=False,
      classifiers=['Development Status :: 0 - Development/Experimental',
                   'Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Operating System :: Unix/Linux based',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
              'cexec = cexec.cexec:main',
              'cexec_worker =  cexec.worker:main',
              ]})

#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

with open("cexec/version.py") as f:
    code = compile(f.read(), "cexec/version.py", 'exec')
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
      packages=find_packages(where='./', exclude=['test_runs','test_data'])+['cexec/templates'],
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
              'cexec = cexec.main:main',
              'cexec_worker =  cexec.worker:main',
              ]})

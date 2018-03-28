


Configuration Files:
~/.cexec
  /pids.external  -pids from externally executed processes
  /pids.local     -pids running on external resources
  /resources.yaml -list of external resources available
  /resource.type  -type of resource of this computer

Missing pieces in configure:
-resource.type needs to be created upon configure
-exec_dir needs to be added in resources.yaml upon ssh setup


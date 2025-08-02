import os.path
from os.path import expanduser

from sshconf import read_ssh_config, empty_ssh_config_file

if os.path.exists(expanduser('~/.ssh/config')):
    ssh_configs = read_ssh_config(expanduser("~/.ssh/config"))
else:
    ssh_configs = empty_ssh_config_file()
ssh_hosts = ssh_configs.hosts()

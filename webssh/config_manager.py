from os.path import expanduser

from sshconf import read_ssh_config

ssh_configs = read_ssh_config(expanduser("~/.ssh/config"))
ssh_hosts = ssh_configs.hosts()

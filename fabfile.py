from fabric.api import *

env.hosts = ['34.224.16.226', '54.173.111.119']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/my_key"


def mkdir():
    sudo("mkdir /try")
    sudo("mkdir timber")
    sudo("mkdir /me")

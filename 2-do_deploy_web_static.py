#!/usr/bin/python3
"""
contains fab functions to create an archive of web file
deploy the web content in the archive file to two servers
"""
from datetime import datetime
from fabric.api import *

env.hosts = ['ubuntu@34.224.16.226', 'ubuntu@54.173.111.119']
env.key_filename = '~/.ssh/my_key'

def do_pack():
    """
    creates an archive on the web_static folder in 'versions' folder
    """
    dt = datetime.today().strftime("%Y%m%d%H%M%S")
    archive = "web_static_{}.tgz".format(dt)
    command = "tar -cvzf versions/{} web_static".format(archive)
    local("mkdir -p versions")

    create = local(command)

    if create is not None:
        return archive
    return None

def do_deploy(archive_path):
    """
    Distributes an archive to two webservers.
    unpacks the archive files to the appropriate locations for the server to serve
    """
    from os.path import exists


    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}{}/'.format(path, no_ext))
        sudo('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        sudo('rm /tmp/{}'.format(file_n))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        sudo('rm -rf {}{}/web_static'.format(path, no_ext))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

#!/usr/bin/python3
"""
Generates a .tgz from the contents of web_static folder
execute: fab -f 1-pack_web_static.py
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    creates an archive on the static folder in version folder
    """
    dt = datetime.today().strftime("%Y%m%d%H%M%S")
    archive = "web_static_{}.tgz".format(dt)
    command = "tar -cvzf versions/{} web_static".format(archive)
    local("mkdir -p versions")

    create = local(command)

    if create is not None:
        return archive
    return None

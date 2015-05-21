# -*- coding: utf-8 -*-
"""
Interaction with Grunt-CLI
==========================



"""
from __future__ import unicode_literals

from salt import utils
from salt.exceptions import SaltInvocationError, CommandExecutionError


def __virtual__():
    """
    Only load if grunt cli is available.
    """
    return utils.which('grunt') is not None


def task(name, cwd=None, user=None, env=None):
    """
    Run a task located in a directories gruntfile.

    .. code-block:: yaml

        build-app:
          grunt.task:
             name: build
             dir: /path/to/project

    name
        Name of the task to run

    cwd
        Target directory to run the task in

    user
        User to run grunt with
    """
    ret = {
        'name': name,
        'result': True,
        'comment': '',
        'changes': {}
    }

    if not cwd:
        raise SaltInvocationError('The cwd argument is required')

    cmd = 'grunt {0} --no-color'.format(name)

    result = __salt__['cmd.run_all'](cmd,
                                     cwd=cwd,
                                     runas=user,
                                     env=env,
                                     python_shell=False)

    if result['retcode'] != 0:
        ret['result'] = False
        ret['comment'] = str(result['stdout'])
    else:
        ret['changes']['output'] = str(result['stdout'])

    return ret


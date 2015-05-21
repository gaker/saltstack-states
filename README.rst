========================
SaltStack Modules/States
========================

A dumping ground for SaltStack states/modules that don't exist in
the core.

------
States
------


Grunt
^^^^^

Execute a Grunt-CLI task.

File
    ``_states/grunt.py``


.. code-block:: yaml

    build-app:
      grunt.task:
      name: build
      dir: /path/to/project/with/Gruntfile.js






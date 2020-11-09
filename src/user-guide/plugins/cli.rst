CLI
===

All Cylc subcommands are installed via the ``cylc.command`` `entry point`_.

Cylc plugins may add subcommands using this interface:

.. code-block::

   [options.entry_points]
   cylc.command =
       name-of-subcommand = python.path.to.module:function

Plugins are advised to use the Cylc command line argument parsing
infrastructure.

.. warning::

   The Cylc command line infrastructure is likely to change in the near
   future.

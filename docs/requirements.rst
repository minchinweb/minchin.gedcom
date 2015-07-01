Requirements
============

The main *minchin.gedcom* module, has the following dependencies:

.. include:: ../requirements.txt
   :literal:

Testing
-------

Testing *minchin.gedcom* requires:

.. include:: ../test/requirements.txt
   :literal:

Then run (from the base directory)::

	green tests


Documentation Generation
------------------------
To generation the documentation (this) for *minchin.gedcom*,
*minchin.gedcom* itself must be installed (it is imported in
the process of building the documentation).
The following dependencies are also required:

.. include:: requirements.txt
   :literal:

Then run (on Windows) (from the ``docs`` directory)::

	make html

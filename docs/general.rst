**********************************************************************
General
**********************************************************************

.. contents:: Contents
   :local:


Top level constants and exceptions from the library.

Version
=========

The following constants provide information about the version of the libgit2
library that has been built against. The version number has a
``MAJOR.MINOR.REVISION`` format.

.. py:data:: LIBGIT2_VER_MAJOR

   Integer value of the major version number. For example, for the version
   ``0.26.1``::

      >>> print LIBGIT2_VER_MAJOR
      0

.. py:data:: LIBGIT2_VER_MINOR

   Integer value of the minor version number. For example, for the version
   ``0.26.1``::

      >>> print LIBGIT2_VER_MINOR
      26

.. py:data:: LIBGIT2_VER_REVISION

   Integer value of the revision version number. For example, for the version
   ``0.26.1``::

      >>> print LIBGIT2_VER_REVISION
      1

.. py:data:: LIBGIT2_VERSION

   The libgit2 version number as a string::

      >>> print LIBGIT2_VERSION
      '0.26.1'

Options
=========

.. autofunction:: pygit2.option

Exceptions
==========

.. autoexception:: pygit2.GitError
   :members:
   :show-inheritance:
   :undoc-members:


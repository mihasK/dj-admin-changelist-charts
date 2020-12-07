=============================
Django Admin Changelist Charts
=============================

.. image:: https://badge.fury.io/py/dj-admin-changelist-charts.svg
    :target: https://badge.fury.io/py/dj-admin-changelist-charts

.. image:: https://travis-ci.org/mihasK/dj-admin-changelist-charts.svg?branch=master
    :target: https://travis-ci.org/mihasK/dj-admin-changelist-charts

.. image:: https://codecov.io/gh/mihasK/dj-admin-changelist-charts/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mihasK/dj-admin-changelist-charts

Allows to create simple aggregate charts on changelist page. E.g. piechart or barcharts by product category for products list

Documentation
-------------

The full documentation is at https://dj-admin-changelist-charts.readthedocs.io.

Quickstart
----------

Install Django Admin Changelist Charts::

    pip install dj-admin-changelist-charts

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_admin_changelist_charts.apps.DjAdminChangelistChartsConfig',
        ...
    )

Add Django Admin Changelist Charts's URL patterns:

.. code-block:: python

    from dj_admin_changelist_charts import urls as dj_admin_changelist_charts_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_admin_changelist_charts_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

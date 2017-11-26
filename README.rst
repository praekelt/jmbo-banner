Jmbo Banner
===========
**Jmbo banner application. Banners are typically used to serve ads.**

.. figure:: https://travis-ci.org/praekelt/jmbo-banner.svg?branch=develop
   :align: center
   :alt: Travis

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``jmbo-banner`` to your Python path.

#. Add ``banner`` to your ``INSTALLED_APPS`` setting.

#. Run ``manage.py migrate banner``.

Usage
-----

Content types
-------------

``jmbo-banner`` defines the following content types:

**Button:**

* A banner can consist of several buttons, although usually only two are used.

* A button has a *text* field which can be used to specify its label, and a *link* object which can be used to specify its click-through.

**Banner:**

* A banner can be thought of as a container for promotional content. It can consist of buttons, images and promotional text. Each banner also has a *style* which controls how its contents are rendered.


How does it work?
-----------------
``jmbo-banner`` allows users to create banners in the admin. ``jmbo-banner`` models


Adding your own banner styles
-----------------------------

It is sometimes necessary to have more *styles* in which banners can be rendered. This can easily be achieved by adding a package, ``banner_config`` to one of your own
apps and ensuring that you create your custom style in a ``styles.py`` file. An example structure would be as follows::
    <your app>
        __init__.py
        styles.py


All custom styles should inherit from ``BaseStyle``. For most situations, overriding the ``template_name`` should suffice.

.. code-block:: python
   :caption: banner_config/styles.py

    from banner.styles import BaseStyle


    class CustomStyle(BaseStyle):
        """
        Custom banner style
        """
        template_name = "banner/custom_banner.html"


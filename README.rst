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

* A button has a `text` field which can be used to specify its label, and a `link` object which can be used to specify its click-through.

**Banner:**

* A banner can be thought of as a container for promotional content. It can consist of buttons, images and promotional text


How does it work?
-----------------
``jmbo-banner`` allows users to create banners in the admin. ``jmbo-banner`` models

Adding your own banner styles
-----------------------------



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

``jmbo-banner`` allows users to create and edit banners in the admin. Each banner can optionally have a byline,
a description block, images and CTA buttons. The way in which these components are laid out in each banner is defined
in a banner style.

Content types
-------------

``jmbo-banner`` defines the following content types:

**Button:**

* A banner can consist of several buttons, although usually only two are used.

* A button has a *text* field which can be used to specify its label, and a *link* object which can be used to specify its click-through.

**Banner:**

* A banner can be thought of as a container for promotional content. It can consist of buttons, images and promotional text. Each banner also has a *style* which controls how its contents are rendered.


Banner styles
-------------

``jmbo-banner`` allows you to control how each banner will be rendered. The different ways in which a banner can be rendered can be found in a predefined list of styles.
A style controls how the different components (buttons, images, description) are rendered through a *template partial*.

Adding your own banner styles
-----------------------------

It is sometimes necessary to have more *styles* in which banners can be rendered. This can easily be achieved by adding a package, ``banner_config`` to one of your own
apps and ensuring that you create your custom style in a ``styles.py`` file. An example structure would be as follows::

    <your app>
        ...
        banner_config
            __init__.py
            styles.py


All custom styles **should** inherit from ``BaseStyle``. For most situations, overriding the ``template_name`` should suffice.
It is important to bear in mind a style's template is meant to be used as a partial containing only the banner content.

.. code-block:: python

    from banner.styles import BaseStyle


    class CustomStyle(BaseStyle):
        """
        Custom banner style
        """
        template_name = "banner/custom_banner.html"

The ``CustomStyle`` should then be available for selection in the list of styles.


Getting banners to render on a page
-----------------------------------

Banners are typically rendered as part of a page. This can be achieved by using the ``render_banner`` template tag as shown in below.

.. code-block:: html

    {% extends "base.html" %}
    {% load banner_tags %}

    {% block content %}
        {% render_banner object %}
    {% endblock %}

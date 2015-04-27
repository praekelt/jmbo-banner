Changelog
=========

0.6
---
#. Django 1.6 compatibility.

0.5
---
#. Remove dependency on `jmbo-foundry`.
#. Add tests.

0.4
---
#. Rename `get_absolute_url` method to `get_target_url` since it was breaking Jmbo convention. If you have customized `imagebanner_*.html` then you need to update them.

0.3
---
#. Remove redundant tests.
#. Use newer version of `django-dfp`. If you have customized `dfpbanner_detail.html` or `dfpbanner_list_item.html` then you need to update them.

0.2.6
-----
#. If there is no actual banner and the banner proxy has no image set then don't render anything.
#. Cache templates.

0.2.5
-----
#. Multiple banners that match a regex are now randomized to effect banner rotation.

0.2.4.4
-------
# Hotfix. Split paths on any whitespace.

0.2.4.3
-------
#. Hotfix. Skip over empty paths to avoid an exception.

0.2.4.2
-------
#. Hotfix. Properly fall back to default banner if it is set.

0.2.4.1
-------
#. Hotfix. Add missing migration.

0.2.4
-----
#. Use search instead of match for regular expressions.
#. A Banner Proxy now has an optional default banner.
#. Consider query string when doing regex matching for Banner Proxies.

0.2.3
-----
#. Add a BannerProxy model that inspects the URL and renders a banner designated to render for that URL.

0.2.2
-----
#. DFP banners draw themselves when loaded via ajax. The code is in the new banner.js.

0.2.1
-----
#. Hotfix release. Add missing files.
#. Display error message in admin interface to notify of missing banner urls.

0.2
---
#. Google DFP banner functionality for web and mobi. This facilitates advertising and tracking using Google's DFP service.
#. `urls.py` created. Be sure to add it to your project urls.
#. Dependency on `django-dfp>=0.1.2`.
#. We now have South migrations.

0.1.3
-----
#. Create list item templates for code banners.

0.1.2
-----
#. Use correct photosize name.

0.1.1
-----
#. Use older `jmbo-foundry` API for image URLs.

0.1
---
#. Add dependency on `jmbo-foundry>=0.7`.

0.0.6
-----
#. Fix incorrect photosizes.json


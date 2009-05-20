==============
Django Cumulus
==============

Django Cumulus provides an interface to Mosso Cloud Files through the Django
admin interface.

Currently, this consists of a custom storage backend and a helper function.

Installation
============

- git clone git://github.com/richleland/django-cumulus.git
- Run "python setup.py install" from within the django-cumulus folder
- In your settings.py:
    CUMULUS_USERNAME = 'YourUsername'
    CUMULUS_API_KEY = 'YourAPIKey'
    CUMULUS_CONTAINER = 'ContainerName'
    DEFAULT_FILE_STORAGE = 'cumulus.storage.CloudFileStorage'
- In your models.py file:
    from cumulus.utils import cumulus_upload_to
    
    class SomeKlass(models.Model):
        some_field = models.ImageField(upload_to=cumulus_upload_to)

You can also check out and modify the example app source for a simple test app.

Planned Features
================

- Clone of Mosso's Cloud Files interface within the Django admin
- Implementation of the Cloud Files pseudo-subdirectories
- Multi-container support, possibly in the form of a custom widget

Requirements
============

#. Mosso's Cloud Files python module http://www.mosso.com/cloudfiles.jsp

==============
Django Cumulus
==============

Django Cumulus provides an interface to Mosso Cloud Files through the Django
admin interface.

Currently, this consists of a custom storage backend and a helper function.

Installation
============

#. git clone git://github.com/richleland/django-cumulus.git

#. Run "python setup.py install" from within the django-cumulus folder

#. Add the following to your project's settings.py file::

    CUMULUS_USERNAME = 'YourUsername'
    CUMULUS_API_KEY = 'YourAPIKey'
    CUMULUS_CONTAINER = 'ContainerName'
    DEFAULT_FILE_STORAGE = 'cumulus.storage.CloudFileStorage'
    
#. Then implement the custom upload_to in your models.py file::

    from cumulus.utils import cumulus_upload_to
    
    class SomeKlass(models.Model):
        some_field = models.ImageField(upload_to=cumulus_upload_to)

Alternatively, if you don't want to set the DEFAULT_FILE_STORAGE, you can do the following in your models::

    from cumulus.storage import CloudFileStorage
    from cumulus.utils import cumulus_upload_to
    
    cloudfiles_storage = CloudFileStorage()
    
    class SomeKlass(models.Model):
        some_field = models.ImageField(storage=cloudfiles_storage,
                                       upload_to=cumulus_upload_to)

Planned Features
================

- Clone of Mosso's Cloud Files interface within the Django admin
- Implementation of the Cloud Files pseudo-subdirectories
- Multi-container support, possibly in the form of a custom widget
- Push metadata with each file

Requirements
============

#. Mosso's Cloud Files python module http://www.mosso.com/cloudfiles.jsp

TODOs and BUGS
==============
See: http://github.com/richleland/django-cumulus/issues


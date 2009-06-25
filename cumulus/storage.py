"""
Custom storage system for Mosso Cloud Files within Django.
"""
import re

from django.conf import settings
from django.core.files import File
from django.core.files.storage import Storage
from django.core.exceptions import ImproperlyConfigured

try:
    import cloudfiles
    from cloudfiles.errors import NoSuchObject
except ImportError:
    raise ImproperlyConfigured, "Could not load cloudfiles dependency. See http://www.mosso.com/cloudfiles.jsp."

try:
    CUMULUS_USERNAME = settings.CUMULUS_USERNAME
    CUMULUS_API_KEY = settings.CUMULUS_API_KEY
    CUMULUS_CONTAINER = settings.CUMULUS_CONTAINER
except AttributeError:
    raise ImproperlyConfigured, "CUMULUS_USERNAME, CUMULUS_API_KEY, and CUMULUS_CONTAINER must be supplied in settings.py."

CUMULUS_TTL = getattr(settings, 'CUMULUS_TTL', 600)


class CloudFileStorage(Storage):
    """
    Custom storage for Mosso Cloud Files.
    """
    def __init__(self):
        """
        Here we set up the connection and select the user-supplied container.
        If the container isn't public (available on Limelight CDN), we make
        it a publicly available container.
        """
        self.connection = cloudfiles.get_connection(CUMULUS_USERNAME,
                                                    CUMULUS_API_KEY)
        self.container = self.connection.get_container(CUMULUS_CONTAINER)
        if not self.container.is_public():
            self.container.make_public()

    def _get_cloud_obj(self, name):
        """
        Helper function to get retrieve the requested Cloud Files Object.
        """
        return self.container.get_object(name)

    def _open(self, name, mode='rb'):
        """
        Not sure if this is the proper way to execute this. Would love input.
        """
        return File(self._get_cloud_obj(name).read())

    def _save(self, name, content):
        """
        Here we're opening the content object and saving it to the Cloud Files
        service. We have to set the content_type so it's delivered properly
        when requested via public URI.
        """
        content.open()
        if hasattr(content, 'chunks'):
            content_str = content.chunks()
        else:
            content_str = content.read()
        cloud_obj = self.container.create_object(name)

        # try to pull a content type off of the File object
        if hasattr(content, 'content_type'):
            cloud_obj.content_type = content.content_type
        # it's possible that it's an ImageFieldFile which won't have a direct
        # 'content_type' attr.  It would live on it's file attr though.
        if hasattr(content, 'file') and hasattr(content.file, 'content_type'):
            cloud_obj.content_type = content.file.content_type
        cloud_obj.send(content_str)
        content.close()
        return name

    def delete(self, name):
        """
        Deletes the specified file from the storage system.
        """
        self.container.delete_object(name)

    def exists(self, name):
        """
        Returns True if a file referened by the given name already exists in the
        storage system, or False if the name is available for a new file.
        """
        try:
            self._get_cloud_obj(name)
            return True
        except NoSuchObject:
            return False

    def listdir(self, path):
        """
        Lists the contents of the specified path, returning a 2-tuple of lists;
        the first item being directories, the second item being files.
        """
        return ([], self.container.list_objects(path=path))

    def size(self, name):
        """
        Returns the total size, in bytes, of the file specified by name.
        """
        return self._get_cloud_obj(name).size()

    def url(self, name):
        """
        Returns an absolute URL where the file's contents can be accessed
        directly by a web browser.
        """
        return self._get_cloud_obj(name).public_uri()

"""
Utilities for use with django-cumulus custom storage app.
"""
from django.utils.text import get_valid_filename

def cumulus_upload_to(self, filename):
    """
    Simple, custom upload_to because Cloud Files doesn't support
    nested containers (directories).
    
    Actually found this out from @minter:
    @richleland The Cloud Files APIs do support pseudo-subdirectories, by 
    creating zero-byte files with type application/directory.
    
    May implement in a future version.
    """
    return get_valid_filename(filename)
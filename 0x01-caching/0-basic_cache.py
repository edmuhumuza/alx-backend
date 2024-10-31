#!/usr/bin/python3
"""0-basic_cache module
"""
from base_caching import BaseCaching
class BasicCache(BaseCaching):
    """ BasicCache defines:
      - how to cache your data
      - how to retrieve cached data
    """
    def __init__(self):
        """ Initialize the cache_data dictionary """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None:
            return
        if key not in self.cache_data.keys():
            return
        else:
            return self.cache_data[key]



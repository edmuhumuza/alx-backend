#!/usr/bin/python3
"""0-basic_cache module
"""

class BasicCache(BaseCaching):
    """ BasicCache defines:
      - how to cache your data
      - how to retrieve cached data
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None:
            return
        if key not in self.cache_data.keys:
            return
        else:
            return self.cache_data[key]



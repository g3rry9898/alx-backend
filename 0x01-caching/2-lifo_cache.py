#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system with a LIFO eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-2]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)


#!/usr/bin/env python3
""" LFUCache module
"""
from collections import defaultdict
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache defines an LFU caching system """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)
        self.recency = defaultdict(int)
        self.time = 0

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key key """
        if key is None or item is None:
            return

        self.time += 1
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.recency[key] = self.time
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
                lru_key = min(lfu_keys, key=lambda k: self.recency[k])
                print("DISCARD:", lru_key)
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.recency[lru_key]

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.recency[key] = self.time

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None
        
        self.frequency[key] += 1
        self.time += 1
        self.recency[key] = self.time
        return self.cache_data[key]


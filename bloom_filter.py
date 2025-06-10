import numpy as np
import mmh3  # We use MurmurHash3 for good, fast hash functions
from math import log, exp

class BloomFilter:
    def __init__(self, size, hash_count):
        """
        Initialize the Bloom Filter.
        
        Parameters:
        - size: Number of bits in the filter
        - hash_count: Number of hash functions to use
        """
        self.size = size
        self.hash_count = hash_count
        # Initialize all bits to 0 (False)
        self.bit_array = np.zeros(size, dtype=bool)
    
    def add(self, item):
        """
        Add an item to the Bloom Filter.
        
        Parameters:
        - item: The element to add (must be string or bytes)
        """
        # For each hash function, calculate the position and set the bit
        for seed in range(self.hash_count):
            # mmh3.hash returns a 32-bit signed integer hash
            index = mmh3.hash(item, seed) % self.size  # Modulo to stay within bounds
            self.bit_array[index] = True
    
    def check(self, item):
        """
        Check if an item is probably in the filter.
        
        Returns:
        - False: Definitely not in the filter
        - True: Probably in the filter (may be a false positive)
        """
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            if not self.bit_array[index]:
                return False  # Definitely not present
        return True  # Probably present
    
    def false_positive_probability(self, inserted_elements):
        """
        Calculate the current false positive probability.
        
        Parameters:
        - inserted_elements: Number of elements added to the filter
        
        Returns:
        - Probability (between 0 and 1) of a false positive
        """
        if inserted_elements == 0:
            return 0.0
        
        # Standard Bloom Filter false positive formula
        return (1 - exp(-self.hash_count * inserted_elements / self.size)) ** self.hash_count

    @staticmethod
    def optimal_hash_count(size, expected_inserts):
        """
        Calculate the optimal number of hash functions.
        
        Parameters:
        - size: Size of the Bloom Filter
        - expected_inserts: Expected number of elements to insert
        
        Returns:
        - Optimal number of hash functions to minimize false positives
        """
        if expected_inserts == 0:
            return 1
        return round((size / expected_inserts) * log(2))

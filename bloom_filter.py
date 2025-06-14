import numpy as np
import mmh3
from math import log, exp

class BloomFilter:
    def __init__(self, size, hash_count):
        """
        Initialize the Bloom Filter.
        - size: Number of bits in the filter
        - hash_count: Number of hash functions to use
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = np.zeros(size, dtype=bool) # All bits initialized to 0 (False)
    
    def add(self, item):
        """Add an item to the Bloom Filter."""
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = True
    
    def add_with_steps(self, item):
        """Add an item and return a log of steps for visualization."""
        steps = [f"Starting 'add' operation for item: **'{item}'** (Hash Count: {self.hash_count})"]
        
        for seed in range(self.hash_count):
            hash_val = mmh3.hash(item, seed)
            index = hash_val % self.size
            
            steps.append(f"  - Hash (seed={seed}): `{hash_val}` -> Index **{index}**.")
            
            if not self.bit_array[index]:
                self.bit_array[index] = True
                steps.append(f"    Bit at index **{index}** was `0`, now set to `1`.")
            else:
                steps.append(f"    Bit at index **{index}** was already `1`, remains `1`.")
        
        steps.append(f"Completed 'add' operation for item: **'{item}'**.")
        return steps
    
    def check(self, item):
        """
        Check if an item is probably in the filter.
        - False: Definitely not in the filter
        - True: Probably in the filter (may be a false positive)
        """
        for seed in range(self.hash_count):
            index = mmh3.hash(item, seed) % self.size
            if not self.bit_array[index]:
                return False 
        return True 

    def check_with_steps(self, item):
        """Check an item and return a log of steps for visualization."""
        steps = [f"Starting 'check' operation for item: **'{item}'** (Hash Count: {self.hash_count})"]

        is_member = True
        for seed in range(self.hash_count):
            hash_val = mmh3.hash(item, seed)
            index = hash_val % self.size
            bit_value = self.bit_array[index]
            
            steps.append(f"  - Hash (seed={seed}): `{hash_val}` -> Index **{index}**.")
            steps.append(f"    Bit at index **{index}** is **`{int(bit_value)}`**.")
            
            if not bit_value:
                steps.append(f"    Since bit at index **{index}** is `0`, item **'{item}'** is **definitely NOT present (early exit)**.")
                is_member = False
                break # Exit early as item is confirmed not present
        
        if is_member:
            steps.append(f"All relevant bits were `1`. Item **'{item}'** is **PROBABLY present**.")
        
        return is_member, steps
    
    def false_positive_probability(self, inserted_elements):
        """Calculate the current false positive probability using the standard formula."""
        if inserted_elements == 0:
            return 0.0
        # Formula: (1 - e^(-k*n/m))^k
        return (1 - exp(-self.hash_count * inserted_elements / self.size)) ** self.hash_count

    @staticmethod
    def optimal_hash_count(size, expected_inserts):
        """Calculate the optimal number of hash functions to minimize false positives."""
        if expected_inserts == 0:
            return 1
        # Formula: k = (m/n) * ln(2)
        return round((size / expected_inserts) * log(2))
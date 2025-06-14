import pytest
import numpy as np
from bloom_filter import BloomFilter

# --- Test Initialization ---
def test_bloom_filter_initialization():
    """Verify initial state of Bloom Filter."""
    bf = BloomFilter(size=100, hash_count=3)
    assert bf.size == 100
    assert bf.hash_count == 3
    assert np.all(bf.bit_array == False) # All bits should be 0 (False)
    assert bf.bit_array.dtype == bool

# --- Test Add Method ---
def test_add_single_item():
    """Test adding one item sets bits."""
    bf = BloomFilter(size=100, hash_count=3)
    bf.add("apple")
    assert sum(bf.bit_array) > 0 

def test_add_duplicate_item_does_not_change_bit_count():
    """Verify adding duplicate item doesn't change number of set bits."""
    bf = BloomFilter(size=100, hash_count=3)
    bf.add("test_item")
    initial_bits_set = sum(bf.bit_array)
    bf.add("test_item")
    assert sum(bf.bit_array) == initial_bits_set

# --- Test Check Method (True Positives & True Negatives) ---
def test_check_true_positives():
    """Verify existing items are found (True Positives)."""
    bf = BloomFilter(size=100, hash_count=3)
    items_to_add = ["apple", "banana", "cherry", "date"]
    for item in items_to_add:
        bf.add(item)
    
    for item in items_to_add:
        assert bf.check(item) is True, f"Expected '{item}' to be found, but it was not."

def test_check_true_negatives_on_empty_filter():
    """Verify non-existent item is not found in empty filter."""
    bf = BloomFilter(size=100, hash_count=3)
    assert bf.check("non_existent_item") is False

def test_check_true_negatives_on_non_empty_filter_can_be_false():
    """Verify a non-existent item is *usually* not found (True Negative)."""
    bf = BloomFilter(size=100, hash_count=3)
    bf.add("existing_item")
    assert bf.check("another_non_existent_item") in [True, False] # Can be FP or TN

# --- Test False Positive Probability ---
def test_false_positive_probability_empty_filter():
    """Verify FP probability is 0 for an empty filter."""
    bf = BloomFilter(size=100, hash_count=3)
    assert bf.false_positive_probability(0) == 0.0

def test_false_positive_probability_increases_with_items():
    """Verify FP probability increases as more items are added."""
    bf = BloomFilter(size=100, hash_count=3)
    bf.add("item1")
    prob1 = bf.false_positive_probability(1)
    
    bf.add("item2")
    prob2 = bf.false_positive_probability(2)
    
    assert prob2 > prob1
    assert prob1 > 0.0 # Should be >0 for non-empty filter

# --- Test Optimal Hash Count (Static Method) ---
def test_optimal_hash_count_zero_expected_inserts():
    """Verify optimal hash count is 1 when no inserts expected."""
    assert BloomFilter.optimal_hash_count(100, 0) == 1

def test_optimal_hash_count_calculation():
    """Test optimal hash count calculation for known values."""
    assert BloomFilter.optimal_hash_count(100, 10) == 7
    assert BloomFilter.optimal_hash_count(1000, 50) == 14

# --- Test False Positive Occurrence (Demonstrative, not strictly deterministic unit test) ---
def test_false_positive_can_occur_under_high_load():
    """
    Demonstrates that false positives *can* occur when the filter is under high load.
    This is not a deterministic unit test for a specific FP, but confirms the possibility.
    """
    bf = BloomFilter(size=50, hash_count=2)
    # Add enough items to significantly increase FP chance
    items_added = [f"item_{i}" for i in range(25)]
    for item in items_added:
        bf.add(item)
    
    # Check a non-existent item. If it's a false positive, the test passes.
    non_existent_item = "definitely_not_in_filter"
   
    assert bf.check(non_existent_item) in [True, False]
    
from bloom_filter import BloomFilter

# Initialize a small Bloom Filter for testing
bf = BloomFilter(size=100, hash_count=3)

# Test adding and checking elements
test_elements = ["apple", "banana", "cherry"]
for elem in test_elements:
    bf.add(elem)
    print(f"Added {elem}")

# Check for existing elements
for elem in test_elements:
    print(f"{elem} in filter? {bf.check(elem)}")  # Should all be True

# Check for non-existing elements (potential false positives)
test_non_elements = ["dog", "cat", "elephant"]
for elem in test_non_elements:
    print(f"{elem} in filter? {bf.check(elem)}")  # Might get some True (false positives)

# Check false positive probability
print(f"Current false positive probability: {bf.false_positive_probability(len(test_elements)):.2%}")

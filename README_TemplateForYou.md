# Bloom Filter - Interactive Visualization

## Project Overview

This project is an interactive web application that implements and visualizes the Bloom Filter, developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

The Bloom Filter is a memory-efficient data structure for quickly checking if an item might be in a set. When an item is added, its value is hashed k times to set k specific bits in a large bit array to 1. To check for an item, the same k bits are inspected; if all are 1, the item is probably in the set (with a chance of false positives), but if any bit is 0, it is definitely not present.

### Problem Definition

The Bloom Filter solves the problem of efficiently checking for the probable membership of an element in a set. It's a probabilistic data structure that can tell you with certainty if an element is not in a set, or if it might be in the set (with a chance of false positives). It's highly space-efficient, making it suitable for scenarios where memory is a constraint and a small rate of false positives is acceptable, such as spell checkers, caching mechanisms, or distributed databases.

### Mathematical Background

A Bloom Filter uses a bit array of m bits, all initially set to 0. To add or check an element, k independent hash functions are used. Each hash function maps an element to an index within the bit array.

1) Optimal Number of Hash Functions (k): For a given bit array size (m) and expected number of inserted items (n), the optimal number of hash functions to minimize false positive probability is given by:
k=
fracmn
cdot
ln(2)

2) False Positive Probability (P_f): The probability of a false positive (an item being reported as present when it's not) for a Bloom Filter with m bits, k hash functions, and n inserted items is approximately:
P_f
approx
left(1−e^ 
frac−kcdotnm
right)^k

### Algorithm Steps

Add Operation
- Step 1: Hash Generation - For the item to be added, k different hash functions are applied.
- Step 2: Index Mapping - Each of the k hash values is mapped to a specific index within the Bloom Filter's bit array (ranging from 0 to m-1).
- Step 3: Bit Setting - The bits at all k calculated indices in the bit array are set to 1. If a bit is already 1, it remains 1.

Check Operation
- Step 1: Hash Generation - For the item to be checked, the same k hash functions are applied to generate k indices, identical to how it's done during the add operation.
- Step 2: Bit Inspection - The bits at each of these k calculated indices in the bit array are examined.
- Step 3: Decision - Definitively Not Present - If even one of the bits at these k indices is found to be 0, the item is definitely not in the filter. The check stops here.
- Step 4: Decision - Probably Present - If all k bits at these indices are found to be 1, the item is probably in the filter. It's important to note this could be a false positive.

### Pseudocode

```
// BloomFilter Class Initialization
function BloomFilter(m, k):
    bit_array = array of m booleans, all initialized to FALSE
    size = m
    hash_count = k

// Add an item to the filter
function add(item):
    for seed from 0 to hash_count - 1:
        index = hash(item, seed) modulo size
        bit_array[index] = TRUE

// Check if an item is in the filter
function check(item):
    for seed from 0 to hash_count - 1:
        index = hash(item, seed) modulo size
        if bit_array[index] is FALSE:
            return FALSE // Definitely not in the set
    return TRUE // Probably in the set
```

## Complexity Analysis

m: size of the bit array
k: number of hash functions
n: number of items inserted

### Time Complexity

Initialization (__init__):
 O(m) - Involves setting up a bit array of size m.

Add (add, add_with_steps):
 O(k) - Always performs k hash computations and sets k bits.

Check (check, check_with_steps):
 Best Case: O(1) - If the first bit checked is 0, the item is definitively not present, leading to an immediate return.
 Average Case: O(k) - Typically requires checking a majority or all of the k bits.
 Worst Case: O(k) - All k hash computations and bit checks are performed (e.g., item present or false positive).

False Positive Probability (false_positive_probability):
 O(1) - Involves a fixed number of mathematical operations.

Optimal Hash Count (optimal_hash_count):
 O(1) - Involves a fixed number of mathematical operations.

### Space Complexity

- O(m) - The primary memory consumption is the bit array of size m.

## Features

Interactive Controls: Users can dynamically adjust the bit array size (m) and the number of hash functions (k).

Element Operations: Functionality to add new elements and check the membership of existing or new elements.

Step-by-Step Explanation: A unique walkthrough feature that visualizes each hash calculation and bit manipulation step during add and check operations, making the algorithm's internal workings transparent.

Live Metrics: Displays real-time updates on the Bloom Filter's performance, including:
 Current False Positive Probability
 Number of Bits Set in the array
 Load Factor (ratio of inserted items to bit array size)

Bit Array Visualization: A clear graphical representation of the Bloom Filter's bit array, showing which bits are set to 0 or 1.

Python Implementation: Core algorithm implemented in Python using numpy for efficient bit array management and mmh3 for hashing.

Comprehensive Unit Tests: Automated test suite verifying the correctness of the Bloom Filter's core functionalities and edge cases.

## Screenshots

file:///Users/aylin/Desktop/the-main-interface.png

*Main Interface*  
- *Top*: Configure filter size (m) and hash functions (k)  
- *Middle*: Add elements or check membership  
- *Bottom*: Empty bit array visualization (all bits unset)  
- *Metrics panel*: Shows initial state (0% FP rate, 0/100 bits used)

file:///Users/aylin/Desktop/the-main-interface2.png

*Configuration Panel & Metrics*  
- *Sliders*: Adjust bit array size (10-1000) and hash functions (1-10)  
- *Live metrics*: Tracks false positive probability, bits set, and load factor  
- *Clean state*: No elements added (0.00% FP rate, all bits unset)  

file:///Users/aylin/Desktop/the-algorithm-in-action.png

*True Positive Verification*  
- Added elements: "apple", "banana"  
- Checking "apple" → ✅ Present (True Positive)  
- Bit array shows set bits from hash collisions  
- Current metrics: 40/100 bits set (Load Factor: 0.18)

file:///Users/aylin/Desktop/the-algorithm-in-action%202.png
 
- Configuration: 100-bit array, 3 hash functions  
- 7.26% FP probability with current load (40 bits set)  
- Visualized bit array density demonstrates collision risk  
- Ready for false positive test by checking non-added elements  


## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Adjust Configuration: Use the sliders in the sidebar to set the "Bit Array Size (m)" and "Hash Functions (k)". Changes will reset the Bloom Filter.
2. Add Elements: Type a string into the "Enter element to add" box and click "Add Element to Filter". Observe the bit array update.
3. View Add Steps: After adding an element, click the "Show 'Add' Operation Steps" expander to see the detailed hash calculations and bit-setting process.
4. Check Membership: Type a string into the "Enter element to check" box and click "Check Element in Filter".
5. Interpret Check Results: The app will indicate if the item is "Present (True Positive)", "False Positive!", or "Definitely not present".
6. View Check Steps: After checking an element, click the "Show 'Check' Operation Steps" expander to trace how the decision was made.
7. Monitor Metrics: Observe the "False Positive Probability," "Bits Set," and "Load Factor" metrics update dynamically below the visualization.

### Example Inputs

- Example 1: True Positive

Action: Add "apple". Then, check "apple".
Expected Output: "✅ Present (True Positive)" and the bit array will show the bits for "apple" set.

- Example 2: True Negative

Action: Add "apple". Then, check "orange".
Expected Output: "❌ Definitely not present" (unless by chance "orange" triggers a false positive, which is rare for a large filter).

- Example 3: Demonstrating False Positive

Action:
1. Set "Bit Array Size (m)" to a small value (e.g., 50).
2. Set "Hash Functions (k)" to 2 or 3.
3. Add several diverse elements (e.g., "cat", "dog", "bird", "fish", "tree", "house", "car", "bike").
4. Check a word you did not add (e.g., "cup").

Expected Output: There is a higher probability you might see "⚠️ False Positive!" demonstrating this inherent characteristic of Bloom Filters.

## Implementation Details

### Key Components

- bloom_filter.py: Contains the core BloomFilter class implementation, including the add, check, false_positive_probability, and optimal_hash_count methods. It also houses the logic for generating step-by-step explanations.
- app.py: The main Streamlit application file responsible for the interactive user interface, displaying visualizations, metrics, and orchestrating user interactions with the Bloom Filter.
- utils.py: Contains helper functions, specifically plot_bloom_filter for generating the bit array visualization and calculate_metrics for computing and formatting performance statistics.
- test_algorithm.py: Contains comprehensive unit tests for the BloomFilter implementation.

### Code Highlights

```
# From bloom_filter.py - Core add operation with step logging
def add_with_steps(self, item):
    """Add an item to the Bloom Filter and return a log of steps."""
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

# From app.py - Displaying step-by-step explanation
# ... inside the check membership section ...
if st.button("Check Element in Filter", key="check_button"):
    if check_element_to_check:
        is_member, steps_log_check = st.session_state.bf.check_with_steps(check_element_to_check)
        st.session_state.check_steps_log = steps_log_check
        # ... logic for displaying success/error ...
        
        with st.expander(f"Show 'Check' Operation Steps for last item"):
            for step_info in st.session_state.check_steps_log:
                st.markdown(step_info)
```

## Testing

This project includes a test suite to verify the correctness of the algorithm implementation:

```bash
python -m unittest test_algorithm.py
```

### Test Cases

- Initialization: Correct setup of the Bloom Filter's size, hash count, and initial empty bit array.
- Add Operations: Verifying that adding items correctly sets bits, including handling duplicate additions.
- Check Operations (True Positives): Ensuring that items known to be added are correctly identified as "probably present".
- Check Operations (True Negatives): Verifying that items not added are correctly identified as "definitely not present", including checks on an empty filter.
- False Positive Probability: Testing the accuracy and behavior of the false_positive_probability calculation.
- Optimal Hash Count: Verifying the static method for calculating the optimal number of hash functions.
- Edge Cases: Testing scenarios that might lead to specific behaviors, such as the possibility of false positives under high load.

## Live Demo

A live demo of this application is available at: [Insert Streamlit Cloud URL here]

## Limitations and Future Improvements

### Current Limitations

- Fixed Hash Functions: Currently uses MurmurHash3, but doesn't allow user selection of other hash algorithms.
- No Deletion: Bloom Filters fundamentally do not support element deletion without re-creating the entire filter, which is a known limitation of the algorithm.
- Simple Visualization: The bit array visualization is basic; it could be enhanced with animations or more interactive elements.
- String-Only Elements: The current implementation primarily handles string inputs; extending it to other data types would require careful handling of hashing.

### Planned Improvements

- Advanced Visualization: Incorporate animations for bit-setting and checking, or allow highlighting specific bit changes.
- Comparison Mode: Enable comparison between different Bloom Filter configurations or against other data structures.
- Performance Benchmarking: Add features to test insertion/check speed with large datasets.
- Predictive Analytics: Show how changing m or k would ideally affect the false positive rate based on the expected number of insertions.
- Error Handling: More robust error handling for invalid user inputs (e.g., empty strings).

## References and Resources

### Academic References

1. Bloom, B. H. (1970). Space/time trade-offs in hash coding with allowable errors. Communications of the ACM, 13(7), 422-426.

### Online Resources

- Wikipedia - Bloom Filter: https://en.wikipedia.org/wiki/Bloom_filter
- Stack Overflow: Various discussions on Bloom Filter implementations and properties.
- Real Python: Tutorials on data structures in Python (general reference).

## Author

- **Name:** AYLIN POURMOHAMMAD SAATLOU
- **Student ID:** 240543604
- **GitHub:** AYLIN-P-SAATLOU

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project.

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*

# Bloom Filter - Interactive Visualization

## Project Overview

This project is an interactive web application that implements and visualizes the Bloom Filter, developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

[Provide a comprehensive explanation of your algorithm here. Include the following elements:]

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

1. [Step 1 with explanation]
2. [Step 2 with explanation]
3. [Step 3 with explanation]
...

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

![Main Interface](docs/screenshots/main_interface.png)
*Caption describing the main interface*

![Algorithm in Action](docs/screenshots/algorithm_demo.png)
*Caption describing the algorithm in action*

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

- [Test case 1 description]
- [Test case 2 description]
- [Test case 3 description]

## Live Demo

A live demo of this application is available at: [Insert Streamlit Cloud URL here]

## Limitations and Future Improvements

### Current Limitations

- [Limitation 1]
- [Limitation 2]
- [Limitation 3]

### Planned Improvements

- [Improvement 1]
- [Improvement 2]
- [Improvement 3]

## References and Resources

### Academic References

1. [Reference 1]
2. [Reference 2]
3. [Reference 3]

### Online Resources

- [Resource 1]
- [Resource 2]
- [Resource 3]

## Author

- **Name:** [Your Name]
- **Student ID:** [Your Student ID]
- **GitHub:** [Your GitHub Username]

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project, and [any other acknowledgements].

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*

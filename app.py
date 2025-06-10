import streamlit as st
from bloom_filter import BloomFilter
from utils import plot_bloom_filter, calculate_metrics

# App Configuration
st.set_page_config(page_title="Bloom Filter Visualizer", layout="wide")

def main():
    st.title("🎯 Bloom Filter Interactive Visualizer")
    
    # Sidebar Controls
    st.sidebar.header("Configuration")
    size = st.sidebar.slider("Bit Array Size", 10, 1000, 100, help="Larger sizes reduce false positives")
    hash_count = st.sidebar.slider("Hash Functions", 1, 10, 3, help="More hashes improve accuracy but increase FPs")
    
    # Initialize Bloom Filter
    if 'bf' not in st.session_state:
        st.session_state.bf = BloomFilter(size, hash_count)
        st.session_state.inserted_items = set()
    
    # Main Interface Columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add Elements")
        new_element = st.text_input("Enter element to add")
        if st.button("Add") and new_element:
            st.session_state.bf.add(new_element)
            st.session_state.inserted_items.add(new_element)
            st.success(f"Added: '{new_element}'")
    
    with col2:
        st.subheader("Check Membership")
        check_element = st.text_input("Enter element to check")
        if st.button("Check"):
            if check_element:
                is_member = st.session_state.bf.check(check_element)
                actual_member = check_element in st.session_state.inserted_items
                
                if is_member:
                    if actual_member:
                        st.success("✅ Present (True Positive)")
                    else:
                        st.error("⚠️ False Positive!")
                else:
                    st.info("❌ Definitely not present")

    # Visualization
    st.subheader("Bit Array Visualization")
    st.pyplot(plot_bloom_filter(st.session_state.bf.bit_array))
    
    # Metrics Display
    metrics = calculate_metrics(st.session_state.bf, st.session_state.inserted_items)
    st.metric("False Positive Probability", metrics["false_positive_rate"])
    st.metric("Bits Set", metrics["bits_used"])
    st.metric("Load Factor", metrics["load_factor"])

if __name__ == "__main__":
    main()

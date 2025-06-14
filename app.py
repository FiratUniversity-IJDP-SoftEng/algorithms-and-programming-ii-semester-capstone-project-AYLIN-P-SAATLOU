import streamlit as st
from bloom_filter import BloomFilter
from utils import plot_bloom_filter, calculate_metrics

st.set_page_config(page_title="Bloom Filter Visualizer", layout="wide")

def main():
    st.title("🎯 Bloom Filter Interactive Visualizer")
    
    st.sidebar.header("Configuration")
    size = st.sidebar.slider("Bit Array Size (m)", 10, 1000, 100, help="Larger sizes reduce false positives, increase memory")
    hash_count = st.sidebar.slider("Hash Functions (k)", 1, 10, 3, help="More hashes improve accuracy for small N, but increase FPs for large N")
    
    if 'bf' not in st.session_state or \
       st.session_state.bf.size != size or \
       st.session_state.bf.hash_count != hash_count:
        st.session_state.bf = BloomFilter(size, hash_count)
        st.session_state.inserted_items = set()
        st.session_state.add_steps_log = [] # Store steps for 'add' operation
        st.session_state.check_steps_log = [] # Store steps for 'check' operation
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add Elements")
        new_element_to_add = st.text_input("Enter element to add", key="add_element_input")
        if st.button("Add Element to Filter", key="add_button") and new_element_to_add:
            # Add item and get step-by-step log
            steps_log_add = st.session_state.bf.add_with_steps(new_element_to_add)
            st.session_state.inserted_items.add(new_element_to_add)
            st.session_state.add_steps_log = steps_log_add 
            st.success(f"Added: '{new_element_to_add}'")
            st.session_state.check_steps_log = [] # Clear check steps on add
            
        # Display 'Add' operation steps in an expander
        if st.session_state.add_steps_log:
            with st.expander(f"Show 'Add' Operation Steps for last item"):
                for step_info in st.session_state.add_steps_log:
                    st.markdown(step_info)

    with col2:
        st.subheader("Check Membership")
        check_element_to_check = st.text_input("Enter element to check", key="check_element_input")
        if st.button("Check Element in Filter", key="check_button"):
            if check_element_to_check:
                # Check item and get step-by-step log
                is_member, steps_log_check = st.session_state.bf.check_with_steps(check_element_to_check)
                st.session_state.check_steps_log = steps_log_check
                st.session_state.add_steps_log = [] # Clear add steps on check

                actual_member = check_element_to_check in st.session_state.inserted_items
                
                if is_member:
                    if actual_member:
                        st.success("✅ Present (True Positive)")
                    else:
                        st.error("⚠️ False Positive!")
                else:
                    st.info("❌ Definitely not present")
            
            # Display 'Check' operation steps in an expander
            if st.session_state.check_steps_log:
                with st.expander(f"Show 'Check' Operation Steps for last item"):
                    for step_info in st.session_state.check_steps_log:
                        st.markdown(step_info)

    st.markdown("---") # Visual separator

    st.subheader("Bloom Filter Bit Array (1 = set, 0 = unset)")
    st.pyplot(plot_bloom_filter(st.session_state.bf.bit_array))
    
    st.subheader("Current Metrics")
    metrics = calculate_metrics(st.session_state.bf, st.session_state.inserted_items)
    col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
    with col_metrics1:
        st.metric("False Positive Probability", metrics["false_positive_rate"])
    with col_metrics2:
        st.metric("Bits Set", metrics["bits_used"])
    with col_metrics3:
        st.metric("Load Factor (n/m)", metrics["load_factor"])

if __name__ == "__main__":
    main()

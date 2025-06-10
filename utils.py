import matplotlib.pyplot as plt
import numpy as np

def plot_bloom_filter(bit_array):
    """Visualize the Bloom Filter's bit array"""
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.imshow([bit_array], cmap='Blues', aspect='auto')
    ax.set_yticks([])
    ax.set_title("Bloom Filter Bit Array (1 = set, 0 = unset)")
    return fig

def calculate_metrics(bf, inserted_items):
    """Compute performance metrics"""
    fp_prob = bf.false_positive_probability(len(inserted_items))
    return {
        "false_positive_rate": f"{fp_prob:.2%}",
        "bits_used": f"{sum(bf.bit_array)}/{len(bf.bit_array)}",
        "load_factor": f"{len(inserted_items)/len(bf.bit_array):.2f}"
    }

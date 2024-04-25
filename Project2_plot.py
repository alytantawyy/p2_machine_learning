import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate statistics
def calculate_statistics(data):
    data = np.array(data, dtype=float)
    mean = np.mean(data)
    variance = np.var(data)
    minimum = np.min(data)
    maximum = np.max(data)
    return [mean, variance, minimum, maximum]

# Function to read data and compute features
def process_data(file_path, data_type):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        features = [[] for _ in range(4)]  # List to store features for each type
        for row in reader:
            if data_type == 'all' or data_type.lower() in row[1].strip().lower():
                data = list(map(float, row[3:]))
                for i, val in enumerate(calculate_statistics(data)):
                    features[i].append(val)
        return features

# Function to create box plot
def create_box_plot(features, feature_names):
    plt.figure(figsize=(10, 6))
    plt.boxplot(features, labels=feature_names)
    plt.title('Box Plot of Hand-crafted Features')
    plt.xlabel('Feature Type')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

# Main block
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Project2.py <data_type> <data_file>")
        sys.exit(1)
    
    data_type = sys.argv[1]
    data_file = sys.argv[2]
    features = process_data(data_file, data_type)
    feature_names = ['Mean', 'Variance', 'Minimum', 'Maximum']
    create_box_plot(features, feature_names)

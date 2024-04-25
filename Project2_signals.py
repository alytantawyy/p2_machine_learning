import csv
import random
import matplotlib.pyplot as plt

# Define colors for each physiological signal
colors = {
    'BP Dia_mmHg': 'blue',    # Diastolic BP
    'EDA_microsiemens': 'red',     # EDA
    'LA Systolic BP_mmHg': 'green',   # Systolic BP
    'Respiration Rate_BPM': 'orange'   # Respiration
}

# Initialize lists to store physiological data
physiological_data = {data_type: [] for data_type in colors.keys()}

# Read data from CSV file
with open('Project2Data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        data_type = row[1]  # Data type
        if data_type in colors:
            # Convert data to float and store in the corresponding list
            physiological_data[data_type].append([float(val) for val in row[3:]])

# Select a random instance for each data type
random_instances = {data_type: random.choice(physiological_data[data_type]) for data_type in colors.keys()}

# Plot the data
plt.figure(figsize=(10, 6))
for data_type, data in random_instances.items():
    plt.plot(data, label=data_type, color=colors[data_type])

# Add labels and legend
plt.xlabel('Time')
plt.ylabel('Physiological Signal')
plt.title('Physiological Signals Comparison')
plt.legend()

# Show the plot
plt.show()

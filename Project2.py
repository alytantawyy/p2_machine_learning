import sys
import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

def calculate_statistics(data):
    data = np.array(data, dtype=float)  # Ensuring data is in numpy array format for accurate computation
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
        features, labels = [], []
        for row in reader:
            if data_type == 'all' or data_type.lower() in row[1].strip().lower():
                data = list(map(float, row[3:]))
                features.append(calculate_statistics(data))
                labels.append(row[2])
        return features, labels

# Function to perform cross-validation and return results
def evaluate_model(features, labels):
    kf = KFold(n_splits=10)
    accuracies, precisions, recalls, conf_matrices = [], [], [], []

    for train_index, test_index in kf.split(features):
        X_train, X_test = [features[i] for i in train_index], [features[i] for i in test_index]
        y_train, y_test = [labels[i] for i in train_index], [labels[i] for i in test_index]

        classifier = RandomForestClassifier()
        classifier.fit(X_train, y_train)
        predictions = classifier.predict(X_test)

        accuracies.append(accuracy_score(y_test, predictions))
        precisions.append(precision_score(y_test, predictions, pos_label='Pain', zero_division=0))
        recalls.append(recall_score(y_test, predictions, pos_label='Pain', zero_division=0))
        conf_matrices.append(confusion_matrix(y_test, predictions))

    avg_accuracy = np.mean(accuracies)
    avg_precision = np.mean(precisions)
    avg_recall = np.mean(recalls)
    avg_conf_matrix = np.mean(conf_matrices, axis=0)
    return avg_accuracy, avg_precision, avg_recall, avg_conf_matrix

# Function to output results
# Function to output results
def output_results(avg_accuracy, avg_precision, avg_recall, avg_conf_matrix):
    with open('output.txt', 'a') as f:  # Changed from 'w' to 'a' to append instead of overwrite
        f.write(f"Data Type: {sys.argv[1]}\n")  # Adding data type to clarify results
        f.write(f"Average Accuracy: {avg_accuracy:.2%}\n")
        f.write(f"Average Precision: {avg_precision:.2%}\n")
        f.write(f"Average Recall: {avg_recall:.2%}\n")
        f.write("Average Confusion Matrix:\n")
        f.write(np.array2string(avg_conf_matrix))
        f.write("\n\n")  # Add spacing for readability between entries


# Main block to execute the functions
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Project2.py <data_type> <data_file>")
        sys.exit(1)
    
    data_type = sys.argv[1]
    data_file = sys.argv[2]
    features, labels = process_data(data_file, data_type)
    avg_accuracy, avg_precision, avg_recall, avg_conf_matrix = evaluate_model(features, labels)
    output_results(avg_accuracy, avg_precision, avg_recall, avg_conf_matrix)

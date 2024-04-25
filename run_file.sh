#!/bin/bash

# Path to the dataset
DATA_FILE="Project2Data.csv"

# Define data types to process
DATA_TYPES=("dia" "sys" "eda" "res" "all")

# Output file path
OUTPUT_FILE="output.txt"

# Clear the output file before starting
> $OUTPUT_FILE  # This command empties the file before starting the loop

# Write the explanation of metrics to the output file once before processing data types
echo "Output Results Explanation:" >> $OUTPUT_FILE
echo " - Average Accuracy: Percentage of correctly predicted instances." >> $OUTPUT_FILE
echo " - Average Precision: Ratio of correctly predicted positive observations to the total predicted positives." >> $OUTPUT_FILE
echo " - Average Recall: Ratio of correctly predicted positive observations to all observations in actual class." >> $OUTPUT_FILE
echo " - Average Confusion Matrix: Shows the number of true positive, false positive, true negative, and false negative predictions." >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

# Loop through each data type and process it
for DATA_TYPE in "${DATA_TYPES[@]}"
do
    # Add a header for the data type being processed
    echo "Processing $DATA_TYPE..." >> $OUTPUT_FILE
    # Run the Python script and append the results to the output file
    python Project2.py $DATA_TYPE $DATA_FILE >> $OUTPUT_FILE
    echo "" >> $OUTPUT_FILE  # Add extra spacing for readability
done

echo "All data types have been processed. Results are in $OUTPUT_FILE."

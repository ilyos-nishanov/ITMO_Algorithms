import csv
import argparse
import os


def convert_txt_to_csv(input_file):
    # Generate the output CSV file path in the current working directory
    output_file = os.path.splitext(os.path.basename(input_file))[0] + '.csv'

    # Open the text file in read mode
    with open(input_file, 'r') as file:
        # Read the lines from the text file
        lines = file.readlines()

    # Open the CSV file in write mode
    with open(output_file, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write each line as a row in the CSV file
        for line in lines:
            # Remove newline characters and split the line into fields
            fields = line.strip().split()

            # Write the fields as a row in the CSV file
            writer.writerow(fields)

    print(f"Conversion complete. Text file '{input_file}' has been converted to CSV file '{output_file}'.")


if __name__ == '__main__':
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Convert a text file to CSV format.')

    # Add the input file argument
    parser.add_argument('input_file', type=str, help='Path to the input text file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert the text file to CSV
    convert_txt_to_csv(args.input_file)
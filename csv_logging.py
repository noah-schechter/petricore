import csv

# Open CSV file for writing header
def init_csv(csv_name):
    with open(csv_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Timestamp', 'Power', 'Fan', 'Temperature', 'Raw Temp Timestamp', 'First Crack', 'Second Crack'])


# Save a row to a CSV file
def write(data, csv_name):
    with open(csv_name, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([data['Timestamp'], data['Power'], data['Fan'], data['Temperature'], data['Raw Temp Timestamp'], data['First Crack'], data['Second Crack']])
    
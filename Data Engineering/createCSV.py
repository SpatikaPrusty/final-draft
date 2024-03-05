import csv

# Data to be written into the CSV file Policy ID, Policy Holder, Policy Type, Total Open Claims, Total Closed Claims
data = [
    ['Policy_ID', 'Policy_holder', 'Total_open_claims', 'Total_closed_claims'],
    ['10011', 'Spatika', 3, 4],
    ['10012', 'Lucky', 6, 2],
    ['10013', 'Nipun', 7, 5],
    ['10014', 'Akansha', 5, 2],
    ['10015', 'Kyla', 7, 4],
]

# File path for the CSV file
csv_file_path = 'C:/Users/spati/OneDrive/Desktop/FINAL DRAFT/Data Engineering/datasheet.csv'

# C:\Users\spati\Downloads\csv

# Writing data to the CSV file
with open(csv_file_path, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data has been appended to", csv_file_path)

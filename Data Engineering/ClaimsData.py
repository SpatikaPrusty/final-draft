import csv

# Claims data
claims_data = [
    ['claim_id', 'user_id', 'policy_id', 'Reason', 'ClaimAmount', 'ClaimStatus', 'filed_at', 'last_updated'],
    [1, 1, 1, {'type': 'Accident', 'description': 'Rear-ended at traffic light'}, 2000, 'Filed', '07:22.2', '07:22.2'],
    [2, 2, 2, {'type': 'Property Damage', 'description': 'Tree fell on house roof'}, 5000, 'Under Review', '07:22.2', '07:22.2'],
    [4, 4, 4, {'type': 'Life', 'description': 'Beneficiary claim'}, 100000, 'Filed', '07:22.2', '07:22.2'],
    [5, 5, 5, {'type': 'Travel', 'description': 'Trip cancellation due to illness'}, 700, 'Denied', '07:22.2', '07:22.2'],
    [6, 6, 6, {'type': 'Accident', 'description': 'Fender bender in parking lot'}, 1500, 'Filed', '15:30.1', '15:30.1'],
    [7, 7, 7, {'type': 'Property Damage', 'description': 'Broken window due to hailstorm'}, 2500, 'Under Review', '20:45.7', '20:45.7'],
    [8, 8, 8, {'type': 'Life', 'description': "Spouse's death"}, 50000, 'Filed', '30:01.0', '30:01.0'],
    [9, 9, 9, {'type': 'Accident', 'description': 'Car accident'}, 3000, 'Filed', '31:15.3', '31:15.3'],
    [10, 10, 10, {'type': 'Property Damage', 'description': 'Water damage'}, 4000, 'Under Review', '32:22.5', '32:22.5'],
    [11, 11, 11, {'type': 'Life', 'description': 'Parent death'}, 60000, 'Filed', '33:30.2', '33:30.2'],
    [12, 12, 12, {'type': 'Travel', 'description': 'Flight cancellation'}, 800, 'Denied', '34:40.4', '34:40.4'],
    [13, 13, 13, {'type': 'Accident', 'description': 'Parking lot collision'}, 2500, 'Filed', '35:50.6', '35:50.6'],
    [14, 14, 14, {'type': 'Property Damage', 'description': 'Vandalism'}, 3500, 'Under Review', '36:55.8', '36:55.8'],
    [15, 15, 15, {'type': 'Life', 'description': 'Siblings death'}, 70000, 'Filed', '38:10.0', '38:10.0'],
    [16, 16, 16, {'type': 'Travel', 'description': 'Lost luggage'}, 1200, 'Denied', '40:20.2', '40:20.2'],
    [17, 17, 17, {'type': 'Accident', 'description': 'Hit by uninsured driver'}, 3200, 'Filed', '42:25.4', '42:25.4'],
    [18, 18, 18, {'type': 'Property Damage', 'description': 'Roof damage'}, 4500, 'Under Review', '44:30.6', '44:30.6'],
    [19, 19, 19, {'type': 'Life', 'description': "Child's illness"}, 80000, 'Filed', '46:40.8', '46:40.8'],
    [20, 20, 20, {'type': 'Travel', 'description': 'Delayed flight'}, 1500, 'Denied', '48:50.0', '48:50.0'],
]
# File path for the new CSV file
csv_file_path = 'C:/Users/spati/OneDrive/Desktop/FINAL DRAFT/Data Engineering/claims_data.csv'

# Writing data to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(claims_data)

print("Claims data has been written to", csv_file_path)

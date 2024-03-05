import csv
from cryptography.fernet import Fernet

#Define the encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    # Encrypt the data using Fernet encryption
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data.decode()

def mask_data(data):
    # Mask sensitive data by replacing characters with placeholders
    return 'XXXX'  # Replace with your masking strategy

def update_claim_status(policy_id, claim_status):
    # Read the dataset
    with open('C:/Users/spati/OneDrive/Desktop/FINAL DRAFT/Data Engineering/datasheet.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Update the dataset with new claim status
    for row in rows:
        if row['Policy_ID'] == policy_id:
            if claim_status == 'open':
                row['Total_open_claims'] = str(int(row['Total_open_claims']) + 1)
            elif claim_status == 'closed':
                row['Total_closed_claims'] = str(int(row['Total_closed_claims']) + 1)
                row['Total_open_claims'] = str(int(row['Total_open_claims']) - 1)

    # Write the updated dataset back to the file
    with open('C:/Users/spati/OneDrive/Desktop/FINAL DRAFT/Data Engineering/datasheet.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Example usage:
update_claim_status('1001', 'open')  
update_claim_status('1002', 'closed')  
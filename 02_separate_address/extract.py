import pandas as pd
import re

def extract_address_parts(addresses_file, address_mapping_file):
    # Load the CSV file with address components
    address_data = pd.read_csv(address_mapping_file)
    
    # Create a dictionary for quick lookup
    mapping_dict = {}
    for idx, row in address_data.iterrows():
        key = (row['sido'], row['sigungu'], row['doromyong'])
        mapping_dict[key] = (row['sido'], row['sigungu'], row['doromyong'])
    
    # Read the addresses from the text file
    with open(addresses_file, 'r', encoding='utf-8') as file:
        addresses = file.readlines()

    # Prepare a DataFrame to store categorized data
    results = pd.DataFrame(columns=['sido', 'sigungu', 'doromyong', 'detailed_address'])

    # Process each address
    for address in addresses:
        address = address.strip()
        found = False
        # Check each combination in the dictionary
        for key in mapping_dict:
            if all(part in address for part in key):
                found = True
                detailed_address = address.replace(key[0], '').replace(key[1], '').replace(key[2], '').strip()
                results = results._append({
                    'sido': key[0],
                    'sigungu': key[1],
                    'doromyong': key[2],
                    'detailed_address': detailed_address
                }, ignore_index=True)
                break

        # Handle addresses that do not match
        if not found:
            results = results._append({
                'sido': None,
                'sigungu': None,
                'doromyong': None,
                'detailed_address': address
            }, ignore_index=True)

    # Save results to a new CSV file
    # results.to_csv('categorized_addresses.csv', index=False, encoding='utf-8')
    results.to_csv('categorized_addresses3.xlsx', index=False, encoding='utf-8')

# Example usage
extract_address_parts('suwonjungang_addresses.txt', 'sido_sigungu_doro.csv')


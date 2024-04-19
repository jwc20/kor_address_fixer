import pandas as pd
import re

def extract_address_parts(addresses_file, address_mapping_file):
    address_data = pd.read_csv(address_mapping_file)
    
    mapping_dict = {}
    for idx, row in address_data.iterrows():
        key = (row['sido'], row['sigungu'], row['doromyong'])
        mapping_dict[key] = (row['sido'], row['sigungu'], row['doromyong'])
    
    with open(addresses_file, 'r', encoding='utf-8') as file:
        addresses = file.readlines()

    results = pd.DataFrame(columns=['sido', 'sigungu', 'doromyong', 'detailed_address'])

    for address in addresses:
        address = address.strip()
        found = False
        for key in mapping_dict:
            if all(part in address for part in key):
                found = True
                key_2 = address[address.index(key[2]):].split()[0]
                if key_2.endswith('길'):
                    detailed_address = address.replace(key[0], '').replace(key[1], '').replace(key_2, '').strip()
                    detailed_address += ' ' + key_2.rstrip('길')
                else:
                    detailed_address = address.replace(key[0], '').replace(key[1], '').replace(key_2, '').strip()

                results = results._append({
                    'sido': key[0],
                    'sigungu': key[1],
                    'doromyong': key_2,
                    'detailed_address': detailed_address
                }, ignore_index=True)
                break

        if not found:
            results = results._append({
                'sido': None,
                'sigungu': None,
                'doromyong': None,
                'detailed_address': address
            }, ignore_index=True)

    results.to_excel('categorized_addresses_20240419_1223_2.xlsx', index=False, engine='openpyxl')

extract_address_parts('suwonjungang_addresses.txt', 'sido_sigungu_doro.csv')



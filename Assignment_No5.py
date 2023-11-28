###  Assignment No 5 ###
# Name : Sandhya Govind Nikale
# Batch : B3
# Roll No : 42
# Assignment Title :Implement regular expression function to find Postal Code, PAN
#number, Mobile number in textual data using python libraries
import re

def find_entities(text):

    result = {
        'Postal Code': re.findall(r'[0-9]{3}[-]{1}[0-9]{3}', text),
        'PAN Numbers': re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text),
        'Mobile Number':re.findall(r'[+]{1}[0-9]{2}[ ]{1}[0-9]{10}', text),         
    }
    return result

# Example usage:
sample_text = """
First Dataset
Postal Code of Shirdi is 423-107.
My PAN Number is CTBPN0854P.
Mobile Number is +91 7385431507.


Second Dataset
Postal Code of Ahmednagar is 410-001
My PAN Number is QWERT6789P.
Mobile Number is +91 9850851611
"""

result = find_entities(sample_text)

for entity_type, entities in result.items():
    print(f"{entity_type}: {entities}")

# Output
''' 
Postal Code: ['423-107', '410-001']
PAN Numbers: ['CTBPN0854P', 'QWERT6789P']
Mobile Number: ['+91 7385431507', '+91 9850851611']

'''    


import json
import re
import pdb
import sys

def subscriber_conversion(subscriber_string):
    number = float(re.search(r'[0-9\.]+', subscriber_string).group())
    if subscriber_string[-1] == 'k':
        subscriber_numeric = number * 1000
    elif subscriber_string[-1] == 'm':    
        subscriber_numeric = number * 1000000
    else:
        subscriber_numeric = number
    return subscriber_numeric

with open('finindep_2hop.json', 'r') as f:
    docs = json.load(f)
    f.close()

for doc in docs:
    # Skip records without a subscriber attribute
    if 'subscribers' in doc.keys():
        # Skip records where subscriber number is 'null'
        if doc['subscribers'] is not None:
            doc['subscribers'] = subscriber_conversion(doc['subscribers'])

with open('finindep_fix.json', 'w') as f:
    json.dump(docs, f)
    f.close()

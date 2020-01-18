from pyusps import address_information
from csv import reader
#import re

addresses = list()
with open('output.txt', 'w') as f:
    f.write('City\tState\tAddress\tZip Code\n')
with open('addresses.txt', 'r') as f:
    r = reader(f, delimiter='\t')
    # Skip the first row.
    next(r)
    for row in r:
        city, state, addr, zip_code = row
        address = dict([('address', addr), ('city', city), ('state', state), ('zip_code', zip_code)])
        try:
            addresses.append(address_information.verify("033NONE01173",address))
        except:
            print("Check address " + address['address'])
        print(address)

    for address in addresses:
        try:
            addr = address['address']+"\t"+address['city']+"\t"+address['state']+"\t"+address['zip5']+"-"+address['zip4']
            print(addr)
            open('output.txt', 'a').write(addr + '\n')
        except:
            print("There was an error")

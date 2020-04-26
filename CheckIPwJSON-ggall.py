import json
import os
from pprint import pprint
import ipaddress

#/Did a pip install to bring in IPy -->pip3 install IPy
from IPy import IP

#Local location of source code--> dne-security-code/intro-python/parsing-json/CSA-SG-Challenge-4-24

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'

#print(f'The Python data format for the "deviceJSON" variable is {type(deviceJSON)}')
#print()
#print(deviceJSON)
#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


print("\n----------- Challenge --> Parse JSON file and Show IP Address Type -----------------\n")
deviceJSON_data = json.loads(deviceJSON)
print("\n------Show contents of deviceJSON_data after load from deviceJSON---------\n")
pprint(deviceJSON_data)
print("\n")

for find_interface in deviceJSON_data["interfaces"]["interface"]:
# Loop through the interfaces in the JSON data and get each interface's name and ip """
    for each_intf, ipaddress in find_interface.items():
        # Get the IP Address Value in prep for finding iptype
        ipaddress_value = IP(ipaddress["ipv4"])
        # In the print statement use .iptype() on the IP address value to get the type of address ....Public, Private, etc
        print("Interface: {} with IP Address: {} \t --> {}".format(each_intf, ipaddress_value, ipaddress_value.iptype()))

print("\nHave a Great Day! \n")

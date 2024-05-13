# This script takes a range input of vlans directly from a configuration and converts
# it to the l2vlans data model for AVD
# Example input:  1-12,15,20,23-30,40,47,145
#
#
# Special thanks to the Wizard for your help!

vlan_range = input("Enter your vlan range: ")

def mixrange(vlan):
    return_list = []
    for i in vlan.split(','):
        if '-' not in i:
            return_list.append(int(i))
        else:
            l,h = map(int, i.split('-'))
            return_list+= range(l,h+1)
    return return_list

vlan_list = mixrange(vlan_range)

vlan_config = open("vlan.txt", "w")

for vid in vlan_list:
    print('- id:', vid, file=vlan_config)
    print('  name:', f'"{vid}"', file=vlan_config)
    print('  tags: [', f'"{vid}"', ']', file=vlan_config)

vlan_config.close()

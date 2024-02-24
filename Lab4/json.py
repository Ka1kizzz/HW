import json
with open('sample-data.json') as file:
    data = json.load(file)
imdata_list = data.get('imdata', [])
for item in imdata_list:
    attributes = item.get('l1PhysIf', {}).get('attributes', {})
    if attributes:
        print("Interface ID:", attributes.get('id'))
        print("Admin Status:", attributes.get('adminSt'))
        print("Auto Negotiation:", attributes.get('autoNeg'))
        print("Description:", attributes.get('descr'))
        print("Link Debounce:", attributes.get('linkDebounce'))
        print("Speed:", attributes.get('speed'))
        print("Usage:", attributes.get('usage'))
        print("--------------------------------------------------")

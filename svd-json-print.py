import json
# pp{
#  "+p_xml": "version=\"1.0\" encoding=\"utf-8\"",
#  "device": {
#      "name": 
#       ...
#      "cpu": ...
#      "peripherals": {
#        "peripheral": [
#          { 
#            "name": "RESETS",
#            "baseAddress": "0x40020000",
#            "addressBlock": {
#             "offset": "0",
#             "size": "12",
#             "usage": "registers"
#           },
#           "registers": {
#            "register": [
#             {
#                "name": "RESET",
#                "addressOffset": "0x00000000",
#                "resetValue": "0x1fffffff",
#                "fields": {
#                  "field": [
jc=json.load(open('/tmp/j.json','r'))
print(jc.get('device').get('description'))
for i in range(len(jc.get('device').get('peripherals').get('peripheral'))):
        p=jc.get('device').get('peripherals').get('peripheral')[i]
        ab=p.get("addressBlock")
        if isinstance(ab,dict):
         if ab.get("offset")!='0': 
            print("-->offset=%s"%ab.get("offset"))
         if ab.get("usage")!="registers": 
            print("-->usage=%s"%ab.get("usage"))
        elif not ab is None:
            print("??"+type(ab))
        print('%-20s\t%s\t%s' % (p.get('name'), p.get('baseAddress'), p.get('description')))
        if p.get('registers'):
            rs=p.get('registers').get('register')
            if isinstance(rs,list):
                for j in range(len(rs)):
                    r=rs[j]
                    print('\t%20s\t%s\t%s' % (r.get('name'), r.get('addressOffset'), r.get('description')))
            elif isinstance(rs,dict):
                for j in rs:
                    print(f'\t{j}\t{rs[j]}')

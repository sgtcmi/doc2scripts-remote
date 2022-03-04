

import json

fh=open ('SCRPT170970200102.scripts' ,"r")
print(fh)
js=json.load(fh)

#for key in js.keys():
    #print(key)
    #print('******')
    #print(js[key])
    #print('******')

scenario_id = js['ssaObject']['recordId']
print(scenario_id)
script_Ids=[scenario_id+'-'+script_id for script_id in  js['ssaObject']['suffix']]

print(script_Ids)

#for key in js['sstObjectList'][0].keys():
    #print('-------')
    #print(key)
    #print('------')
    #print(js['sstObjectList'][0][key])
# for i in range(len(script_Ids)):
important_keys=[key for key in js['sstObjectList'][0].keys() if  js['sstObjectList'][0][key]]
print(important_keys)

for key in important_keys:
    print(key)
    print('----')

    print(js['sstObjectList'][0][key])



# Important stuffs to take out 
# scriptid description productgroup
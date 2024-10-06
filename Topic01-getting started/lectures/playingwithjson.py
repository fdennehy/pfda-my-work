# playing with JSON
# Author: FInbar Dennehy

import json
#create dictionary object, data
data = {
    'name' : 'joe',
    'age' : 21,
    'student': True
    }
jsonString = json.dumps(data)
print (data)
print (jsonString)
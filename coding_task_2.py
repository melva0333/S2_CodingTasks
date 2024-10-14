'''Write a function/method to accept a multi-dimensional JSON array 
and produce an equivalent list grouped by any valid field:

cars=[
  {"car_make": "bmw", "car_model": "m2", "transmission": "automatic"},
  {"car_make": "audi", "car_model": "A3", "transmission": "automatic"},
  {"car_make": "ford", "car_model": "focus", "transmission": "manual"},
  {"car_make": "audi", "car_model": "quatro", "transmission": "manual"},

  {"car_make": "bmw", "car_model": "330i", "transmission": "manual"},
  {"car_make": "nissan", "car_model": "leaf", "transmission": "automatic"}
]
'''

def group_by_field(array,field):
    grouped_data = {}
    for item in array:
        key = item.get(field) #use the passed field to group
        if key not in grouped_data:
            grouped_data[key]=[]
        #Append the remaining fields to the items (excluding the field being grouped by)
        grouped_data[key].append({k:v for k,v in item.items() if k!=field})
        #Convert grouped_data dictionary to list format
        result=[{field:key, "items": value} for key, value in grouped_data.items()]
    return result

cars=[
  {"car_make": "bmw", "car_model": "m2", "transmission": "automatic"},
  {"car_make": "audi", "car_model": "A3", "transmission": "automatic"},
  {"car_make": "ford", "car_model": "focus", "transmission": "manual"},
  {"car_make": "audi", "car_model": "quatro", "transmission": "manual"},

  {"car_make": "bmw", "car_model": "330i", "transmission": "manual"},
  {"car_make": "nissan", "car_model": "leaf", "transmission": "automatic"}
]
#Sample tests
print(group_by_field(cars,"car_make"))

print(group_by_field(cars, "car_model"))

print(group_by_field(cars, "transmission"))
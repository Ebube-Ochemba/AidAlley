# test.py
from models.base_model import BaseModel
from models import storage

# Reload storage from file
print("---reloading storage---")
all_obj = storage.all()
for obj_id in all_obj.keys():
    obj = all_obj[obj_id]
    print(obj)
print("---storage reloaded---")

# Create a new instance of BaseModel
print("---creating new instance---")
new_instance = BaseModel()
print(new_instance.id)  # Print ID
print(new_instance)  # Print the string representation
print(type(new_instance.created_at))  # Print the type of created_at
print("---new instance created---")

print("---constructing JSON from instance---")
new_instance_json = new_instance.to_dict()
print(new_instance_json)
print("JSON of new instance:")
for key in new_instance_json.keys():
    print("\t{}: ({}) - {}".format(key, type(new_instance_json[key]), new_instance_json[key]))
print("---JSON of new instance constructed---")

print("---reconstructing instance from JSON---")
my_new_instance = BaseModel(**new_instance_json)
print(my_new_instance.id)
print(my_new_instance)
print(type(my_new_instance.created_at))
print("---new instance reconstructed---")

print("---check if instances are the same---")
print(new_instance is my_new_instance)
print("---checked if instances are the same---")

# Save the instance to the storage
print("saving instance")
new_instance.save()
print("saved instance")

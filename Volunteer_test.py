from models import storage
from models.volunteer import Volunteer

# Reload storage from file
print("---reloading storage---")
all_obj = storage.all()
for obj_id in all_obj.keys():
    obj = all_obj[obj_id]
    print(obj)
print("---storage reloaded---")

# Create a new volunteer
print("---creating new instance---")
volunteer1 = Volunteer()
volunteer1.first_name = "Walter"
volunteer1.last_name = "White"
volunteer1.email = "heisenberg@me.com"
volunteer1.phone = "555-555-5555"
volunteer1.availability = "Monday, Wednesday, Friday, Sunday"
volunteer1.password = "Heisenberg" # Password will be hashed
volunteer1.save()
print(volunteer1)  # Print the string representation
print("---new instance created---")

print("---creating a second instance---")
volunteer2 = Volunteer()
volunteer2.first_name = "Jesse"
volunteer2.last_name = "Pinkman"
volunteer2.email = "jesseblue@me.com"
volunteer2.phone = "222-222-2222"
volunteer2.availability = "Monday, Wednesday, Friday, Sunday"
volunteer2.password = "JessePinkman" # Password will be hashed
volunteer2.save()
print(volunteer2)  # Print the string representation
print("---new instance created---")

# Reload storage from file
print("---reloading storage---")
all_obj = storage.all()
for obj_id in all_obj.keys():
    obj = all_obj[obj_id]
    print(obj)
print("---storage reloaded---")
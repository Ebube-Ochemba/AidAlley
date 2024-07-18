#!/usr/bin/python3
from models import storage
from models.event import Event

# Reload storage from file
print("---reloading storage---")
all_obj = storage.all()
for obj_id in all_obj.keys():
    obj = all_obj[obj_id]
    print(obj)
print("---storage reloaded---")

# Create a new event
print("---creating new event instance---")
event1 = Event()
event1.title = "Community Cleanup"
event1.description = "Join us for a community cleanup event."
event1.date = "2023-07-01T09:00:00+00:00"  # ISO 8601 format
event1.location = "123 Main St, Anytown, USA"
event1.creator_id = "some-creator-uuid"
event1.save()
print(event1)  # Print the string representation
print("---new event instance created---")

# Create another event
print("---creating a second event instance---")
event2 = Event()
event2.title = "Tree Planting"
event2.description = "Help us plant trees in the local park."
event2.date = "2023-08-15T10:00:00+00:00"  # ISO 8601 format
event2.location = "Local Park, Anytown, USA"
event2.creator_id = "another-creator-uuid"
event2.save()
print(event2)  # Print the string representation
print("---second event instance created---")

# Reload storage from file
print("---reloading storage---")
all_obj = storage.all()
for obj_id in all_obj.keys():
    obj = all_obj[obj_id]
    print(obj)
print("---storage reloaded---")

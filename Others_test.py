from models import storage
from models.event_volunteer import EventVolunteer
from models.volunteer_hours import VolunteerHours
from models.notification import Notification

# Reload storage from file
print("---reloading storage---")
all_obj = storage.all()
for obj_id in all_obj.keys():
    obj = all_obj[obj_id]
    print(obj)
print("---storage reloaded---")

# Create a new event_volunteer
print("---creating new instance---")
event_volunteer1 = EventVolunteer()
event_volunteer1.event_id = "event-uuid"
event_volunteer1.volunteer_id = "volunteer-uuid"
event_volunteer1.status = "accepted"
event_volunteer1.save()
print(event_volunteer1)  # Print the string representation
print("---new event instance created---")

# Create another event_volunteer
print("---new event instance created---")
event_volunteer2 = EventVolunteer()
event_volunteer2.event_id = "event-uuid"
event_volunteer2.volunteer_id = "volunteer-uuid"
event_volunteer2.status = "accepted"
event_volunteer2.save()
print(event_volunteer2)  # Print the string representation
print("---second event instance created---")

# Create a new volunteer_hours
print("---creating new instance---")
volunteer_hours1 = VolunteerHours()
volunteer_hours1.volunteer_id = "volunteer-uuid"
volunteer_hours1.event_id = "event-uuid"
volunteer_hours1.hours = 5.5
volunteer_hours1.verified = False
volunteer_hours1.save()
print(volunteer_hours1)  # Print the string representation
print("---new event instance created---")

# Create another volunteer_hours
print("---new event instance created---")
volunteer_hours2 = VolunteerHours()
volunteer_hours2.volunteer_id = "volunteer-uuid"
volunteer_hours2.event_id = "event-uuid"
volunteer_hours2.hours = 7.5
volunteer_hours2.verified = False
volunteer_hours2.save()
print(volunteer_hours2)  # Print the string representation
print("---second event instance created---")

# Create a new notification
print("---creating new instance---")
notification1 = Notification()
notification1.volunteer_id = "volunteer-uuid"
notification1.message = "You have a new message"
notification1.status = "unread"
notification1.save()
print(notification1)  # Print the string representation
print("---new event instance created---")

# Create another notification
print("---new event instance created---")
notification2 = Notification()
notification2.volunteer_id = "volunteer-uuid"
notification2.message = "You have a new message"
notification2.status = "unread"
notification2.save()
print(notification2)  # Print the string representation
print("---second event instance created---")

# Reload storage from file
print("---reloading storage---")
all_obj = storage.all()
for obj_id in all_obj.keys():
    obj = all_obj[obj_id]
    print(obj)
print("---storage reloaded---")
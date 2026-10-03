# Two dictionaries
rooms = {}
resources = {}

# Add a room
def add_room():
    print("\nAdd Room")
    room_id = input("Enter room ID: ")

# Check room exists
    if room_id in rooms:
        print("Invalid room ID. Room already exists.")
        return
    room_type = input("Enter room type: ")
    capacity = input("Enter capacity: ")

    if not capacity.isdigit() or int(capacity) <= 0:
        print("Capacity must be a positive number. Try again!")
        return
    capacity = int(capacity)
    status = input("Enter status (Available or Booked): ")
    if status not in ["Available", "Booked"]:
        print("Try again! Status must be Available or Booked.")
        return
    
# Store room Id in the rooms dictionary as the key
    rooms[room_id] = {
        "type": room_type,
        "capacity": capacity,
        "status": status
    }
    print("room added!")

# Add a resource
def add_resource():
    print("\nAdd Resource")
    resource_id = input("Enter resource ID: ")

# Check resource ID to prevent duplication
    if resource_id in resources:
        print("Invalid resource ID. Resource already exists.")
        return

    name = input("Enter resource name: ")
    category = input("Enter category: ")
    condition = input("Enter condition: ")

    status = input("Enter status (Available or Booked): ")

    if status not in ["Available", "Booked"]:
        print("Try again! Status must be Available or Booked.")
        return

    resources[resource_id] = {
        "name": name,
        "category": category,
        "condition": condition,
        "status": status
    }
    print("resource added!")


# Display All Rooms and Resources

def display():
    print("\nAll Rooms")
# Check the rooms dictionary contains any rooms
    if len(rooms) == 0:
        print("No rooms found.")
    else:
        for room_id in rooms:
            room = rooms[room_id]
            print("\nRoom ID:", room_id)
            print("Type:", room["type"])
            print("Capacity:", room["capacity"])
            print("Status:", room["status"])
    print("\nAll Resources")

    if len(resources)==0:
        print("No resources found.")
    else:
        for resource_id in resources:
            resource = resources[resource_id]

            print("\nResource ID:", resource_id)
            print("Name:", resource["name"])
            print("Category:", resource["category"])
            print("Condition:", resource["condition"])
            print("Status:", resource["status"])


# Searching room by type

def search_room():
    print("\nSearch Room by Type")
    search_type = input("Enter room type: ")

    found = False
# Check each room for a matching in the rooms dictionary
    for room_id in rooms:
        room = rooms[room_id]

        if room["type"].lower() == search_type.lower():
            print("\nRoom ID:", room_id)
            print("Type:", room["type"])
            print("Capacity:", room["capacity"])
            print("Status:", room["status"])
            found = True

    if found == False:
        print("No room found. Change the type and try again!")


# Search resource by category

def search_resource():
    print("\nSearch Resource by Category")
    search_category = input("Enter Resource Category: ")
    found = False
# Check each resource for a matching in the resources dictionary
    for resource_id in resources:
        resource = resources[resource_id]
# Compare stored resource category with user's search input
        if resource["category"].lower() == search_category.lower():
            print("\nResource ID:", resource_id)
            print("Name:", resource["name"])
            print("Category:", resource["category"])
            print("Condition:", resource["condition"])
            print("Status:", resource["status"])

            found = True

    if found == False:
        print("No resource found.")


# Update Booking Status

def update_status():
    print("\nUpdate Booking Status")
    print("1. Update Room")
    print("2. Update Resource")

    choice = input("Enter your choice: ")

    if choice == "1":
        room_id = input("Enter room ID: ")
# Check the id exists in the rooms dictionary
        if room_id not in rooms:
            print("The room does not exist.")
            return

        new_status = input(
            "Enter new status (Available/Booked): "
        )

        if new_status not in ["Available", "Booked"]:
            print("Try again! Status must be Available or Booked.")
            return
# Update room's status
        room = rooms[room_id]
        room["status"] = new_status
        print("Room status updated successfully!")

    elif choice == "2":
        resource_id = input("Enter Resource ID: ")
# Check the resource ID exists in the resources dictionary
        if resource_id not in resources:
            print("Error: Resource does not exist.")
            return

        new_status = input(
            "Enter new status (Available/Booked): "
        )

        if new_status not in ["Available", "Booked"]:
            print("Error: Status must be Available or Booked.")
            return

        resource = resources[resource_id]
        resource["status"] = new_status

        print("Resource status updated successfully!")

    else:
        print("Invalid choice.")


# Main Menu

def main():
# Keep displaying the menu untill the user choose to exit
    while True:

        print("\nSmart Campus Room Booking Manager")
        print("1. Add Room")
        print("2. Add Resource")
        print("3. Display All")
        print("4. Search Room by Type")
        print("5. Search Resource by Category")
        print("6. Update Booking Status")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_room()

        elif choice == "2":
            add_resource()

        elif choice == "3":
            display()

        elif choice == "4":
            search_room()

        elif choice == "5":
            search_resource()

        elif choice == "6":
            update_status()

        elif choice == "7":
            print("Exit successfully")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main() 
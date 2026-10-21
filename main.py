import json

FILE_NAME = "resources.json"


def add_resource():
    print("\n===== Add a Resource =====")

    resource_id = input("Enter resource ID: ").strip()
    title = input("Enter resource title: ").strip()
    course = input("Enter course name: ").strip()
    resource_type = input("Enter resource type (Book/Notes/PDF): ").strip()

    if not resource_id or not title or not course or not resource_type:
        print("All fields are required.")
        return

    for resource in resources:
        if resource["id"] == resource_id:
            print("This resource ID already exists.")
            return

    resource = {
        "id": resource_id,
        "title": title,
        "course": course,
        "type": resource_type
    }

    resources.append(resource)
    save_resources()
print("Resource added successfully!")

def view_resources():
    print("\n===== All University Resources =====")

    if not resources:
        print("No resources available yet.")
        return

    for resource in resources:
        print("------------------------------")
        print(f"ID: {resource['id']}")
        print(f"Title: {resource['title']}")
        print(f"Course: {resource['course']}")
        print(f"Type: {resource['type']}")

def search_resource():
    print("\n===== Search for a Resource =====")

    search_title = input("Enter resource title to search: ").strip().lower()

    if not search_title:
        print("Please enter a title to search.")
        return

    found = False

    for resource in resources:
        if search_title in resource["title"].lower():
            print("------------------------------")
            print(f"ID: {resource['id']}")
            print(f"Title: {resource['title']}")
            print(f"Course: {resource['course']}")
            print(f"Type: {resource['type']}")
            found = True

    if not found:
        print("No matching resource found.")

def delete_resource():
    print("\n===== Delete a Resource =====")

    resource_id = input("Enter the resource ID to delete: ").strip()

    for resource in resources:
        if resource["id"] == resource_id:
            resources.remove(resource)
            save_resources()
            print("Resource deleted successfully!")
            return

    print("Resource ID not found.")

def save_resources():
    with open(FILE_NAME, "w") as file:
        json.dump(resources, file, indent=4)


def load_resources():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Resource file is empty or invalid.")
        return []
resources = load_resources()

while True:
    print("\n===== University Resource Management System =====")
    print("1. Add a resource")
    print("2. View all resources")
    print("3. Search for a resource")
    print("4. Delete a resource")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_resource()

    elif choice == "2":
        view_resources()

    elif choice == "3":
        search_resource()

    elif choice == "4":
        delete_resource() 

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

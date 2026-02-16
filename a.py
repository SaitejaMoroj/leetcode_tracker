import requests
import argparse
BASE_URL = "https://dummyjson.com/users"
def print_user(user):
    print(f"ID        : {user['id']}")
    print(f"Name      : {user['firstName']} {user['lastName']}")
    print(f"Username  : {user['username']}")
    print(f"Email     : {user['email']}")
    print(f"Phone     : {user['phone']}")
    print(f"Age       : {user['age']}")
    print(f"Gender    : {user['gender']}")
    print(f"City      : {user['address']['city']}")
    print(f"Company   : {user['company']['name']}")
    print("-" * 40)
def get_all_users():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            return response.json()["users"]
        return []
    except:
        print("Error occured")
        return []
def get_user_info(username, password):
    try:
        users = get_all_users()
        for user in users:
            if user["username"] == username and user["password"] == password:
                return user
        return None
    except:
        print("Error occured")
        return None
parser = argparse.ArgumentParser(description="Validate user credentials")
parser.add_argument("username", nargs="?")
parser.add_argument("password", nargs="?")

args = parser.parse_args()
username = args.username
password = args.password
try:
    if not username and not password:
        print("All Users List\n")
        users = get_all_users()
        for u in users:
            print_user(u)

    elif username and password:
        user = get_user_info(username, password)
        if user:
            print("Login Successful\n")
            print_user(user)
        else:
            print("UserNotFound")

    else:
        print("Please provide both username and password")
except:
    print("Error occured")

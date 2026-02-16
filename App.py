import requests

BASE_URL = "https://dummyjson.com"


def get_user_info(username, password):
    login_response = requests.post(f"{BASE_URL}/auth/login",json={
            "username": username,
            "password": password
        }
    )

    user_id = login_response.json().get("id")

    user_response = requests.get(f"{BASE_URL}/users/{user_id}")

    if user_response.status_code == 200:
        return user_response.json()

    return None
username = input("Enter username: ")
password = input("Enter password: ")

data_info = get_user_info(username, password)

if data_info:
    print(data_info)
else:
    print("Invalid credentials")

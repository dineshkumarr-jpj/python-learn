
import requests

Url = "https://jsonplaceholder.typicode.com"
response = requests.get(f"{Url}/users")

print("GET STATUS:", response.status_code)

users = response.json()

for user in users[:5]:
    print("ID:", user["id"])
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("-------------------")
new_post = {
    "title": "Learning Python API",
    "body": "I am learning GET and POST requests",
    "userId": 1
}

response = requests.post(
    f"{Url}/posts",
    json=new_post
)

print("POST STATUS:", response.status_code)
print("Created ID:", response.json()["id"])

updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated post body",
    "userId": 1
}

response = requests.put(
    f"{Url}/posts/1",
    json=updated_post
)

print("PUT STATUS:", response.status_code)

partial_update = {
    "title": "Partially Updated Title"
}

response = requests.patch(
    f"{Url}/posts/1",
    json=partial_update
)
print("PATCH STATUS:", response.status_code)

response = requests.delete(f"{Url}/posts/1")

print("DELETE STATUS:", response.status_code)

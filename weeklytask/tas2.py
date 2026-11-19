
import os
import csv
import json
import requests
from dotenv import load_dotenv
os.chdir(os.path.dirname(os.path.abspath(__file__)))

HOW_MANY = 1

employees = []

csv_file = open("employees.csv", "r")
reader = csv.DictReader(csv_file)      
for row in reader:
    row["id"] = int(row["id"])        
    row["salary"] = int(row["salary"])
    employees.append(row)
csv_file.close()

json_file = open("employees.json", "w")
json.dump(employees, json_file, indent=2)
json_file.close()

high_earners = []
for emp in employees:
    if emp["salary"] > 50000:
        high_earners.append(emp)

out_file = open("high_earners.csv", "w", newline="")
writer = csv.DictWriter(out_file, fieldnames=["id", "name", "department", "salary", "city"])
writer.writeheader()
writer.writerows(high_earners)
out_file.close()

print("Rows read:", len(employees), "| High earners:", len(high_earners))

load_dotenv()                       
api_key = os.getenv("API_KEY")      
headers = {}
if api_key:
    headers = {"Authorization": "Bearer " + api_key}

url = "https://jsonplaceholder.typicode.com/users"
users = []

try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()    
    users = response.json()

    for user in users[:HOW_MANY]:
        print(user["id"], "-", user["name"], "-", user["email"])

except requests.exceptions.Timeout:
    print("Error: the request timed out")
except requests.exceptions.ConnectionError:
    print("Error: could not connect to the server")
except requests.exceptions.HTTPError as error:
    print("Error: HTTP problem", error)

try:
    response = requests.get(url + "/9999", headers=headers, timeout=5)
    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        print("/users/9999 ->", response.status_code)

except requests.exceptions.Timeout:
    print("Error: the request timed out")
except requests.exceptions.ConnectionError:
    print("Error: could not connect to the server")

clean_users = []

for user in users:
    address = user.get("address", {})      
    geo = address.get("geo", {})           
    company = user.get("company", {})

    clean_user = {
        "id": user.get("id"),
        "name": user.get("name"),
        "email": user.get("email"),
        "city": address.get("city"),
        "lat": geo.get("lat"),
        "company": company.get("name"),
    }
    clean_users.append(clean_user)

json_file = open("users.json", "w")
json.dump(clean_users, json_file, indent=2)
json_file.close()
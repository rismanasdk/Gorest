import requests

authorization = {
    "Authorization": "Bearer <TOKEN_GOREST>",
    "Content-Type": "application/json"
}

while True:
    if authorization.get("Authorization") == "Bearer <TOKEN_GOREST>":
        print("Enter the Token Gorest First...")
        break
    else:

        print("========GOREST==========")

        lists = ["GET", "POST", "PUT", "DELETE"]
        emails = ("@gmail.com", "@example.com")

        for list in lists:
            print("-", list)

        Method = input("Choose Method :").upper()

        if Method == "GET":
            spe = input("Search user using id (optional) :")
            BASE = f"https://gorest.co.in/public/v2/users/{spe}"
        elif Method == "POST":
            BASE = f"https://gorest.co.in/public/v2/users"
        elif Method == "PUT":
            spe = input("Enter id :")
            if spe == "":
                print("Id is mandatory")
                break
            else:
                BASE = f"https://gorest.co.in/public/v2/users/{spe}"
        elif Method == "DELETE":
            spe = input("Enter id :")
            if spe == "":
                print("Id is mandatory")
                break
            else:
                BASE = f"https://gorest.co.in/public/v2/users/{spe}"

        if Method not in lists:
            print("Method not supported")
            break
        elif Method == "GET":
            app = input("(text/json ?) :").upper()
            if app == "TEXT":
                r = requests.get(BASE, headers=authorization)
                print(r.text)
                print(f"Status Code :{r.status_code}")
                break
            elif app == "JSON":
                r = requests.get(BASE, headers=authorization)
                print(r.json())
                print(f"Status Code :{r.status_code}")
                break
            else:
                print("Invalid")
                break
        elif Method == "POST":
            name = input("Enter Name :")
            email = input("Enter Email :")
            gender = input("Choose Gender (male/female) :").lower()
            status = input("Choose Status (active/inactive) :").lower()
            app = input("(text/json) :").upper()

            if gender not in ["male", "female"]:
                print("Choose one (male/female)")
                break
            elif status not in ["active", "inactive"]:
                print("Choose one (active/inactive)")
                break
            elif not email.endswith(emails):
                print(f"Domain Email Supported :{emails}")
                break

            data = {
                "name": name,
                "email": email,
                "gender": gender,
                "status": status
            }

            r = requests.post(BASE, headers=authorization, json=data)
            if app == "TEXT":
                print(r.text)
                print(f"Status Code :{r.status_code}")
                break
            elif app == "JSON":
                print(r.json())
                print(f"Status Code :{r.status_code}")
                break
            else:
                print("Invalid")
                break

        elif Method == "PUT":
            name = input("Enter Nama :")
            email = input("Enter Email :")
            gender = input("Choose Gender (male/female) :").lower()
            status = input("Choose Status (active/inactive) :").lower()
            app = input("(text/json) :").upper()

            if gender not in ["male", "female"]:
                print("Choose one (male/female)")
                break
            elif status not in ["active", "inactive"]:
                print("Choose one (active/inactive)")
                break
            elif not email.endswith(emails):
                print(f"Domain Email Supported :{emails}")
                break

            payload = {
                "name": name,
                "email": email,
                "gender": gender,
                "status": status
            }

            r = requests.put(BASE, headers=authorization, json=payload)
            if app == "TEXT":
                print(r.text)
                print(f"Status Code :{r.status_code}")
                break
            elif app == "JSON":
                print(r.json())
                print(f"Status Code :{r.status_code}")
                break
            else:
                print("Invalid")
                break
        elif Method == "DELETE":
            r = requests.delete(BASE, headers=authorization)
            print(f"Status Code :{r.status_code}")
            break
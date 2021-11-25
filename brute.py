import requests
import time

PATH = "C:\\Users\\Everone\\Documents\\GCPBucketBrute\\"
URL = "https://www.googleapis.com/storage/v1/b/"


file_name = input("Enter file name: ")

PATH = PATH + file_name

with open(PATH) as file:
    file_contents = file.read()
    lines = [line for line in file_contents.splitlines() if "EXISTS" in line or "UNAUTHENTICATED ACCESS ALLOWED" in line]
    buckets = [line.split(" ")[-1] for line in lines]
    for bucket in buckets:
        #print(URL + bucket + "/o")
        r = requests.get(URL + bucket + "/o")
        if r.status_code == 200:
            print(URL + bucket + "/o")
            print("Bucket: " + bucket + " is open. Status code:" + str(r.status_code))
            time.sleep(1)
            data = r.json()
            if data:
                if "items" not in data:
                    print("No items in bucket")
                    print("\n")
                    time.sleep(1)
                else:
                    items = data["items"]
                    print("**************************************************************")
                    for item in items:
                        print(item["name"])
                    print("**************************************************************")
                    print("\n")
                    time.sleep(1)

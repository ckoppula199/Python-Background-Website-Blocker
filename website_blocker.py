import time
from datetime import datetime as dt

hosts_temp = "hosts"
host_file_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
block_site_list = ["www.facebook.com", "www.instagram.com", "www.reddit.com", "facebook.com", "instagram.com", "reddit.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print("working hours")
        with open(host_file_path, "r+") as file:
            file_content = file.read()
            for website in block_site_list:
                if website in file_content:
                    continue
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        print("fun hours")
        with open(host_file_path, "r+") as file:
            file_content = file.readlines()
            file.seek(0)
            for line in file_content:
                if not any(website in line for website in block_site_list):
                    file.write(line)
                else:
                    continue
            file.truncate()
    time.sleep(5)

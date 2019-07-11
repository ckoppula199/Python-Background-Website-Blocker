import time
from datetime import datetime as dt

# temporary file path for testing program
hosts_temp = "hosts"
# actual file path where file to be changed is located
host_file_path = r"C:\Windows\System32\drivers\etc\hosts"
# the address we will redirect the user to if they go to a blocked site, can be changed
redirect = "127.0.0.1"
# list of sites to block, has 2 variations per site as if only 1 address is used it doesn't work all the time
block_site_list = ["www.facebook.com", "www.instagram.com", "www.reddit.com", "facebook.com", "instagram.com", "reddit.com"]

# infinte loop keeps programming running until system is shut down
while True:
    # checks if current time is between working hours (9 till 5)
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        #print("working hours")

        # checks if site string from block_site_list is found in the file, if not it writes the redirect address and the websites address to the file
        with open(host_file_path, "r+") as file:
            file_content = file.read()
            for website in block_site_list:
                if website in file_content:
                    continue
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        #print("fun hours")

        #checks each line of the file to see if it contains a website string, if it does then that line is not writen to the file
        with open(host_file_path, "r+") as file:
            file_content = file.readlines()
            file.seek(0) #used to set cursor to start of file so we write at the top of the file
            for line in file_content:
                if not any(website in line for website in block_site_list):
                    file.write(line)
                else:
                    continue
            file.truncate() # removes anything that comes after what we've just written to the top of the file
                            # as we basicaly just re-wrote the file on top of the existing file
    time.sleep(300) # waits five minutes as to not be a burden on CPU usage

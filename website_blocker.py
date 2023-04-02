import time
from datetime import datetime as dt

# specify the list of websites to block
blocked_websites = ['www.facebook.com', 'www.youtube.com', 'www.twitter.com']# Example websites, past your own once in here

# specify the path of the host file
host_path = r"/etc/hosts"

# specify the IP address to redirect to
redirect_ip = "127.0.0.1"

# specify the duration of the blocking in seconds
blocking_duration = 3600  # set the time (3600 sec = 1h)

while True:
    # check if the current time is within the blocking time interval (e.g. 9 AM to 5 PM)
    if dt.now().hour >= 9 and dt.now().hour < 17:
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    # add the website to the hosts file
                    file.write(f"{redirect_ip} {website}\n")
    else:
        # remove the blocked websites from the hosts file
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()

    # wait for the specified blocking duration before checking the time again
    time.sleep(blocking_duration)

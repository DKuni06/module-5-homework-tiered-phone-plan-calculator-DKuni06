#check one single API request for status

FAILURE_LIMIT = 5
REQUEST_LIMIT = 20
STREAK_LIMIT = 3

ip_count = int(input("How Many IP addresses should be reviewed? "))

total_requests = 0
total_failed_requests = 0
total_flagged_failure_streak = 0
#loop for each IP address that needs review
for ip in range(ip_count):

    ip_address = input("Enter IP address: ")
    request_count = int(input("How many requests came from this IP address? "))
    total_requests += request_count
    #initialize status counts
    success_count = 0
    failure_count = 0

    current_failure_streak = 0
    highest_failure_streak = 0

    #for every request, get status and request count
    for request in range(request_count):

        status = input("Enter request status (success or failure): ")

        #checks if user input incorrect value and requests a proper status
        while status != "failure" and status != "success":
            print("Invalid status." )
            print("Please enter a valid status (success or failure)")
            status = input("Enter status: ")
            
        if status == "success":
            #up the count of success requests
            success_count += 1

            #reset failure streak
            current_failure_streak = 0
            
        elif status == "failure":
            #up the count of failure requests
            failure_count += 1

            #update current failure streak
            current_failure_streak += 1

            if current_failure_streak > highest_failure_streak:
                highest_failure_streak = current_failure_streak
    total_failed_requests = failure_count
    ip_flagged = False
    if failure_count >= FAILURE_LIMIT:
        ip_flagged = True


    rate_limited = False
    if request_count > REQUEST_LIMIT:
        rate_limited = True

    limit_flagged = False
    if limit_flagged >= STREAK_LIMIT:
        limit_flagged = True
        total_flagged_failure_streak += 1

    #print summary for one IP
    print(f"IP address: {ip_address}")
    print(f"Successful requests: {success_count}")
    print(f"Failed requests: {failure_count}")
    print(f"Highest failure streak: {highest_failure_streak}")
    print(f"Flagged for IT review: {ip_flagged}")
    print(f"Rate limited: {rate_limited}")

#summarize requests across all IPs

print(f"Total requests {total_requests}")
print(f"Total failed requests {total_failed_requests}")

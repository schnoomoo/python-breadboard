import subprocess
import time

ip_addresses = ['10.0.0.45', '10.0.0.41', '10.0.0.40']

# Function to check if an IP address is reachable
def is_ip_reachable(ip):
    result = subprocess.run(['ping', '-c', '1', ip], capture_output=True)
    #print (result)
    return result.returncode == 0

# Main loop
while True:
    for ip in ip_addresses:
        previous_state = None
        current_state = is_ip_reachable(ip)
        print("IP:", ip, "  State:", current_state)
        time.sleep(1)  # Wait for 1 second before checking again


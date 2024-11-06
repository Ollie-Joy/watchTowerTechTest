import subprocess
import time
import requests

# Assume there's an API endpoint provided by the task scheduler to get IPs for scanning
TASK_API = "http://scheduler.example.com/api/get_ips_to_scan"


# Function to fetch tasks from the scheduler
def fetch_ips_from_scheduler(node_id):
    response = requests.get(f"{TASK_API}?node_id={node_id}")
    if response.status_code == 200:
        return response.json().get("ips", [])
    return []


# Function to scan IP addresses fetched for this node
def distributed_scan(node_id, rate_limit=1000):
    while True:
        # Fetch IP addresses from the scheduler
        ip_list = fetch_ips_from_scheduler(node_id)
        if not ip_list:
            print("No tasks assigned. Retrying in 10 seconds...")
            time.sleep(10)
            continue

        # Perform scans on the assigned IPs
        for ip in ip_list:
            print(f"Node {node_id} scanning IP: {ip} with rate limit {rate_limit}")
            result = subprocess.run(
                ["python", "scan.py", "--ip", ip, "--rl", str(rate_limit)],
                capture_output=True,
                text=True
            )
            # Output result (can also push to results storage here)
            print(result.stdout)

        # Wait before next task fetch to avoid overload
        time.sleep(5)


# Example: Start scanning with node ID 1
distributed_scan(node_id=1)

import subprocess

# Mock list of IP addresses across tenants for illustration (would typically be fetched from a database)
ip_addresses = [
    "192.168.1.1", "192.168.1.2", "192.168.1.3",  # Tenant 1 IPs
    "10.0.0.1", "10.0.0.2", "10.0.0.3",           # Tenant 2 IPs
    # Add all other IPs here...
]


# Function to scan IP addresses with a specified rate limit
def scan_ip_addresses(ip_list, rate_limit=1000):
    for ip in ip_list:
        print(f"Scanning IP: {ip} with rate limit {rate_limit}")
        # Run the mock scan script with the IP and rate limit
        result = subprocess.run(["python", "scan.py", "--ip", ip, "--rl", str(rate_limit)])
        # Output result
        print(result.stdout)


# Scan all IP addresses
if __name__ == '__main__':
    scan_ip_addresses(ip_addresses)

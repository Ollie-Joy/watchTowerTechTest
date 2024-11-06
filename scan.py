import json
import random
import argparse


def mock_nmap_scan(ip_address, rate_limit):
    # Predefined first 5 ports
    predefined_ports = [22, 80, 443, 8080, 3306]

    # Generate 195 random ports, excluding the predefined ones
    remaining_ports = random.sample([p for p in range(1, 65535) if p not in predefined_ports], 195)

    # Combine predefined ports and remaining random ports
    ports = predefined_ports + remaining_ports

    # Generate port scan results
    scan_results = []
    for port in ports:
        result = {
            'port': port,
            'protocol': 'tcp'
        }
        scan_results.append(result)

    # Create the mock JSON output
    mock_output = {
        'nmap_scan': {
            'ip_address': ip_address,
            'rate_limit': rate_limit, # Included but not used in logic
            'host_status': 'up',
            'scan_results': scan_results
        }
    }
    return json.dumps(mock_output, indent=4)


if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Mock Nmap scan")
    parser.add_argument('--ip', type=str, required=True, help='IP address to scan')
    parser.add_argument('--rl', type=int, required=False, default=1000,
                        help='Rate limit in packets per second (default 1000)')

    # Parse arguments
    args = parser.parse_args()

    # Run the mock scan
    scan_output = mock_nmap_scan(args.ip, args.rl)
    print(scan_output)

# ARP Scanner

The ARP Scanner script is used to scan the network and display the IP addresses and corresponding MAC addresses of devices on the local network. It uses the `scapy` library to craft ARP requests and analyze the responses.

## Features

1. **`get_args()`**:  
   This function allows passing arguments to the script via the command line. It expects the user to provide an IP address (or range of addresses) to be scanned.

2. **`scan(ip)`**:  
   This function sends ARP requests to the given IP address and collects responses, identifying devices on the network (IP and MAC addresses).

3. **`display_result(result)`**:  
   This function displays the scan results in a table format showing the IP and corresponding MAC addresses.

## How to Use

1. **Install dependencies**  
   To run the script, you need to have the `scapy` library installed. You can install it via `pip`:
   ```bash
   pip install scapy

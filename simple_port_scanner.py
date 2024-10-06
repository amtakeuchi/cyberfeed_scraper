from socket import *

# Function to scan a single port on the target host
def conScan(tgtHost, tgtPort):
    try: 
        # Create a TCP/IP socket
        connskt = socket(AF_INET, SOCK_STREAM)
        # Attempt to connect to the target host and port
        connskt.connect((tgtHost, tgtPort))
        # If successful, print that the port is open
        print('[+] %d/tcp open' % tgtPort)
        connskt.close()  # Close the socket connection
    except:
        # If connection fails, print that the port is closed
        print('[-] %d/tcp closed' % tgtPort)

# Function to scan multiple ports on a target host
def portScan(tgtHost, tgtPorts):
    try:
        # Resolve the target host to its IP address
        tgtIP = gethostbyname(tgtHost)
    except:
        # If resolution fails, print an error message
        print('[-] Cannot resolve %s' % tgtHost)
        return  # Exit the function

    try:
        # Attempt to get the hostname from the IP address
        tgtName = gethostbyaddr(tgtIP)
        # Print the resolved hostname
        print('\n[+] Scan result of: %s' % tgtName[0])
    except:
        # If hostname resolution fails, print the IP address
        print('\n[+] Scan result of: %s' % tgtIP)

    # Set the default timeout for socket connections to 1 second
    setdefaulttimeout(1)
    # Iterate over the list of target ports to scan
    for tgtPort in tgtPorts:
        print('Scanning Port: %d' % tgtPort)  # Indicate which port is being scanned
        conScan(tgtHost, tgtPort)  # Call the connection scan function for each port

# Main block to execute the port scanning
if __name__ == '__main__':
    # Saying to start scanning specified ports (80 and 22) on google.com
    portScan('google.com', [80, 22])

# What comes out in the results is the domain name of the server that is resolved, and the results of the specified ports that got scanned
import socket  # Importing the 'socket' module which provides access to the BSD socket interface.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a socket object. AF_INET specifies the address family (IPv4), SOCK_STREAM specifies the socket type (TCP).
s.settimeout(5)  # Setting a timeout of 5 seconds for socket operations.

host = input("Please enter the IP you want to scan: ")  # Asking the user to input the IP address they want to scan.
port = int(input("Please enter the port you want to scan: "))  # Asking the user to input the port number they want to scan.

# Defining a function called portScanner that takes a port number as input.
def portScanner(port):
    # Using the connect_ex method of the socket object to check if a connection can be established to the specified host and port.
    if s.connect_ex((host, port)):
        print("The port is closed")  # If connection attempt fails, print that the port is closed.
    else:
        print("The port is open")  # If connection attempt succeeds, print that the port is open.

portScanner(port)  # Calling the portScanner function with the port number input by the user.


"""

This code performs a simple port scanning operation using Python's socket module. Here's a breakdown of its functionality:

1) Importing Required Module: The script starts by importing the socket module, which provides access to socket operations, enabling network communication.

2) Creating Socket Object: A TCP socket object (s) is created using socket.socket() function, specifying the address family (AF_INET for IPv4) and socket type (SOCK_STREAM for TCP).

3) Setting Timeout: The settimeout() method is used to set a timeout of 5 seconds for socket operations. This means that if a connection attempt takes longer than 5 seconds, it will be aborted.

4) User Input: The user is prompted to input the IP address they want to scan and the port number they want to check for openness.

5) Port Scanning Function: The portScanner() function is defined, which takes a port number as input.

6) Connection Attempt: Inside the portScanner() function, the connect_ex() method of the socket object (s) is used to attempt to establish a connection to the specified IP address and port. This method returns an error code. If the port is open, it returns 0; otherwise, it returns an error code indicating that the connection attempt failed.

7) Checking Connection Result: If connect_ex() returns a non-zero value, it means the connection attempt failed, and the script prints "The port is closed". If it returns 0, it means the connection attempt succeeded, and the script prints "The port is open".

8) Function Invocation: The portScanner() function is invoked with the port number entered by the user.

In summary, this code performs a basic TCP port scanning operation, where the user provides an IP address and a port number, and the script attempts to establish a TCP connection to that IP address on the specified port. It then reports whether the port is open or closed based on the success or failure of the connection attempt.

"""
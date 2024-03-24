import scapy.all as scapy  # Import the necessary modules from scapy library
import argparse  # Import the argument parsing module

def Get_Arguments():  # Define a function to get the command-line arguments
    Parser = argparse.ArgumentParser()  # Create an ArgumentParser object
    Parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")  # Add an argument to specify the target IP or IP range
    Options = Parser.parse_args()  # Parse the command-line arguments and store them in Options
    return Options  # Return the parsed options

def Scan(IP):  # Define a function to perform the network scan
    ARP_Request = scapy.ARP(pdst=IP)  # Create an ARP request packet with the target IP
    Broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Create an Ethernet frame with a broadcast MAC address
    ARP_Request_Broadcast = Broadcast/ARP_Request  # Combine the Ethernet frame and ARP request to create the complete packet
    Answered_List = scapy.srp(ARP_Request_Broadcast, timeout=1, verbose=False)[0]  # Send the ARP request and receive the response

    Clients_List = []  # Initialize an empty list to store the results
    for Element in Answered_List:  # Iterate over each element in the response list
        Client_Dict = {"IP": Element[1].psrc, "MAC": Element[1].hwsrc}  # Create a dictionary to store IP and MAC addresses
        Clients_List.append(Client_Dict)  # Append the dictionary to the results list
    return Clients_List  # Return the list of clients

def Print_Result(Results_List):  # Define a function to print the scan results
    print("IP\t\t\tMAC Address\n------------------------------------------")  # Print header for the result table
    for Client in Results_List:  # Iterate over each client in the results list
        print(Client["IP"] + "\t\t" + Client["MAC"])  # Print the IP and MAC address of each client

Options = Get_Arguments()  # Get the command-line arguments
Scan_Result = Scan(Options.target)  # Perform the network scan with the specified target
Print_Result(Scan_Result)  # Print the scan results



"""

This code performs the following steps:

1) Imports:

scapy.all: Imports the entire scapy library for network scanning.
argparse: Imports the module for parsing command-line arguments.

2) Get_Arguments() function:

Creates an ArgumentParser object to handle command-line arguments.
Adds an argument -t or --target to specify the target IP or IP range.
Parses the command-line arguments and returns the parsed options.

3) Scan(IP) function:

Constructs an ARP request packet for the specified IP.
Creates an Ethernet frame with a broadcast MAC address.
Combines the ARP request packet and the Ethernet frame to form the complete packet.
Sends the packet and receives the response.
Extracts IP and MAC addresses from the response and stores them in a list of dictionaries.
Returns the list of dictionaries containing IP and MAC addresses of the discovered devices.

4) Print_Result(Results_List) function:

Prints a formatted table header for the scan results.
Iterates over each client in the results list.
Prints the IP and MAC address of each client in the specified format.

5) Parsing Command-Line Arguments:

Calls the Get_Arguments() function to parse command-line arguments.
Stores the parsed options in the Options variable.

6) Performing the Network Scan:

Calls the Scan(IP) function with the target IP or IP range obtained from the parsed options.
Stores the scan results in the Scan_Result variable.

7) Printing the Scan Results:

Calls the Print_Result(Results_List) function to print the scan results.
Passes the list of scan results (Scan_Result) as an argument to the printing function.

"""
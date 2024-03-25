import nmap  # Import the nmap library

# Create a new PortScanner object
Scanner = nmap.PortScanner()

# Print welcome message
print("Welcome, This is a Nmap Scanner Tool")
print("<----------------------------------------------------->")

# Prompt user to input the IP address they want to scan
IP_Addr = input("Please Enter the IP Address you want to Scan: ")
print("The IP you Entered is: ", IP_Addr)  # Print the IP address entered by the user
type(IP_Addr)  # This line doesn't do anything, as it doesn't assign the result to a variable

# Prompt user to select the type of scan
Resp = input("""\nPlease enter the type of scan you want to run (e.g '0'):
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan \n""")
print("You have selected option: ", Resp)  # Print the selected option

# Define a dictionary mapping scan options to corresponding Nmap commands and protocols
Resp_Dict = {'1': ['-v -sS', 'TCP'], '2': ['-v -sU', 'UDP'], '3': ['-v -sS -sV -sC -A -O', 'TCP']}

# Check user's selection and execute the corresponding scan
if Resp == '1':  # If user selected SYN ACK Scan
    print("Nmap Version: ", Scanner.nmap_version())  # Print the Nmap version
    Scanner.scan(IP_Addr, '1-1024', '-v -sS')  # Perform SYN ACK scan
    print(Scanner.scaninfo())  # Print scan information
    print("IP Status: ", Scanner[IP_Addr].state())  # Print IP status
    print(Scanner[IP_Addr].all_protocols())  # Print protocols detected
    if 'tcp' in Scanner[IP_Addr]:  # Check if TCP ports are open
        print("Open Ports: ", Scanner[IP_Addr]['tcp'].keys())  # Print open TCP ports
    else:
        print("No open TCP ports found.")  # Print if no open TCP ports are found

elif Resp == '2':  # If user selected UDP Scan
    print("Nmap Version: ", Scanner.nmap_version())  # Print the Nmap version
    Scanner.scan(IP_Addr, '1-1024', '-v -sU')  # Perform UDP scan
    print(Scanner.scaninfo())  # Print scan information
    print("IP Status: ", Scanner[IP_Addr].state())  # Print IP status
    print(Scanner[IP_Addr].all_protocols())  # Print protocols detected
    if 'udp' in Scanner[IP_Addr]:  # Check if UDP ports are open
        print("Open Ports: ", Scanner[IP_Addr]['udp'].keys())  # Print open UDP ports
    else:
        print("No open UDP ports found.")  # Print if no open UDP ports are found

elif Resp == '3':  # If user selected Comprehensive Scan
    print("Nmap Version: ", Scanner.nmap_version())  # Print the Nmap version
    Scanner.scan(IP_Addr, '1-1024', '-v -sS -sV -sC -A -O')  # Perform comprehensive scan
    print(Scanner.scaninfo())  # Print scan information
    print("IP Status: ", Scanner[IP_Addr].state())  # Print IP status
    print(Scanner[IP_Addr].all_protocols())  # Print protocols detected
    if 'tcp' in Scanner[IP_Addr]:  # Check if TCP ports are open
        print("Open Ports: ", Scanner[IP_Addr]['tcp'].keys())  # Print open TCP ports
    else:
        print("No open TCP ports found.")  # Print if no open TCP ports are found

elif Resp >= '4':  # If user entered an invalid option
    print("Please Enter a Valid Option")  # Print error message





"""
Explanation of what the program does:

1) Welcomes the user to the Nmap Scanner Tool.
2) Prompts the user to enter an IP address they want to scan.
3) Asks the user to select the type of scan they want to perform (SYN ACK Scan, UDP Scan, or Comprehensive Scan).
4) Depending on the user's choice, the program executes the corresponding Nmap scan command using the nmap library.
5) It prints out the scan results, including Nmap version, scan information, IP status, detected protocols, and open ports (if any).
6) If the user enters an invalid option, it displays an error message.

"""
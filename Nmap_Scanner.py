import nmap                              # This line imports the nmap library, which provides functions to interact with the Nmap security scanner.
import pyfiglet                          #  This line imports the pyfiglet library, used to create ASCII art banners.
 
Scanner = nmap.PortScanner()             # This line initializes an Nmap PortScanner object, which will be used to perform scans.
print(pyfiglet.figlet_format("NMAP SCANNER"))  # This line prints a stylized banner with the text "NMAP SCANNER" using the pyfiglet.figlet_format function.
print("<-------------------------------------------------->")

IP_Address = input("Please Enter the IP Address you want to Scan: ")   # This line prompts the user to input the IP address they want to scan and stores it in the variable IP_Address.
print("The IP you Entered is: ", IP_Address)
type(IP_Address)

Response = input(""" \nPlease Enter the type of Scan you want to run (e.g -> 0):
                     1) SYN ACK Scan
                     2) UDP Scan
                     3) Comprehensive Scan \n""")
print("You have Selected Option: ", Response)         # This line prompts the user to select the type of scan they want to perform and stores their choice in the variable Response.

if(Response == '1'):
    print("Nmap Version: ", Scanner.nmap_version())
    Scanner.scan(IP_Address, '1-1024', '-v -sT')      # The selected scan type is executed using the Scanner.scan method with appropriate parameters.
    print(Scanner.scaninfo())
    print("IP Status: ", Scanner[IP_Address].state())
    print(Scanner[IP_Address].all_protocols())
    print("Open Ports: ", Scanner[IP_Address]['tcp'].keys())

elif(Response == '2'):
    print("Nmap Version: ", Scanner.nmap_version())
    Scanner.scan(IP_Address, '1-1024', '-v -sU')
    print(Scanner.scaninfo())
    print("IP Status: ", Scanner[IP_Address].state())
    print(Scanner[IP_Address].all_protocols())
    print("Open Ports: ", Scanner[IP_Address]['udp'].keys())

elif(Response == '3'):
    print("Nmap Version: ", Scanner.nmap_version())
    Scanner.scan(IP_Address, '1-1024', '-v -sS -sV -sC -A -O')
    print(Scanner.scaninfo())
    print("IP Status: ", Scanner[IP_Address].state())
    print(Scanner[IP_Address].all_protocols())
    print("Open Ports: ", Scanner[IP_Address]['tcp'].keys())

elif(Response >= '4'):
    print("Please Enter a Valid Option")        # The script includes error handling to ensure that the user inputs a valid option for the scan type.

import subprocess  # Importing the subprocess module to run shell commands.
import optparse    # Importing the optparse module to parse command-line arguments.
import re          # Importing the re module for regular expressions.

def Get_Arguments():  # Defining a function to get command-line arguments.
    Parser = optparse.OptionParser()  # Creating a command-line argument parser.

    # Adding options for interface and new MAC address.
    Parser.add_option("-i", "--interface", dest="Interface", help="Interface to change its MAC Address")
    Parser.add_option("-m", "--mac", dest="New_MAC", help="New MAC Address")

    # Parsing command-line arguments.
    (options, arguments) = Parser.parse_args()

    # Checking if required arguments are provided.
    if not options.Interface:  
        Parser.error("[-] Please specify the correct interface using -i or --interface, use --help for more information.")
    elif not options.New_MAC:
        Parser.error("[-] Please specify the correct new MAC address using -m or --mac, use --help for more information.")
    else:
        return options  # Returning parsed options.

def Change_MAC(Interface, New_MAC):  # Defining a function to change MAC address.
    print("[+] Changing MAC Address for " + Interface + " to " + New_MAC)  # Printing a message indicating MAC address change.

    # Running shell commands to bring the interface down, set new MAC address, and bring the interface back up.
    subprocess.call(['ifconfig', Interface, 'down'])
    subprocess.call(['ifconfig', Interface, 'hw', 'ether', New_MAC])
    subprocess.call(['ifconfig', Interface, 'up'])

def Get_Current_MAC(Interface):  # Defining a function to get the current MAC address.
    # Running ifconfig command to get interface information.
    Ifconfig_Result = subprocess.check_output(['ifconfig', Interface]).decode('utf-8')

    # Printing ifconfig result.
    print(Ifconfig_Result)

    # Using regular expression to search for MAC address pattern in ifconfig result.
    MAC_Address_Search_Result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Ifconfig_Result)

    # Checking if MAC address is found.
    if MAC_Address_Search_Result:
        return MAC_Address_Search_Result.group(0)  # Returning the found MAC address.
    else:
        print("[-] Could not read MAC Address.")  # Printing a message if MAC address is not found.

options = Get_Arguments()  # Parsing command-line arguments.
Current_MAC = Get_Current_MAC(options.Interface)  # Getting the current MAC address.
print("Current MAC = " + str(Current_MAC))  # Printing the current MAC address.

Change_MAC(options.Interface, options.New_MAC)  # Changing the MAC address.
Current_MAC = Get_Current_MAC(options.Interface)  # Getting the current MAC address again.

# Checking if MAC address was successfully changed.
if Current_MAC == options.New_MAC:
    print("[+] MAC Address was changed to " + Current_MAC + " successfully!")  # Printing success message.
else:
    print("[-] MAC Address did not get changed.")  # Printing failure message if MAC address was not changed.



"""
This code performs the following steps:

1) Import necessary modules:

subprocess: Allows running shell commands.
optparse: Helps in parsing command-line arguments.
re: Provides support for regular expressions.

2) Define function to get command-line arguments:

This function (Get_Arguments()) sets up an argument parser.
It adds options for the interface (-i or --interface) and new MAC address (-m or --mac).
Then, it parses the command-line arguments provided by the user.
It checks if both required arguments (interface and new MAC address) are provided. If not, it raises an error.

3) Define function to change MAC address:

This function (Change_MAC(Interface, New_MAC)) prints a message indicating the MAC address change.
It then runs shell commands to bring the specified interface down, set the new MAC address, and bring the interface back up.

4) Define function to get the current MAC address:

This function (Get_Current_MAC(Interface)) gets the current MAC address of the specified interface.
It runs the ifconfig command to retrieve interface information.
Then, it searches for the MAC address pattern within the ifconfig result using a regular expression.
If found, it returns the MAC address; otherwise, it prints a message indicating that the MAC address couldn't be read.

5) Parse command-line arguments and get the current MAC address:

It parses the command-line arguments using the Get_Arguments() function.
Then, it gets the current MAC address using the Get_Current_MAC() function and prints it.

6) Change the MAC address:

It calls the Change_MAC() function to change the MAC address of the specified interface to the new MAC address provided by the user.

7) Get the current MAC address again and check if it's changed:

It gets the current MAC address again after the change using the Get_Current_MAC() function.
If the current MAC address matches the new MAC address provided by the user, it prints a success message; otherwise, it prints a failure message.


"""
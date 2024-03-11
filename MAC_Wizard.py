import subprocess      #importing subprocess module
import pyfiglet        # pyfiglet is for design banner

print(pyfiglet.figlet_format("MAC Wizard"))
Interface = input("Enter the Interface: ")     # Getting the Input of Network Interface
New_MAC = input("Enter the New MAC Address: ") # Getting the Input of New MAC Address 
print(pyfiglet.figlet_format("Changing MAC Address "+ Interface +" to "+New_MAC+"..."))   #Notifying the user that the MAC Address is changing
#print("Changing MAC Address "+ Interface +" to "+New_MAC+"...")   

#subprocess.call("ifconfig "+ Interface + " down", shell=True)
#subprocess.call("ifconfig "+ Interface + " hw ether " + New_MAC, shell=True)  #Note: THIS METHOD IS A SECURITY HAZARD. SO IT IS BETTER TO USE THE BELOW METHOD, WHERE WE ARE USING LIST.
#subprocess.call("ifconfig "+ Interface + " up", shell=True)

subprocess.call(["ifconfig", Interface, "down"])                    # Switching off the Interface
subprocess.call(["ifconfig", Interface, "hw", "ether", New_MAC])    # Changing the MAC Address
subprocess.call(["ifconfig", Interface, "up"])                      # Switching On the Interface with the New MAC Address
print(pyfiglet.figlet_format("MAC Address Changed Successfully!"))
#print("MAC Address Changed Successfully!")
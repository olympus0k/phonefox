from pyfiglet import Figlet
from termcolor import colored
import os
import time,sys
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

f = Figlet(font='5lineoblique')

msg=(colored('''
██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗███████╗░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝██╔════╝██╔══██╗╚██╗██╔╝
██████╔╝███████║██║░░██║██╔██╗██║█████╗░░█████╗░░██║░░██║░╚███╔╝░
██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░██╔══╝░░██║░░██║░██╔██╗░
██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗██║░░░░░╚█████╔╝██╔╝╚██╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝
    \n''',color = 'green'))


for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)


print('''=================================================-
              made by tolt 
              i am not responsable for the bad use of this tool
              ======================================================''' )

 
c = colored("\n\nTO CONFIRM YOU WANT TO START THIS TOOL ENETER =Y IF NOT ENTER=N (y/n) = ", color = 'green')
d = input(c).lower()
if d == "y":
	b = (colored("Time Zone = ",color = 'cyan'))
	ae1 = input("\n\nenter the phone number to scan with + and country code: ")

	phone_number = phonenumbers.parse(ae1)
	os. system('clear')
	print(colored("Phone Number = " + ae1,color = 'cyan'))
	print(("Country = ") + geocoder.	description_for_number (phone_number, "en"))
	print(("Carrier = ") + carrier.name_for_number (phone_number, "en"))
	timeZone = timezone.time_zones_for_number(phone_number)
	print(b , timeZone)
	
elif d == "n":
	print(colored("\n\nexit tool",color = 'yellow'))
	exit
else:
	print(colored("\n\nsorry cant do that",color = 'green'))
	exit
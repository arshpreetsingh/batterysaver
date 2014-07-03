"""
%%% battery.py %%%

"""

########################## Header Files ########################################
import os
import sys
import time
import acpi
import re
import webbrowser

################################################################################
def limitcheck():
	"""
	limitcheck checks the battery status between scale of 40 and 80. It warns 
	the user to charge the system if battery status is less than 40 and asks the 
	user to unplug the charger when system battery is more than 80.
	"""
	a=acpi.acpi();
	print a;
	c=str(acpi.acpi());
	b=a[0][2];
	print b;
	
	match1=re.search(r'Charging',c);
	match2=re.search(r'Discharcharging',c);		
	if(b>=80):
		if match1:
			print "Remove AC";
			webbrowser.open('http://arshpreetsingh.wordpress.com/');	
			time.sleep(200);
			limitcheck();
		else:
			time.sleep(3000);
			limitcheck();
	elif(b<=40):
		if match1:
			time.sleep(5400);
		else:
			print "You need Charging, Please plug in the Charger";
			webbrowser.open('http://arshpreetsingh.wordpress.com/');
			time.sleep(200);
			limitcheck();
	else:
		print "You are running Safe";
		time.sleep(900);
		limitcheck();
		
limitcheck();

######################## TaDaa... Thank you ####################################

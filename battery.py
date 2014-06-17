import os
import sys
import time
import acpi
import re
import webbrowser
		
def limitcheck():
	
	a=acpi.acpi();
	print a;
	c=str(acpi.acpi());
	b=a[0][2];
	print b;
	
	match1=re.search(r'Charging',c); #ethe fer patteren matching vich galti aa rhi aaa oh discharging nu vi charging samaj riha haii.
	match2=re.search(r'Discharcharging',c);		
	if(b>=80):
		if match1:
			print "remove ac";
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
			print"you need charging";
			webbrowser.open('http://arshpreetsingh.wordpress.com/');
			time.sleep(200);
			limitcheck();
	else:
		print "you are running safe";
		time.sleep(900);
		limitcheck();
limitcheck();
#there is one thing. time should be configurable but how? we should made a formula to test how much time it takes to charge or
#discharge battery by 2% so make a formula that counts it first then put those values in the configured time. :D
#so before running the actual script user have to run a test script which will tell the user that what should be the 
#values of your time.sleep in 25th,29th,and 37th value. and ceate a phenomenon which will put values in the script automatically
#completely automation. :D :D

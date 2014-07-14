import os
import acpi
import re
import timeit
import time
import sys
##my future is in python programmer 
print "plug in your charger we will run a test script to check your battery timings.. really?? yes and follow the instructions";
def fxn():
	print "Now plugin your cahrger";
	print"please press enter if you have plugged in";
	##oh function labho jisde vich jado takk user enter press na kare program agge na challe
	try:
		input("Press enter to continue");
	except SyntaxError:
		pass;
	a=acpi.acpi();
	print a;
	b=a[0][2];
	print "checking";
	time.sleep(10);	
	c=acpi.acpi();
	d=c[0][2];

	if(d>b):
		e=d-b;
		print c;
		print e;
		fxn2();
	else:
		fxn();
					
fxn();
##ethe jhda fxn2 define kitta hoya usnu globaly defie karna hai and haan je global define karna galt hai tan koi dosri option
##vi hor esnu kis tareeke naal use kar sakde aan
def fxn2():
	print "Now plugin your cahrger";
	print"please press enter if you have plugged in";
	##oh function labho jisde vich jado takk user enter press na kare program agge na challe
	
	a2=acpi.acpi();
	print a2;
	b2=a2[0][2];
	print "checking";
	time.sleep(10);	
	c2=acpi.acpi();
	d2=c2[0][2];

	if(d2>b2):
		e2=d2-b2;
		print c2;
		print e2;
	else:
		fxn2();
		
#hun main net ton eh dekhna hai vi eh function challe nu 
#kinna time lagea.
#fer oh time hovega vi 1% battery nucharge karn vaaste lagea time
#us time nu apan agge kive use karna hai???
#umumumumumumumumumumumumumumumumumumumumumumum
#jiven mainu 100 seconds lagge ne 1% charging vaaste
#1% vaaste 100 seconds
#40-x vaaste (40-x)X100seconds----->>> oh hovga sleeptime

import time
import acpi
import timeit

#oh time calculate karna hai us vaaste net te function dekhna hai vi kehda hovega..........................
def fxn2():
	
	##fer ohi code enter hit hon te agge challan wala
	
	e=acpi.acpi();
	print e;
	f=e[0][2];
	print "checking";
	time.sleep(10);	
	j=acpi.acpi();
	k=j[0][2];

	if(k<f):
		g=k-f;
		print k;
		print f;
		print g;
		timetaken = timeit.timeit(fxn2);
		print timetaken;
	else:
		fxn2();

try:
	input("Press Enter to continue");
except SyntaxError:
	pass;	
fxn2();


###%%% battery2.py %%%
import acpi
import re
import sys
def limitcheck():

	"""   limitcheck checks the battery status between 
              scale of 40 and 80. """
	a=acpi.acpi();
        print a;
        c=str(acpi.acpi());
        b=a[0][2];
        print b;

        match1=re.search(r'Charging',c);
        match2=re.search(r'Discharging',c);

	if(b>=80):
                if match1:
                        print "Remove AC";
                        
                       	
	if(b<=40):
		if match2:
			print "Connecet AC";
			
			
limitcheck();		

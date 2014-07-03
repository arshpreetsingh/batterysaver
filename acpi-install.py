"""
%%% acpi-install.py %%%
This file is used to check whether the system has acpi package or not. If it 
does not fine the package, it is installed.
"""

########################## Header Files ########################################
import os
from sys import platform as _platform
import platform
import urllib2
################################################################################

def check_connectivity():
	"""This function checks the connectivity to internet"""
    try:
        urllib2.urlopen('http://www.google.com',timeout=2)
        return True
    except urllib.request.URLError:
    	print("No internet connection available. Please get one to move further")
        return False
        
def install_acpi():
	"""We find the distribuion of the system and then run command to install 
	acpi if it is not installed"""
	check_connectivity()
	linux_distro = platform.linux_distribution()[0]

	try:
		__import__('acpi')
	except ImportError:
		if _platform == "linux" or _platform == "linux2":
			if linux_distro=='Ubuntu':
				os.system("sudo apt-get install acpi")
			elif linux_distro=='RedHat':
				os.system("sudo yum install acpi")
		
		# linux
		elif _platform == "darwin":
			#here we need a command to install acpi on darwin
		# OS X
		elif _platform == "win32":
			#here we need a command to install acpi on window's DOS	
		
		print "Ahaa..!! acpi module installed"
	
install_acpi();
    

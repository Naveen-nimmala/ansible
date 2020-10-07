 noinspection PyInterpreter
import  fileinput
import shutil
import re
filename = input("Enter input file:")
output_filename = input("Enter outputfilename:")
shutil.copyfile(filename, output_filename)
hostname = input("Enter the new hostname to change (this will change the hostnames that starts with sg): ")
domain = input("enter the domain name to chnage(it will change the all domain name that ends with .com):")
IpAddress = input("enter the New IPAddress to change(it will change the all IP addresses in the file):")
pattern1 = r"\b\w*.*.com\b"
pattern2 = r"\bsg\w*\b"   #^sg.*$
pattern3 = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b' #^\d\w{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
for line in fileinput.input(output_filename, inplace=1): # backup=input("Taking the backup of existing file. Enter the Name:")):
    #combined_pat = r'|'.join((pattren1, pattren2))
    #line = re.sub(combined_pat, 'hellooooooooooooo', line.rstrip())
    line = re.sub(pattern1, domain, line.rstrip())
    line = re.sub(pattern2, hostname, line.rstrip())
    line = re.sub(pattern3, IpAddress, line.rstrip())
    print(line)
#combined_pat = r'|'.join((pat1, pat2))
#stripped = re.sub(combined_pat, '', s2)

# noinspe
import  fileinput,datetime
import shutil
import re
import os,sys,platform
from os import walk
directory = input("Enter directory path:")
if not os.path.exists(directory):
    print("Path is not valid")
    sys.exit()
hostname = input("Enter the new hostname to change (this will change the hostnames that starts with sg): ")
domain = input("enter the domain name to chnage(it will change the all domain name that ends with .com):")
IpAddress = input("enter the New IPAddress to change(it will change the all IP addresses in the file):")
pattern1 = r"\b\w*.*.com\b"
pattern2 = r"\b[Ss][Gg]\w*\b"   #^sg.*$
pattern3 = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b' #^\d\w{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

date1 = datetime.date.today()
sec = datetime.datetime.now()
time = sec.strftime("%X")

date = str(date1)+"_"+str(time)
print(date)
filenames = []
for (dirpath, dirnames, filename) in walk(directory):
        filenames.extend(filename)
        break

os_version = platform.system()

# for file in filenames:
    # print(file)
    # output_filename = str(file) + str(count)
    # os.chdir(directory)
    # shutil.copyfile(file, output_filename)
    # count = count + 1
os.chdir(directory)
name = "Output_Dir"+"_"+str(date1)
newdir = os.path.join(directory, name)
if not os.path.exists(newdir):
    os.makedirs(newdir)
print(newdir)
for filenamee in filenames:
    output_filename = str(filenamee)+"_"+str(date)
    if os_version == "Windows":
        destination = str(newdir)+"\\"+str(output_filename)
    else:
        destination = str(newdir)+"/"+str(output_filename)

    print(destination)
    shutil.copyfile(filenamee, destination)
    os.chdir(newdir)
    for line in fileinput.input(output_filename, inplace=1): # backup=input("Taking the backup of existing file. Enter the Name:")):
        #combined_pat = r'|'.join((pattren1, pattren2))
        #line = re.sub(combined_pat, 'hellooooooooooooo', line.rstrip())
        line = re.sub(pattern1, domain, line.rstrip())
        line = re.sub(pattern2, hostname, line.rstrip())
        line = re.sub(pattern3, IpAddress, line.rstrip())
        print(line)
        os.chdir(directory)
        #combined_pat = r'|'.join((pat1, pat2))
        #stripped = re.sub(combined_pat, '', s2)

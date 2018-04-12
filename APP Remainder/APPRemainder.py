import subprocess,re;

temp = subprocess.call("bx target -o chinkul3@in.ibm.com -s dev");

result  = subprocess.check_output("bx app list");
result = str(result);

file = open("names","r");
file = file.read().split("\n");    
records = dict();   
                    
def checkOwner(line):
    for name in file:
        if name in line:
            print line;
            break;

for line in result.splitlines():
   checkOwner(line.lower());
        








import re;

f = open("country.txt","r");

"""
myDi = {}
for line in f:
     language =  line.split(",")[-1].rstrip();
     if myDi.has_key(language):
          myDi[language] += 1;
     else:                                                                               
          myDi[language]=1;

print myDi;
f.close();
"""

"""
myDi = {};
mylist = [];
for line in f:
     newline = line.split(",")[4].rstrip();
     newLine = re.sub("\d+","",newline);
    
     if myDi.has_key(newLine):
          mylist = myDi.get(newLine);
          mylist.append(line.split(",")[0]);
     else:
          mylist.append(line.split(",")[0]);
          myDi[newLine]=mylist;

     mylist = [];        

for line in myDi:
     print line,myDi[line];
"""





     
     



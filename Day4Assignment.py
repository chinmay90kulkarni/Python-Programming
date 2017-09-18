try:
     splitter = [];
     langstat = {};
     f = open("country.txt","r");
     for line in f:
          splitter = line.split(",")[-1].rstrip();
          if(langstat.has_key(splitter)):
               langstat[splitter] +=1;
          else:
               langstat[splitter] =1;
     print langstat;     

     for i in langstat:
          print i;

except Exception as a:
     print a;
     

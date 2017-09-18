try:
     f = open("emp.txt","r");
     global temp;
     temp = [];
     for line in f:
          if (len(line) >0):
               temp  = line.split(":");
               newSal = int(line.split(":")[-1]) + 15000;
               temp[-1] = str(newSal);
               temp += temp; 
          else:
               break;
                     
except Exception as a:
     print a;

finally:
     f.close();



try:
     f = open("emp.txt","w");
     for line in temp:
          if (len(line) >0):
               f.write(line);
               
          else:
               break;
                     
except Exception as a:
     print a;

finally:
     f.close();










#!/usr/bin/python3
import requests
import sys

def check_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                 return False
        else:
            return True
    else:
        return False

# get 0 start day and month
def gen_code1(username,year,endyear,option):
    options=2
    if(option ==1): options=0
    for i in range (year,endyear+1):
        for j in range(1,13):
            # month
            if (j==2) :  
                #check leap year
                if (check_leap_year(i)):
                    for k in range (1,30):
                        if k<10 :
                            print(username+"0"+str(k)+"0"+str(j)+str(i)[options:])
                            #else: print(username+str(k)+str(j)+str(i)[options:])
                        else: 
                            print(username+str(k)+"0"+str(j)+str(i)[options:])
                            #else: print(username+str(k)+str(j)+str(i)[options:])
                else :
                    for k in range (1,29):
                        if k<10 : print(username+"0"+str(k)+"0"+str(j)+str(i)[options:])
                        else: print(username+str(k)+"0"+str(j)+str(i)[options:])

            elif (j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12):
                for k in range (1,32):
                    if k<10 :
                            if j<10: print(username+"0"+str(k)+"0"+str(j)+str(i)[options:])
                            else: print(username+"0"+str(k)+str(j)+str(i)[options:])
                    else: 
                            if j<10: print(username+str(k)+"0"+str(j)+str(i)[options:])
                            else: print(username+str(k)+str(j)+str(i)[options:])
            else :
                for k in range (1,31):
                    if k<10 :
                            if j<10: print(username+"0"+str(k)+"0"+str(j)+str(i)[options:])
                            else: print(username+"0"+str(k)+str(j)+str(i)[options:])
                    else: 
                            if j<10: print(username+str(k)+"0"+str(j)+str(i)[options:])
                            else: print(username+str(k)+str(j)+str(i)[options:])
           

# get not 0 start days and month
def gen_code2(username,year,endyear,option):
    options=2
    if(option ==1): options=0
    for i in range (year,endyear+1):
        for j in range(1,13):
            # month
            if (j==2) :  
                #check leap year
                if (check_leap_year(i)):
                    for k in range (1,30):
                        print(username+str(k)+str(j)+str(i)[options:])
                else :
                    for k in range (1,29):
                        print(username+str(k)+str(j)+str(i)[options:])
            elif (j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12):
                for k in range (1,32):
                    print(username+str(k)+str(j)+str(i)[options:])
            else :
                for k in range (1,31):
                    print(username+str(k)+str(j)+str(i)[options:])
# get 0 start day not month
def gen_code_last(username,year,endyear,option):
    options=2
    if(option ==1): options=0
    for i in range (year,endyear+1):
        for j in range(1,13):
            # month
            if (j==2) :  
                #check leap year
                if (check_leap_year(i)):
                    for k in range (1,30):
                        if k<10: print(username+"0"+str(k)+str(j)+str(i)[options:])
                        #else: print(username+str(k)+str(j)+str(i)[options:])
                else :
                    for k in range (1,29):
                        if k<10: print(username+"0"+str(k)+str(j)+str(i)[options:])
                        #else: print(username+str(k)+str(j)+str(i)[options:])
            elif (j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12):
                for k in range (1,32):
                    if k<10: print(username+"0"+str(k)+str(j)+str(i)[options:])
                    #else: print(username+str(k)+str(j)+str(i)[options:])
            else :
                for k in range (1,31):
                    if k<10: print(username+"0"+str(k)+str(j)+str(i)[options:])
                    #else: print(username+str(k)+str(j)+str(i)[options:])    

# get not 0 start day but in month
def gen_code_last1(username,year,endyear,option):
    options=2
    if(option ==1): options=0
    for i in range (year,endyear+1):
        for j in range(1,13):
            # month
            if (j==2) :  
                #check leap year
                if (check_leap_year(i)):
                    for k in range (1,30):
                        if j<10: print(username+str(k)+"0"+str(j)+str(i)[options:])
                        else: print(username+str(k)+str(j)+str(i)[options:])
                else :
                    for k in range (1,29):
                        if j<10: print(username+str(k)+"0"+str(j)+str(i)[options:])
                        else: print(username+str(k)+str(j)+str(i)[options:])
            elif (j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12):
                for k in range (1,32):
                    if j<10: print(username+str(k)+"0"+str(j)+str(i)[options:])
                    else: print(username+str(k)+str(j)+str(i)[options:])
            else :
                for k in range (1,31):
                    if j<10: print(username+str(k)+"0"+str(j)+str(i)[options:])
                    else: print(username+str(k)+str(j)+str(i)[options:])    
    
def gen_code_all(username,year,endyear):
    #time 1
    gen_code1(username,year,endyear,1)
    gen_code2(username,year,endyear,1)
    gen_code_last(username,year,endyear,1)
    gen_code_last(username,year,endyear,1)
    #time 2
    gen_code1(username,year,endyear,2)
    gen_code2(username,year,endyear,2)
    gen_code_last(username,year,endyear,2)
    gen_code_last(username,year,endyear,2)

def main():
    #username="long"
    #startyear=1950
    #endyear=2021
    #options=2 #get full year otherwise get two digitals in year
    if len(sys.argv) != 4:
        print ("[+] Usage: %s <username> <startyear> <endyear>" % sys.argv[0])
        print ('[+] Example: %s admin 1950 2021' % sys.argv[0])
        sys.exit(-1)
    username=sys.argv[1]
    startyear=int(sys.argv[2])
    endyear=int(sys.argv[3])
    gen_code_all(username,startyear,endyear)

if __name__ == "__main__":
    main()

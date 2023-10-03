x = 0
y = 0
m = 5
n = 3
print("Current State",(x,y))
print("Capacity",(m,n))
print("Capacity of jug",(m,n))
print("Rule 1 : Comletely Fill jug 1")
print("Rule 2 : Comletely Fill jug 2")
print("Rule 3 : Fill some water jug 2 form jug 1")
print("Rule 4 : Fill some water jug 1 form jug 2")
print("Rule 6 : Comlete water to jug 1 form jug 2")
print("Rule 7 : Comlete water to jug 2 form jug 1")
print("Rule 8 : Empty whole jug 1")
print("Rule 9 : Empty whole jug 2")
while(x!=4):
    rule=int(input("Enter the rule :"))
    if(rule==1):
        x=m;
    elif(rule==2):
        y=n;
    elif(rule==3):
        t=n-y;
        y=n;
        x-=t;
    elif(rule==4):
        t=m-x;
        x=m;
        y-=t;
    elif(rule==5):
        x+=y;
        y=0;
    elif(rule==6):
        y+=x;
        x=0;
    elif(rule==7):
        y=0;
    elif(rule==8):
        x=0;
    else:
        print("Not Exactly");
    print("jug 1 water,jug 2 water",(x,y))

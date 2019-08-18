import maxNumber
Num= maxNumber.Numberss()

print("Program : Finding Maximum Number")
iscontinue=True
lst=[]
while(iscontinue):
    inp = int(input("Enter an element for the list:"))
    lst.append(inp)
    cont = input("Do you want to continue adding items in the list? write y or Y to continue.")
    if(not(cont=='y' or cont=='Y')):
       iscontinue=False  
       
print(end="\n\n")     
print(f"Maximum nuber from your inputs is {Num.max_number(lst)}")
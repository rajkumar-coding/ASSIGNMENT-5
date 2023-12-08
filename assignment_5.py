startRange = int(input("From Range:"))
endRange = int(input("To Range:"))
n=int(input("Enter Number:"))

if (n>=startRange)and(n<=endRange) and (n%2==0):
    print("Not Wierd")
else:
    print("Wierd")
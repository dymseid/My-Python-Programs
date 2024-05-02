year = int(input("Enter a Year"))
if year%4==0:
   if year%100==0:
       if year%400==0:
            print("is a leap year")
       else:
            print("Not a leap year")
   else:
       print("is a leap year")
else:
    print("not a leap year")





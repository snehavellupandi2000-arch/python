# a = 50
# b = 21
# if (a>=18):
#     print("a is eligible for voting")
# else:
#     print("a is not eligible for voting")
# if (b>=21):
#    print("b is eligible for election participation")
#else:
#    print("b is not eligible for election participation")

age=int(input("Enter the age ")) # type casting
if(age>=21):
    print("Eligible for election participation and voting")
elif(age>=18 and age<21):
    print("Eligible for election participation and not voting")
else:
    print("Not eligible for election participation and voting")
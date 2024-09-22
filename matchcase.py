x=int(input("enter a number"))
# x is  a variable to match
match x:
    # if x is zero
    case 0:
        print("x is zero")
        # case with if condition
    case 4:
       print("case is 4")

    case _:
         print(x)
        #  if cases.............
    # case _ if x!=90:
        #  print(x,"not equal to 90")
    # case _ if x!=80:
        #  print(x,"not equal to 80")
    # case _: 
        #  print(x)

#  matchcase is use to compare variable with all patterns 
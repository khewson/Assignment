#Kim Hewson
#18/09/14
#Development exersise 4

length=int(input("Enter the length of the pool: "))
width=int(input("Enter the width of the pool: "))
deepest=int(input("Enter the depth at the deep end: "))
shallow=int(input("Enter the depth at the shallow end: "))
volume=(length*width*deepest)-(((deepest-shallow)*width*length)//2)
print("The volume of you're pool is {0}".format(volume))

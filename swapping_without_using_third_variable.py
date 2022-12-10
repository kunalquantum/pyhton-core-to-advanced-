

#accepting the values from the user (run time)
a=int(input("enter the value for the first variable :"))
b=int(input("enter the value for the second variable :"))
print("before swapping:")
print("value of a :",a)
print("value of b",b)
#(process of swapping the values)

a=a+b  #here we have added two values of a and b variable
b=a-b  # here we substract the value of b from total of a and b which returns a
a=b-a  # here we substract the value of a from toal of a and b which returns b

# priting the outputs
print("after  swapping:")
print("value of a :",a)
print("value of b :",b)







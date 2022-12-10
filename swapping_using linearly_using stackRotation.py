

#accepting the values from the user (run time)
a=int(input("enter the value for the first variable :"))
b=int(input("enter the value for the second variable :"))
print("before swapping:")
print("value of a :",a)
print("value of b",b)
#(process of swapping the values)

a,b=b,a
#here we have used the linear assignment technique of python along with stack reverse property
# priting the outputs
print("after  swapping:")
print("value of a :",a)
print("value of b :",b)







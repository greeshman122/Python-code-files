#Activtiy 1 tuples
my_tuple=()
print(my_tuple)

#Tuple with integer values
my_tuple1= (3 , 5 , 9)
print(my_tuple1)

#Tuple with mixed data types
my_tuple2= ("Bunny" , 7 , 4.5)
print(my_tuple2)

#Accessing the value of the tuple using index
print(my_tuple2[0])

#Creating a nested tuple
my_tuple3 = ("Bunny" , 2 , 55.3 , (5 , "Nun"))
print(my_tuple3)

#Accessing the value of the nested tuple using index
print(my_tuple3[3][1])

#Slicing the value of the nested tuple
print(my_tuple3[1:4])

#Iterating through a tuple
my_tuple4 = (9 , 45 , 39)
for i in my_tuple4:
    print(i)
    
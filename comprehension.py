nums=[10,20,30,40,50,60,70,80,90]
my_lis=[]
for b in nums:
        print(b)
        c=b/10
        my_lis.append(c)
        print(my_lis)
        # getting an index of an element
car_brands=["Subaru","Toyota","BMW","Peugeot","Benz"]
print(car_brands[1])
print(car_brands[3])
print(car_brands[0])
car_brands2=["Audi","Chevrolet","Ford","Honda"]
car_brands.extend(car_brands2) 
print(car_brands)
# sorting in reverse alphabetical order
car_brands.reverse()
print(car_brands)
# finding the length of an array
print(len(car_brands))
# list comprehension
w=[3,6,9,12,15,18,21,24]
x=[]
z=[a/3 for a in w]
print(z)
x.append(z)
print(x)
x.append(w)
print(x)
# operations for values in a list
squares=[z*z for z in w]
print(squares)
cubes=[q*q*q for q in w]
print(cubes)


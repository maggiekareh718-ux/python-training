students=('Alex','Mike','James','Mary','Luke')
print(type(students))
print(students)
print(students[1])

#convert a tuple to a list we use a list function
students=list(students)
print(type(students))

students[2]='kevin'
print(type(students))
#converts a list to a tuple using  a tuple function
students=tuple(students)
print(type(students))
print(students)

#add 'John' between Mary and Luke
students=list(students)
print(type(students))

students.insert(4,"John")
print(students)

students=tuple(students)
print(type(students))
print(students)

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
print(days[2])
#2. Using a function a find the length of the tuple.
print(len(days))
days=tuple(days)
print(type(days))
print(days)
#3. Replace Thursday with Thur
days=list(days) #convert to list
days(3)="Thur"#modify
print(days)
days=tuple(days)#convert to tuple
print(days)



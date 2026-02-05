def hello():
    print('hello world!')
    hello()

    #area of a triangle
    base=10
    height=12
    area=0.5*base*height
    print(area)

def area_triangle():
    base=10
    height=12
    area=0.5*base*height
    print(area)
area_triangle()

#calculate area of a circle

#without functions
pi=3.142
radius=14
area=pi*radius*radius
print(area)

#with functions
def area_circle():
    pi=3.142
    radius=14
    area=pi*radius*radius
    print(area)

area_circle()

#create a number that check if a number is even or odd
def check_number(num):
 if num%2==0:
    print('even')
 else:
    print('odd')

check_number(10)
check_number(11)

def square_number(a):
 square=a**2
 return square


def check_password(password):
   correct_password="secret123"
   if password==correct_password:
      res="Access granted"
   else:
      res="Access denied"
      return res
   
   user_input=input('Enter your password')
   res=check_password(user_input)
   print(res)
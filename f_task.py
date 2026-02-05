valid_ids=[101,102,103]
user_id=105
if user_id in valid_ids:
    print('Access Granted')
else:
    print('Access denied')

#or
if user_id in valid_ids:
    res='Access Denied'
else:
    res='Access Denied' \

print(res)


value="Joy is a girl"
if type(value)==str:
   val= 'String detected'
elif type(value)==int:
    val='Integer Detected'
else:
    val='unknown type'

print(val)

#Nested if
#=> if statements within another if statements

1.# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive

age=10
input()
2.# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."
credit_score=input('enter the credit_score:')
annual_income=input('enter the annual income:')
credit_score=float(credit_score)
if credit_score>700:
    if annual_income>50000:
        print('Loan Approved')
    else:
        print('Income requirement not met')
else:
    print('Credit score too low')

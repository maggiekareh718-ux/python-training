my_dict={
    'name':'Maggie Kareh',
    'age':17,
    'location':'Kiambu',
    'city':'Nairobi',
    'name':'David Wechanga'
}
print(my_dict)
print(type(my_dict))

#displaying values in dictionaries
print(my_dict['age'])

print(my_dict['city'])
print(my_dict['location'])

#adding new keys and values
my_dict['Occupation']='Software Developer'
my_dict['id']=5346789
print(my_dict)
#add address
my_dict['address']='P.O.BOX 229-375'
print(my_dict)


# updating values
my_dict['age']=19
print(my_dict)
#update location
my_dict['location']='Ruiru Muthaiga'
print(my_dict)

#remove items
my_name='Maggie Kareh'
print(my_name.lower())#converts strings to lowercase
print(my_name.upper())#converts strings to uppercase
print(my_name.capitalize())#converts the first letter of a name in a sentence

x="    strip method    "
print(x)
x=x.strip()
print(x)#removes spaces in strings

my_name="Maggie Kareh"
my_name=my_name.replace("Maggie","David")#repalces names
print(my_name)

x=x+' '+"alex"#the space quations adds spaces in between sentences
print(x)

#clean first name"   aLex   " to "alex"
first_name="   aLex   "
first_name=first_name.lower()
first_name=first_name.strip()
print(first_name)

#clean sentence1="    pYthoN PROGramming    "to "JAVA PROGRAMMING"
sentence1="    pYthoN PROGramming    "
sentence1=sentence1.upper()
sentence1=sentence1.strip()
sentence1=sentence1.replace("PYTHON","JAVA")
print(sentence1)

#.count=>counts the number of appearance of a character
main="Python programming" 
print(main.count("p"))
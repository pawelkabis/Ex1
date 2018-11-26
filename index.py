import datetime
now = datetime.datetime.now()
name = input("What's your name: ")
age = int(input("Hi {}, how old are you: ".format(name.title())))
year = (now.year-age) + 100

msg = "{}, you are {} years old. You will have 100 years old in  {} \n".format(name.title(), age, year)
print(msg)

copy_msg = int(input("Ok {}, lets give me some number: ".format(name.title())))
print (copy_msg * msg)
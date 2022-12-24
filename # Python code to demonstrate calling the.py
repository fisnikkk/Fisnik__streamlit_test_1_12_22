

title = input('enter a text here')

def Convert(string):
	li = list(string.split(" "))
	return li
str1 = title
print(Convert(str1))

var = Convert(title)


def all_lower(my_list):
    new_list = []
    for x in my_list:
        new_list.append(x.upper())
    return new_list
print(all_lower(var))

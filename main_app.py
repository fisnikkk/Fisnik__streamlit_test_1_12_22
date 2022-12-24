import streamlit as st

title = st.text_input('enter a text here', '')

def convert_list(string):
	li = list(string.split(" "))
	return li
if st.button('List'):
    result = convert_list(title)
    st.write('result: %s' % result)

var = convert_list(title)

def convert_lower(my_list):
    new_list = []
    for x in my_list:
        new_list.append(x.upper())
    return new_list

if st.button('Lower'):
    result1 = convert_lower(var)
    st.write('result: %s' % result1)
    
var2 = convert_lower(var)

def count(list):
    count = 0
    for element in list:
        count += 1
    return count
count(var2)

if st.button('print_count'):
    result1 = count(var2)
    st.write('result: %s' % result1)
 



    


import streamlit as st

title = st.text_input('enter a text here', '')

##########################################################
def convert_list(string):
	li = list(string.split(" "))
	return li
convert_list(title)

if st.button('List'):
    result = convert_list(title)
    st.write('result: %s' % result)
#########################################################
def convert_lower(new_list):
    new_list = []
    for x in new_list:
        new_list.append(x.upper())
        return new_list
new_list = convert_lower
convert_lower(new_list)
if st.button('Lower'):
    result1 = convert_lower(title)
    st.write('result: %s' % result1)
#########################################################
def count(list):
    count = 0
    for element in list:
        count += 1
    return count
count(title)

if st.button('print_count'):
    result1 = count(title)
    st.write('result: %s' % result1)
##########################################################    



    


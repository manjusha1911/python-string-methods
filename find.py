'''it will give the index position of a chr
including space index position also
if element not find it will print -1
we can specify the value but if we have multiole chrs it will give one first chr index position
'''

txt="my name is Manjusha naidu"
# print(txt.find(":"))
# print(txt.find("i",1,20))
'''we can give txt.index but value should be exist otherwise it will be shown as value error
we can specify start and end value'''
print(txt.index("n",4,140))
txt="Manjusha is my name"
print(txt.rindex("my"))

'''if string contains same chr multiple 
time its will print only last specified chr'''

txt="Manjusha is my name"
print(txt.rindex("e"))

'''we can specify the start and end value
if we specify the start and end value it will print
last specified chr'''

txt="My name ise manjusha"
print(txt.rindex("e",5,30))

'''if we five non exsit value it will shown as valueerror'''
txt="My name is manjusha"
print(txt.rindex("Q"))
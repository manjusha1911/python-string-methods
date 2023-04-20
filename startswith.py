txt="hello!,my name is Manjusha"
print(txt.startswith("Hello"))    #false
print(txt.startswith("hello"))    #true
print(txt.startswith("ello"))   #false
print(txt.startswith("hel"))     #true
print(txt.startswith("h"))   #true


txt="Hi!there welcome to my world."
# print(txt.startswith("!Hi",0,10))

x = txt.startswith("wel", 9, 20)
print(x)
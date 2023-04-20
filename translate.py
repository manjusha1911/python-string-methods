#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
d={83:80}
print("Hello Sam".translate(d))


a="Hello Manjusha"
b=str.maketrans("a","A")
print(a.translate(b))


txt = "Hi manjukla!"
x = "alk"
y = "ahs"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))


txt = "Good night Manjulka!"
x = "akl"
y = "ahs"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))


txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))
# txt="manjusha" false 
# txt="233" true 
# txt="23manjusha" false 
# txt="123 333"    false with space it will give false

# print(txt.isnumeric())

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())   #true
print(b.isnumeric())  #true
print(c.isnumeric())   #false
print(d.isnumeric())   #false
print(e.isnumeric())   #false
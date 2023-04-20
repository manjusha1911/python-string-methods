# it will count the specified chr

# txt="my name is manjusha , my favorite food is egg biryani"
# print(txt.count("my"))
# t=txt.count("my")
# print(t)

'''we can specify from where to where we have to count the specified chr 
there no limit for ending position
if we'll not specify the ending postion also it won't show any error''' 

txt="my name is manjusha ,my favorite dress is jeans"
print(txt.count("my",0,)) 
print(txt.count("my",10,209000))

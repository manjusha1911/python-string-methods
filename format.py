'''it will give decimal value
we have to put dot(.) otherwise extra 000's will be printed'''
# txt="my {salary:.2f} dollars!"
# print(txt.format(salary=100))

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))
# t1="my name {name},I'm {age}".format(name="manjusha",age=26)
# t2="my name{name},I'm {age}".format(name="honey",age=26)
# t3="my name{name},I'm {age}".format(name="Nany",age=10)
# print(t1)
# print(t2)
# print(t3)

#  {:<8}............... it will give left space,we have to specify the space value

# txt="I have{:<8}chickens"
# print(txt.format(49))

#  {:>8}............... it will give right space,we have to specify the space value
# tx="I have{:>8}chickens"
# print(tx.format(49))

# {:^8} it will give center allign....

# txt="i have {:^8} chichens"
# print(txt.format(48))

# {:=5} left most position.......

# txt="i have {:=8}chickns"
# print(txt.format(48))

# {:+5}.................

# txt = "The temperature is between {:} and {:+} degrees celsius."
# print(txt.format(-3,7))

# {:5}..............

# txt = "The temperature is between {:-8} and {:+} degrees celsius."
# print(txt.format(-3,7))
# txt = "The temperature is between {:-} and {:+} degrees celsius."
# print(txt.format(-3,7))

# {:}.........................

# txt = "The temperature is between {: } and {: } degrees celsius."
# print(txt.format(-3, 7))

# {:,}..........................

txt = "The universe is {:,} years old."
print(txt.format(13800000000))


# txt="I have{:}chickens"
# print(txt.format(49))



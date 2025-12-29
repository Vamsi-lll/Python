""" count the number of chemicals in the word or sentance"""
""" ------------------------------------  approach 2----------------------------------- """
stri="Hello world"
count=0
for i in stri:
  if i.lower() in "aeiou":
    count+=1
print(count)



""" ------------------------------------  approach 2----------------------------------- """
print(sum(ch.lower() in "aeiou" for ch in stri))

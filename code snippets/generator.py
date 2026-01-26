# what is a generator 
# - A generator is a special type of function that uses the yield keyword instead of return

def my_generator():
    yield 1
    yield 2
    
print(my_generator())    # this will return the generator object some thing like <generator object my_generator at 0x000002854F555C70>
# but how can i get value the generator function giving
# inorder to get the value which the generator function giving we need to use the next() function

print(next(my_generator())) # but this is giving the value 1 now how can i get the second value 
print(next(my_generator())) # simple use the code snippet again

#  thats cool i can write the code for 2 time and if needed 10 time but what if the generator function giving 100 values i couldint write the 100 time right 
#  yes that is correct and as i told you before we can loop through the generator object we can use this 

my_generator_var=my_generator()

for i in my_generator_var:
    print(i)

# this is how the generator function works and how we can loop through it 

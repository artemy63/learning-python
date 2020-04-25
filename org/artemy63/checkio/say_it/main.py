def say_hi(name, age):
    """
        Hi!
    """
    # return "Hi. My name is " + name + " and I'm " + str(age) + " years old"
    return f"Hi. My name is {name} and I'm {age} years old"


print(say_hi("Alex", 32))
assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
print('Done. Time to Check.')
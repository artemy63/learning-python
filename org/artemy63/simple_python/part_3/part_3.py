# will be splitted by symbols cause a string is just a sequence of symbols
print(list("string to be splitted"))

# will be splitted
print("a/b//c/d//e".split('//'))

# get second element of list (index == 1 cause first element has 0 index)
print(["a", "b", "c", "d"][1])

# get lsat element
print(["a", "b", "c", "d"][-1])

# lists are mutable
mutable_list = ["first", "second", "third", "fourth"]
mutable_list[3] = "4th"
print(mutable_list)

# get slice of list
print(mutable_list[1:3])

# get slice of list start from the end (shift is -1)
print(mutable_list[-2::-1])

# append to list in the end
mutable_list.append("fifth")
print(mutable_list)

# extend existing list with new one
mutable_list2 = ["6th", "seventh"]
mutable_list2.extend(mutable_list)
print(mutable_list2)

# insert into list with specified index
mutable_list.insert(0, "zero")
print(mutable_list)

# deletion of element by index
del mutable_list[0]
print(mutable_list)

# deletion of element by value
mutable_list.append("6th")
mutable_list.remove("6th")
print(mutable_list)

# get and delete element simultaneously
print("deleted last", mutable_list.pop())
print("deleted by index", mutable_list.pop(-2))
print("changed list", mutable_list)

# define index of element
print("index of existing element", mutable_list.index("second"))
# ValueError: 'not_exist' is not in list
# print("index of non-existing element", mutable_list.index("not_exist"))

# define if element in list
print("is 'second' in list", "second" in mutable_list)
print("is 'blablabla' in list", "blablabla" in mutable_list)

# join element into one string
print("joined", ', '.join(mutable_list2))


# tuples
tttuple = ('artem', 'timoffey', 'timoha')
print(tttuple)

# unpack tuple
a, b, c = tttuple
print(b)
# too many values to unpack
# a, b = tttuple
# need more value to unpack
# a, b, c, d = tttuple

str_to_change = "it comes firstly"
str_to_change_2 = "it should be second"
# will change two stings without 3rd variable
str_to_change, str_to_change_2 = str_to_change_2, str_to_change
print("str_to_change", str_to_change, "str_to_change_2", str_to_change_2)

expected_statuses = {'COMPLETED'}
print("expected_statuses ", expected_statuses.__class__)

triggered_statuses = {'STARTING', 'PROCESSING', 'COMPLETED'}
print("triggered_statuses ", triggered_statuses.__class__)

bb = 'COMPLETED' in triggered_statuses
print('bb', bb)



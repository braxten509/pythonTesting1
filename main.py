names = ["Jimmethy", "James", "John"]

for each in names:
    print(each)

# the reason you have to use "range" instead of just "len" is because a for loop
# only accepts lists, and "len" outputs an "int," not list!
for each in range(len(names)):
    print(names[each])

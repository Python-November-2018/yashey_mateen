# 1. Remember things
    # variables
    # databases
    # functions
    # databases
# 2. Math/Logic/Conditionals
    # arithmetic
    # if-else-else
    # comparisons == is not <= >= > <
# 3. Loops
    # while
    # for
# 4. Bonus
    # print()
    # comments;


my_float = 1.2
my_int = 10
my_list = [1,2,3]
my bool = False
None
my_string = 'hello world'
my dict = {
    'key': 'value',
    'other': 1
}

my_tuple= {1,2,3,4}
print(my_tuple[0])
my_tuple[0] = 2


print(my_int + my_string)
# --> In javascript, this wouldn't work but in python it does

print(type(my_float))
print(instance(my_float, float))

def my_function():
    print('hello')


my_function()

if 2 == 2:
    print("yep")
else:
    print('nope')

# Loops

my_list=[1,2,3,4]
for value in my_list:
    print(value)
#value at each index of the list

for i in range(0,100,1):
    print(i)

for i in range(0, len(my_list), 1):
    print(i)

# for loops create new lists/arrays so it's better to use while

i = 0
while i < 100:
    print(i)
    i += 1




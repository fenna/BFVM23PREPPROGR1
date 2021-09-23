
# Q1
print("Question1") 
number_as_string = input("give a number: ")
number = int(number_as_string)

if number %2 ==0:
	print("even")
else:
	print("odd")
    
# Q2
print("Question2") 
that_list = [1, 2, 6, 3, 7, 4, 8, 9, 0]
for number in that_list:
    if number > 5:
        print(number)

# Q2_extra1
print("Question2 extra 1") 
that_list = [1, 2, 6, 3, 7, 4, 8, 9, 0]
new_list = []
for number in that_list:
    if number > 5:
        new_list.append(number)

print(new_list)

# Q2_extra2
print("Question2 extra 2")
asked_number = int(input("give me a number: "))

that_list = [1, 2, 6, 3, 7, 4, 8, 9, 0]
new_list = []
for number in that_list:
    if number > asked_number:
        new_list.append(number)

print(new_list) 


# Q3
print("Question3")
ask_string = input("Give me a sequence: ")
reversed_sequence = ask_string[::-1]

if ask_string == reversed_sequence:
    print("Found palindrome")
    

# Q4
print("Question4")
x = [1,2,3,4]
new_list = [x[0], x[-1]]

print("Old list: ", x)
print("New list: ", new_list)


# Q5
print("Question5")
x = [1,2,3,4,4,5,6,7,7]
y = set(x)
x = y

print("x: ", x) 
print("Unique x: ", x) 

# OR
new_list = []
x = [1,2,3,4,4,5,6,7,7]
for i in x:
    if i not in new_list:
        new_list.append(i)

print("x: ", x) 
print("Unique x: ", new_list) 


# Q6
print("Question6")
asked_sentence = input("Give me a line of text: ")
split_string_list = asked_sentence.split(" ")
reversed_split_string_list = split_string_list[::-1]

reversed_string = " ".join(reversed_split_string_list)
print(reversed_string)


# Q7
print("Question7")
x = [1,2,3,4,4,5,6,7,7]

my_count_dict = {}

for i in x:
    if i in my_count_dict:
        my_count_dict[i] += 1
    else:
        my_count_dict[i] = 1

print(my_count_dict)

# Q8
print("Question8")
list_with_tuples = [(), (), ("",), ("A", "B"), ("a", "b", "c"), ("d",), ()]
expected_output = [("",), ("A", "B"), ("a", "b", "c"), ("d",)]

output_list = []

for tuple_placeholder in list_with_tuples:
    if len(tuple_placeholder) != 0:
        output_list.append(tuple_placeholder)

if output_list == expected_output:
    print("same")
else:
    print("Not the same")


# Q9
print("Question9")
example_list1 = [1, 3, 5, 7, 9, 10]
example_list2 = [2, 4, 6, 8]
example_list = example_list1[:-1] + example_list2
print(example_list)



# Q10
print("Question10")

example_list = [1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks'], {"Python": "Awesome"}]
dict_with_lists = {}

for item in example_list:
    str_type = str(type(item))
    
    if str_type in dict_with_lists:
         dict_with_lists[str_type].append(item)
    else:
         dict_with_lists[str_type] = [item]
         
print(dict_with_lists)


# Q11
print("Question11")
asked = input("Please give your name and your age: ")
splitted_asked = asked.split(" ")
name = splitted_asked[0]
age = splitted_asked[1]
my_dict = {name:age}
print(my_dict)


# Q12
print("Question12")
d = {"Students": "start practicing ;-)"}

asked = input("Ask anything: ")


if d.get(asked) != None:
    print(d[asked])
else:
    d[asked] = ""
    
print(d)

# Q13
print("Question13")

test_dict = {1: "A", 2: "B", 3: "C", 4: "D"}

for key, value in test_dict.items():
    print("key = ", key, "value = ", value)
    
    
# OR
for key in test_dict.keys():
    print("key = ", key, "value = ", test_dict[key])

# Q14
print("Question14")
example_dictionary = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}] 

count_number_success = 0
for this_dict in example_dictionary:
    if this_dict.get("success") == True:
        count_number_success += 1

print("counted: ", count_number_success)

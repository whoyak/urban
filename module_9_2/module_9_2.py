first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [len(length) for length in first_strings if len(length)>5]

second_result = [(first,second) for first in first_strings for second in second_strings if len(first) == len(second)]
third = [*first_strings,*second_result]
third_result = {thirds:len(thirds) for  thirds in third if len(thirds)%2 ==0}
print(first_result)
print(second_result)
print(third_result)







def calculate_sum(data):
    sum = 0
    def recursive_sum(i):
        nonlocal sum
        if isinstance(i,int):
            sum += i
        elif isinstance(i,str):
            sum +=len(i)
        elif isinstance(i,dict):
            for key,value in i.items():
                recursive_sum(key)
                recursive_sum(value)
        elif isinstance(i,(list,tuple,set)):
            for item in i:
                recursive_sum(item)
    recursive_sum(data)
    return sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_sum(data_structure))


calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    count_calls()
    return (length, upper, lower)

def is_contains(string,list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
    return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) 
print(is_contains('cycle', ['recycling', 'cyclic'])) 
print(calls)

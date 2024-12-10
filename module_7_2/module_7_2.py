def custom_write(file_name:str,strings=None):
    file = open(file_name,'a', encoding='utf-8')
    strings_positions = {}
    i=0
    for string in strings:
        tell = file.tell()
        file.write(f'{string}\n')
        i +=1
        strings_positions[(i, tell)] = string
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


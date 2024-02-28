#ex1
import re

def match_pattern(text):
    pattern = r'a*b*'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False


strings = ['ab', 'abb', 'aabb', 'b', 'a', 'abab', 'aabbb']
for string in strings:
    if match_pattern(string):
        print(f'{string}',' pattern')
    else:
        print(f'{string}', 'not pattern')
#ex2
import re

pattern = r'a(b{2,3})'

test_strings = ['abb', 'abbb', 'abbbb', 'acb', 'ab', 'abbbbcd']
for test_string in test_strings:
    if re.search(pattern, test_string):
        print(f'{test_string}', "is pattern" )
    else:
        print(f'{test_string}',"not a pattern")

#ex3
import re

pattern = r'[a-z]+_[a-z]+'

test_strings = ['hello_world', 'python_program', 'data_science', 'abc_def_ghi', '123_abc']

for test_string in test_strings:
    matches = re.findall(pattern, test_string)
    if matches:
        print(f"Found sequence(s) in '{test_string}': {matches}")
    else:
        print(f"No sequence found in '{test_string}'.")

#ex4
import re

pattern = r'[A-Z]+[a-z]+'

test_strings = ['Almaty', 'python', 'Inzhu', 'One', 'Love', 'bbc_123', 'Abc_eea']

for test_string in test_strings:
    matches = re.findall(pattern, test_string)
    if matches:
        print(f"Found sequence(s) in '{test_string}': {matches}")
    else:
        print(f"No sequence found in '{test_string}'.")

#ex5
import re

pattern = r'a.*b$'

test_strings = ['acb', 'a123b', 'axb', 'ab', 'a_xyz_b', 'abc']

for test_string in test_strings:
    if re.search(pattern, test_string):
        print(f"'{test_string}'pattern.")
    else:
        print(f"'{test_string}'not pattern")

#ex6
import re

input_string = str(input("Enter a string: "))

pattern = r'[ ,.]'

output_string = re.sub(pattern, ':', input_string)

print("Modified String:", output_string)

#ex7
snake_case_string = str(input("Write your snake_case string: "))
def snake_to_camel(snake_str):
    return ''.join(word.capitalize() for word in snake_str.split('_'))

camel_case_string = snake_to_camel(snake_case_string)

print(camel_case_string)

#ex8
import re

def split_string_at_uppercase(input_string):
    split_string = re.findall('[A-Z][^A-Z]*', input_string)
    return split_string

input_string = "HelloNurbaNurba"
result = split_string_at_uppercase(input_string)
print(result)

#ex9
import re

def insert_spaces(input_string):
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return modified_string

input_string = "SalamAlekumAlekumSalam"
result = insert_spaces(input_string)
print(result)

#ex10
import re

def camel_to_snake(input_string):
    snake_case_string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', input_string).lower()
    return snake_case_string

input_string = "jHoneJhonesOadc"
result = camel_to_snake(input_string)
print(result)

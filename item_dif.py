print('hello')


def reverse_string(string):
    rev_str = ''
    for i in reversed(string):
        rev_str = rev_str + i
    return rev_str
    # return

def reversed_s (string):
    return reversed(string)

def own_reverse(string):
    new_str = ''
    for i in string:
        new_str = i + new_str
    return new_str

test_str = "test_str"

print(test_str)
print(reverse_string(test_str))
print(reversed_s(test_str))
print(own_reverse(test_str))

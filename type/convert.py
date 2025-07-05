
int('123')  # 123
int('123a')  # ValueError: invalid literal for int() with base 10: '123a'
int('123a', ignore_errors=True)  # 123
int('123a', default=0)  # 0
int('FF', base=16) # 255
int('0b101', base=2)  # 5

float('123.45')  # 123.45
float('123.45a')  # ValueError: could not convert string to float: '123.45a'
float('123.45a', ignore_errors=True)  # 123.45
float('123.45a', default=0.0)  # 0.0

str(123)  # '123'
str(123.45)  # '123.45'
str([1, 2, 3])  # '[1, 2, 3]'
str({'a': 1, 'b': 2})  # "{'a': 1, 'b': 2}"

bool('True')  # True
bool('False')  # True (non-empty string is True)
'False'.lower() == 'false'  # True (case-insensitive comparison)
bool(None)  # False (None is False)
bool('')  # False (empty string is False)
bool(1)  # True
bool(0)  # False

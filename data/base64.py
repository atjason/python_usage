# https://docs.python.org/3/library/base64.html

import base64

j_str = b'{"name": "Tom", "age": 3}'
encode_str = base64.b64encode(j_str)
decode_str = base64.b64decode(encode_str)
decode_str == decode_str

encode_str = base64.urlsafe_b64encode(j_str)
decode_str = base64.urlsafe_b64decode(encode_str)
decode_str == decode_str

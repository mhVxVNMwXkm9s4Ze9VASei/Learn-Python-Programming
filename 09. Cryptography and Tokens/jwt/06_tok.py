# jwt/tok.py
import jwt

data = {'payload': 'data', 'id': 123456789}

token = jwt.encode(data, 'secret-key')
algs = ['HS256', 'HS512']

data_out = jwt.decode(token, 'secret-key', algorithms = algs)
print(token)
print(data_out)

token512 = jwt.encode(data, 'secret-key', algorithm = 'HS512')
data_out = jwt.decode(token512, 'secret-key', algorithms = ['HS512'])
print(token512)
print(data_out)

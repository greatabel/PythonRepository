import json
import jwt

import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from os import environ

# https://github.com/jpadilla/pyjwt/pull/197/files
# https://pyjwt.readthedocs.io/en/latest/
private_key_pem = environ.get('PRIVATE_KEY_PEM_ALADDIN')
print( type(private_key_pem), private_key_pem.encode(), type(private_key_pem.encode()))
private_key_pem = private_key_pem.encode()
private_key_pem = b'''
-----BEGIN RSA PRIVATE KEY-----
MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAIjjDcqMV/J5WG/KGQ+DOotKe0UfFgG4Vu9ZvwaxGRZ4plQ4exSSXamXoNLBTKVFflvqCCYW9/XRBpnFgoUg7EQac8e6aqYqzSCwtQwO1ygo2JS3L1SzIiU3dt4WVs91oRMgxoD+DsQ7gkPGVgMTnwiMrTus6OxFeE8rwEdpFAuVAgMBAAECgYAEemkZFz5JUG70OUhYmZJwvB8MQ9gUdlNhwS3eqiyH76qBVtev9Jnb0noQawJ25a8ckqtxk47JG+17WlrKwCj6hLB1d3H7yZbtpwHkBqCINq3mGajzW58beCq5Umfq+jE5+4N5qse1e8DWiPhluJHPYgEUdIMGvsHGJW1r/5bMgQJBAPU5mSlFOuMKBGV62IvOe9YTum9Jr3HjRGxLnmvqQaj941VQ3bZNiqYFQ92Lc4X1iwaWju5QARGKhyrZbFSTL3cCQQCO5tHr9UWZlk42RFi0KUoHiBpVYi5C3Jk9DmoJzGOEfmPEHwyQL//ba4hKWgAnglTy7ci7yygfzqDvSB5Ne5hTAkBsiLefKoLrpa1YdMyO5C6vC0BCrSw3jczk2XsebCnvb59ETWwzmZI59K6ayXOx4IFNwykzlLlEWDmG34Aw1ov1AkBqXZqRJG6a5Irwz6yq5TTKKF9ZgIvojqStEqaRBoZon18JIwdJ58BtBTxcA2OsBNHQRHeueIg0LKwTjz2m9MErAkBHOB29i6t83D90DGW3INWBKlxY7JZOJvbi3LUHUVYhdF4oHSYS/jFra2ayRRIIX/zo3x0zstbQ+YQDrU0eQyVH
-----END RSA PRIVATE KEY-----
    '''
private_key = serialization.load_pem_private_key(
    private_key_pem,
    password=None,
    backend=default_backend())

# cat private_key.pem | openssl rsa -pubout | tee public_key.pem
public_key_pem = b'''
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCI4w3KjFfyeVhvyhkPgzqLSntFHxYBuFbvWb8GsRkWeKZUOHsUkl2pl6DSwUylRX5b6ggmFvf10QaZxYKFIOxEGnPHumqmKs0gsLUMDtcoKNiUty9UsyIlN3beFlbPdaETIMaA/g7EO4JDxlYDE58IjK07rOjsRXhPK8BHaRQLlQIDAQAB
-----END PUBLIC KEY-----
    '''
# public_key_pem = environ.get('PUBLIC_KEY_PEM_ALADDIN')
# public_key_pem = public_key_pem.encode()

public_key = serialization.load_pem_public_key(
    public_key_pem,
    backend=default_backend())

print('private_key->', private_key)
print('public_key->',   public_key)

mytime = datetime.datetime.utcnow() + datetime.timedelta(10,10)
# message = {
#     'usr': 10002,
#     'name': 'mockname',
#     'iat': mytime,
#     'exp': mytime,
#     'iss': '模拟凯旋广州公司',
#     'aud': 'meomo',
#     'rnd': 10
# }
message = {'usr': '324324', 'rnd': 123456}

# encoded = jwt.encode(message, 'secret', algorithm='HS256')

# assert message == jwt.decode(encoded, 'secret', algorithms=['HS256'])

encoded = jwt.encode(message, private_key, algorithm='RS256')
# encoded = b'eyJhbGciOiJIUzI1NiJ9.eyJybmQiOjEyMzQ1NiwidXNyIjoiMzI0MzI0In0.09AMJg2oWxj5w9aV1sYQPrWzU9JQkDemoa9rCbdPnWI'
print('-'*20, type(encoded),'-'*20,'\n', encoded,'\n'*2)
# decoded = jwt.decode(encoded, public_key, audience='meomo', algorithms=['RS256'])
js_obj = jwt.decode(encoded, verify=False)
print('decoded',js_obj, '#'*20)
decoded = jwt.decode(encoded, public_key,  algorithms=['RS256'])
print('decoded',decoded)
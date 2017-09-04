import json
import jwt
from datetime import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# https://github.com/jpadilla/pyjwt/pull/197/files
# https://pyjwt.readthedocs.io/en/latest/

private_key_pem = b'''
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDBCeVu627zFZ1JH9/Wi/J/bs6zC3bUFl0ASfE6XHGxyPTAPXgJ
nc7AsnRBxbNA692v1srkZr1X1BwUbzcaMRZwpGi4vO4VwzLldJC/YLFp5z6C66bg
GvRrp5pQhu4ntuHR82yS2X/IBsmMArUug9mO/LyoGthqRBVic/a9l9+INQIDAQAB
AoGBAIekj45waubuwjXW6u+UKRL4ZtAS9y2yhSklzBbpTI7TmX/X8Zg4RkbLXru0
0u+EjaL4eFskAlpL1mtZdsu1wICvyiFKuvh5WE+OwxBLpju/7AuZ9lCan9HR0X8P
EXASwU8ZFGTbLWPJePeiWl41431EAZtq/cWDSB/RQeoa2mNBAkEA5OKP+uxjSH1o
kCg+YqmlaakQ+2b8fS5J0ZyriVmoOAG0af647rsf4G3x3tXokoLXLn/620DE1HQ5
fCqI7l2xhQJBANfoNwSAqMbrURS2g4X1F6t5kxqPW7QNYrqPiAwGeXrJlG0Y8U5v
Yv73vRlnigdSJzTQOnY0FhniFWuScIdk4vECQG6iTLIfHQZnB+nWagFKuxfNjtXW
O+lOPIRDVG75lWQs/sXVSBKtBIV431a00swuzlA9sEXWks2WuEqaTMHbK/kCQQCG
3uV3Z5OG5zp4EOcqCAeoM0LERadIW1BAMCcRM/4wyLlySTF8CLKziThUJUyg9B3P
rP/IFRN1SbiNwSWQPmJRAkEAlBTPJeblIe0u/Zj8f4AKaSnKQXBvTwA3OP/FyjHR
8KaS4wpfYQvYuXZe6EDB6d6AxNxDuYn5T6D/qtVAR/eZWw==
-----END RSA PRIVATE KEY-----
    '''
private_key = serialization.load_pem_private_key(
    private_key_pem,
    password=None,
    backend=default_backend())

# cat private_key.pem | openssl rsa -pubout | tee public_key.pem
public_key_pem = b'''
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBCeVu627zFZ1JH9/Wi/J/bs6z
C3bUFl0ASfE6XHGxyPTAPXgJnc7AsnRBxbNA692v1srkZr1X1BwUbzcaMRZwpGi4
vO4VwzLldJC/YLFp5z6C66bgGvRrp5pQhu4ntuHR82yS2X/IBsmMArUug9mO/Lyo
GthqRBVic/a9l9+INQIDAQAB
-----END PUBLIC KEY-----
    '''

public_key = serialization.load_pem_public_key(
    public_key_pem,
    backend=default_backend())

print('private_key->', private_key)
print('public_key->',   public_key)

message = {
    'userid': 'https://example.com/',
    'sub': 'yosida95',
    'iat': datetime.utcnow(),
    'exp': datetime.utcnow(),
}

# encoded = jwt.encode(message, 'secret', algorithm='HS256')

# assert message == jwt.decode(encoded, 'secret', algorithms=['HS256'])

encoded = jwt.encode(message, private_key, algorithm='RS256')
print('-'*20, type(encoded),'-'*20, encoded)
decoded = jwt.decode(encoded, public_key, algorithms=['RS256'])
print(decoded)
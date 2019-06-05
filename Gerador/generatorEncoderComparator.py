#Domarys Correa - generatorEncoderComparator.py()
from itertools import product
import string
import base64
import hashlib

#key = "b'FnAmZZ+NfRVWmY16yvI+aV4s0ztDLiUx3uHtFNHd3iw='" #teste com "domarys9"
key = "b'YTEUCxI8/wSjrTpm/EqL7s9aR++fqs2f3JBav3vK5Uk='" #palavra-chave


permsList = [''.join(x) for x in product((string.ascii_lowercase+string.ascii_uppercase+string.digits), repeat=1)] #indo de 1-8 caracteres
'''
print(permsList)
x = "domarys9";
x = x.encode("utf-8")
key256  = hashlib.sha256(x).digest()
key64 = base64.b64encode(key256)
print("key64: "+str(key64))
print("key: "+str(key))
if str(key64) == str(key):
	print("achamos")
'''
for x in permsList:
	x = x.encode("utf-8")
	key256  = hashlib.sha256(x).digest()
	key64 = base64.b64encode(key256)
	if str(key64) == str(key):
		code = key64;
		print("achamos")
		break
print(code);
		



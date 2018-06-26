from distutils.log import warn as printf
from json import dumps
from pprint import pprint



print(type(BOOKs))

printf('\n*** RAW JSON ***')
printf(dumps(BOOKs))

printf('\n*** PRETTY_PRINTED JSON ***')
printf(dumps(BOOKs, indent=4))

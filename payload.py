#!/usr/bin/env python
#coding = utf-8
import codecs

from base64 import *

result = {
	'16': lambda x: b16decode(x),
	'32': lambda x: b32decode(x),
	'64': lambda x: b64decode(x),
}

flag = open('code.txt', 'rb')
flag_content = flag.read()
# print flag_content

num = ('16', '32', '64')

for i in range(10):
	for k in num:
		try:
			flag_content = result[k](flag_content)
			if flag_content:
				break
			else:
				continue
		except:
			pass
print(flag_content)
with open("final_flag.txt", "wb") as final_flag:
	final_flag.write(flag_content)


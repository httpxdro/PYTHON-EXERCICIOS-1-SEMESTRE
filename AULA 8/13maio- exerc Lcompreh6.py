Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> L = [0, 2, 4, 6, 8]
>>> L
[0, 2, 4, 6, 8]
>>> L = []
>>> for i in range(5):
	L.append(2*i)
l
SyntaxError: invalid syntax
>>> L = [2*i] for i in range(5)]
SyntaxError: invalid syntax
>>> L = [2*i for i in range(5)]
>>> L
[0, 2, 4, 6, 8]
>>> 

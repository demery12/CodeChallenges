
#y is vowel
def is_vowel(char):
	return char.lower() in ['a','i','e','o','u','y']
def is_const(char):
	return char.lower() in "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,z".split(',')
def encode_rov(text):
	encoded = ""
	for char in text:
		if is_const(char):
			encoded += "o"+char+"o"
		else:
			encoded += char
	return encoded
print encode_rov("I'm speaking Robber's language!")

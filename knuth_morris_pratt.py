def preprocess(pattern):
	preprocess_table = {}
	j = 0 
	i = 1
	preprocess_table[0] = 0
	while i < len(pattern):
		while i<len(pattern) and pattern[j]==pattern[i]:
			preprocess_table[i]=j+1
			i += 1
			j +=1
		if j == 0:
			preprocess_table[i] = 0
			i +=1
		else:
			j = preprocess_table[j-1]
	return preprocess_table
def knuth_morris_pratt(string,pattern):
	p_table = preprocess(pattern)
	i = 0
	j = 0
	ans=[]
	print "woo"
	while i<len(string):
		print string[i],pattern[j],i,j
		while i<len(string) and string[i] == pattern[j]:
			print i,j
			if j+1 == len(pattern):
				ans += [i-j]
				print ans
				break
			i+=1
			j+=1
		if j != 0 and p_table[j]>1:
			i += j-p_table[j-1]
			j = 0
		else:
			i+=1
			j=0
	return ans
preprocess('abcdabca')
print preprocess('abababca')
print knuth_morris_pratt('abababcaaabbcabbcbabbcbbcbabbcbcabbcabcbabbcbabbcbbabcbbbabbcbbabbcbabbcbabbcbabbacbcbabbcabbabcabcabcabc','abcabcabcabc')
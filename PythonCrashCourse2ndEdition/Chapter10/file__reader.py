'''
with open('pi__digits.txt') as file_object:
	contents=file_object.read()
	#print(contents)
	print(contents.rstrip())
'''
'''
with open('pi__digits.txt') as file_object:	
	for line in file_object:
		print(line)
'''
with open('pi_million_digits.txt') as file_object:
	lines=file_object.readlines()
pi_string=''
for line in lines:
	pi_string+=line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))

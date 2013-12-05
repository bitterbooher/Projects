#quiz maker

#how to read in files

useranswers = []
realanswers = []
with open("sample1.txt") as f:
	for line in f:
		print line,
		var = raw_input("Your answer :")
		useranswers.append(var)
#print useranswers

with open("key1.txt") as b:
	for line in b:
		#print line,
		realanswers.append(line.rstrip()) #rstrip will rid of \n 
print realanswers

print useranswers[0] == realanswers[0]
print useranswers[1] == realanswers[1]
print useranswers[2] == realanswers[2]
#print key versus answers


#answer each question in line

#randomly select questions

# implementing ceaser cypher

# String, Int -> String
# Rotate each letter in the string, by int to produce a string

# cc(AB,2) -> CD
# cc(AB,4) -> EF


alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","q","x","y","z"]
#if we can do a find on the each substring, maybe we can return the index of it + 2

def cypher(string, key):
	newstring = ""
	for x in string:
 
#print alphabet[alphabet.index("g")+2] # now shifted 2 spaces to the left
		if alphabet.index(x)+key > 25:
			newstring = newstring + alphabet[alphabet.index(x)+key-26]
		else:
			newstring = newstring + alphabet[alphabet.index(x)+key] #one issue is that we need to do this for every letter.
					#this only works if the index+key < 23
	print newstring
	return newstring
	
cypher("y", 1)
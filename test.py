f = open("raw",'r')

string = f.read()
length = len(string)

counter = 0
newString = ""
while(counter < length):
	if ord(string[counter]) > 126:
		newString = newString + string[counter]
	if string[counter] == " " and string[counter-1] != " ":
		newString = newString + " "
	counter += 1
newString = newString.split()

wholeNewString = ""
for word in newString:
	ifcapital = 1
	print(word)
	for n in word:
		if ord(n) > 1071 and ord(n) != 1256 and ord(n) != 1198:
			ifcapital = 0
	if ifcapital == 1:
		wholeNewString = wholeNewString + " " + word
print(wholeNewString)
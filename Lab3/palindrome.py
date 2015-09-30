print "Give a word to Palindrome Checker"

a = raw_input()

b = a[::-1]

if a.lower() == b.lower():

print "True"

else:

print "False" 

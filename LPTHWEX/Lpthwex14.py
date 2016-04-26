from sys import argv
script, user_name = argv
prompt = '> '

print ("Hi %s, I'm the %s script."%(user_name,script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)
print ("Where do you live? %s"%user_name)
lives = input(prompt)
print ("What kind of computer do you have? %s"%user_name)
computer = input(prompt)
print ("""Alright, so you said %r about liking me.
You live in %r . Though not sure where that is.
And you have a %r computer. nice!"""%(likes,lives,computer))

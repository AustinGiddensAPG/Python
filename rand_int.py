from random import * 
def randlist(r):
	alpha = ["a","b","c","d","e"]
	c = alpha[r]
	return c #this belongs to ranlist(r)
	
def main():
	while True:
		r = randint(0,4)
		c = randlist(r)
		print(c,end="")
main()

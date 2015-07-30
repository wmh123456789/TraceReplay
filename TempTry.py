# temp try
import os


def RegionCount(alist,rules):
	# rules: {keyA:ruleA,keyB:ruleB,...}
	count = dict(zip(rules.keys(),[0 for i in xrange(0,len(rules))]))
	for e in alist:
		for key in rules.keys():
			if rules[key](e) == True:
				count[key] += 1
				pass
		pass
	return count
	pass

def main():

	A = lambda t: t<10
	B = lambda t: t>=10 and t<20
	C = lambda t: t>=20
	rules = {'I':A,'II':B,'III':C}
	alist = [1,2,12,23,33,44]
	count = RegionCount(alist,rules)
	print count


if __name__ == '__main__':
	main()
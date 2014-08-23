import sys
import json
import pprint
from collections import Counter

pp = pprint.PrettyPrinter(indent=1)

def hw(tweet_file):
	cleandata = []
	
	for line in tweet_file:
		textdata = json.loads(line)
		if 'entities' in textdata.keys():
			for e in textdata["entities"]["hashtags"]:
				cleandata.append(e["text"])
	hashcount = Counter(cleandata).most_common()
	for lines in range(10):
		print hashcount[lines][0].encode('utf8'), hashcount[lines][1]
	
	

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()

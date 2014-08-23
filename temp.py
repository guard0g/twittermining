import sys
import json


def hw(tweet_file,sent_file):
	score_dic = {}
	read_dic(score_dic,sent_file) 
	for line in tweet_file:
		tweet = json.loads(line)
		if 'text' in tweet.keys():
			tweet_words = tweet['text'].encode('utf8').split()
		print tweet_words
	
def lines(fp):
    print str(len(fp.readlines()))

def read_dic(score_dic,sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
		score_dic[term] = int(score)
#	print scores.items() # Print every (term, score) pair in the dictionary

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(tweet_file,sent_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()

    

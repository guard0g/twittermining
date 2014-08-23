import sys
import json

def hw(tweet_file):
	all_tweets = []
	
	for line in tweet_file:
		textdata = json.loads(line)
		if 'text' in textdata:
			all_tweets.append(textdata['text'].encode('utf-8'))
		
	new_words = set()
	for line in all_tweets:
		word_list = line.split()
		for word in word_list:
			if word not in new_words:
				new_words.add(word)
	
	new_word_list = list(new_words)
	new_word_score = [0.]*len(new_word_list)
	
	for idx in range(len(new_word_list)):
		for index in range(len(all_tweets)):
			if new_word_list[idx] in all_tweets[index]:
				new_word_score[idx] += 1.
		print new_word_list[idx], new_word_score[idx]

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)


if __name__ == '__main__':
    main()

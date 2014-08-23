import sys
import json

def hw(sent_file,tweet_file):
	score_dic = {}
	all_scores = []
	all_tweets = []
	read_dic(score_dic,sent_file) 
	
	for line in tweet_file:
		score = 0
		textdata = json.loads(line)
		if 'text' in textdata:
			for item in score_dic:
				if item in textdata['text'].encode('utf-8'):
					score += score_dic[item]
			all_scores.append(score)
			all_tweets.append(textdata['text'].encode('utf-8'))
		
	new_words = set()
	for line in all_tweets:
		word_list = line.split(" ")
		for word in word_list:
			if word not in new_words:
				new_words.add(word)
	
	new_word_list = list(new_words)
	new_word_score = [0.]*len(new_word_list)
	
	for idx in range(len(new_word_list)):
		for index in range(len(all_tweets)):
			if new_word_list[idx] in all_tweets[index]:
				new_word_score[idx] += all_scores[index]
		print new_word_list[idx], new_word_score[idx]
#	for i in range(len(new_word_score)):
#		print new_word_score[i]
					

					
def read_dic(score_dic,sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
		score_dic[term] = int(score)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()

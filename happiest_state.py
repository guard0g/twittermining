import sys
import json
import pprint
pp = pprint.PrettyPrinter(indent=1)

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def hw(tweet_file,sent_file):
	results = []

	score_dic = {}     #load sentiment word dictionary
	read_dic(score_dic,sent_file) 
	
	for line in tweet_file:   # score tweets, store in results
		score = 0
		textdata = json.loads(line)
		if 'text' in textdata.keys():
			for item in score_dic:
				if item in textdata['text'].encode('utf-8'):
					score += score_dic[item]
			results.append((textdata,score))

	
	# Code tweets by state
	resultss = []
	for item in results:		
		textdata = item[0]
		if 'user' in textdata.keys():
			if textdata['user']['location'] != None:
				location = textdata['user']['location'].encode('utf8').strip()
				for state in states:
					if state in location:
						item = (item,state)
						break
					elif states[state] in location:
						item = (item,state)
						break
		resultss.append(item)
	
	stscores = {}
	for item in states:
		stscores[item] = 0

	for item in resultss:
		if item[1] in states:
			stscores[item[1]] += 1
	
	print max(stscores,key=stscores.get)
	
	

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

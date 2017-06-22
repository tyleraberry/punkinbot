'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'qL3VpnFAETqoX0PyGG9DgxC6d'
MY_CONSUMER_SECRET = 'fZFBouJnGhr0br3eQF5gcP2bs9rTgRrupH2Msff0F4D4ikw5qy'
MY_ACCESS_TOKEN_KEY = '730458577178112001-PDB2SXJMfmynjKwwM9wqqguR8iT0P9s'
MY_ACCESS_TOKEN_SECRET = 'CD3ax1jN2G8sjCbT1JMLAtEGqY3rRNLJayfs9YktstUfA'

SOURCE_ACCOUNTS = ["maggiereimherr"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 4 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "punkin_bot" #The name of the account you're tweeting to.

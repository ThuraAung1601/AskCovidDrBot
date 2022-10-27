import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dataset = "./data/covid_qA.csv"
data = pd.read_csv(dataset)

vectorizer = TfidfVectorizer()
count_vec = vectorizer.fit_transform(data['Question']).toarray()

def COVIDbot(user_response):
    text = vectorizer.transform([user_response]).toarray()
    data['similarity'] = cosine_similarity(count_vec, text)
    return data.sort_values(['similarity'], ascending=False).iloc[0]['Answer']

welcome_input = ("hello", "hi", "greetings", "sup", "what's up","hey",)
welcome_response = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def welcome(user_response):
    for word in user_response.split():
        if word.lower() in welcome_input:
            return random.choice(welcome_response)

def generate_response(user_response):
	user_response = user_response.lower()
	if(user_response not in ['bye','shutdown','exit', 'quit']):
		if(user_response=='thanks' or user_response=='thank you'):
		    flag=False
		    return "You are welcome.."
		else:
		    if(welcome(user_response)!=None):
		    	response = welcome(user_response)
		        return response
		    else:
		        return COVIDbot(user_response)
            
def main():
	flag=True 
	print("Greetings! I am a chatbot and I will try to answer your questions about COVID-19. If you want to exit, type Bye!")
	while(flag==True):
	    user_response = input()
	    user_response = user_response.lower()
	    if(user_response not in ['bye','shutdown','exit', 'quit']):
		if(user_response=='thanks' or user_response=='thank you'):
		    flag=False
		    print("Chatbot : You are welcome..")
		else:
		    if(welcome(user_response)!=None):
		        print("Chatbot : "+welcome(user_response))
		    else:
		        print("Chatbot : ",end="")
		        print(COVIDbot(user_response))
	    else:
		flag=False
		print("Chatbot : Bye!!! ")

main()

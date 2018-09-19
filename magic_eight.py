import random

poss_answers = [ "It is certain.", "It is decidely so.", "Without a doubt.", "Yes - definitely.",
"You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", 
"Signs point to yes.",  "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
"Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
"My sources say no.", "Outlook not so good.", "Very doubtful."]

my_responses = input("What is your question?")

while my_responses != "quit":
	while my_responses[-1] != "?":
		print("I'm sorry, I can only answer questions.")
		my_responses = input("What is your question?")

    x = random.randrange(0, 20)

    print (poss_answers[x])
    
    my_response = input("What is your question?")
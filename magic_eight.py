my_responses = input("What is your question?")

while my_responses != "quit":
	while my_responses[-1] != "?":
		print("I'm sorry, I can only answer questions.")
		my_responses = input("What is your question?")

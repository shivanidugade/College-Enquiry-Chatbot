import aiml

kernel = aiml.Kernel()
kernel.learn('std-startup.xml')
kernel.respond('load aiml b')

while True:
	input_text = input("HUMAN > ")
	response = kernel.respond(input_text)
	if response[:4] == 'http':
		print("<a href='"+ response +"'>Click here for more info</a>")
	else:
		print("Bot >" + response[0:4])

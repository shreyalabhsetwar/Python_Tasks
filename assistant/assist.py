import pyttsx3 as pys
import os
print("\n\t \t :-:-:-:-:-:-:-:-:-:-:-:Welcome To Shreya's Menu:-:-:-:-:-:-:-:-:-:-:-:")

pys.speak("welcome to the world where OS based programs are converted in Menu Driven Programs")
print("\n How can I Help You?\n")
pys.speak("How can I help You?? please Specify your operation")


while True:
	print("Please specify your operation: ",end='')
	#pys.speak("Please specify your operation")
	choice=input()
	
	if (("run" in choice) or ("execute" in choice)) or (("start" in choice) or ("open" in choice) or ("run" in choice)or("goto" in choice)):
		#pys.speak("loading the program for you.")
		
		if ("chrome" in choice):
			os.system("start chrome")
		elif ("wmplayer" in choice) or ("mediaplayer"in choice):
			os.system("start wmplayer")
		elif ("notepad" in choice):
			os.system("start notepad")
		elif ("paint" in choice):
			os.system("start mspaint")
		elif ("calculator" in choice)or ("cal" in choice) or ("calc" in choice):
			os.system("start calc")
		elif ("prompt" in choice) or ("cmd" in choice):
			os.system("start cmd")
		elif ("explorer" in choice) or ("file" in choice):
			os.system("start explorer")
		elif ("team" in choice) :
			os.system("TeamViewer")
		elif ("settings" in choice) :
			os.system(" start ms-settings:")
		elif ("vbox" in choice) :
			os.system(" start VirtualBox")
		elif ("vs" in choice):
		    os.system("start Code")
		elif ("studio" in choice) :
			os.system(" start devenv")
		elif ("word" in choice) :
			os.system(" start WINWORD")
		elif ("excel" in choice) :
			os.system(" start EXCEL")
		elif ("ppt" in choice) :
			os.system(" start POWERPNT")
		elif ("date" in choice) :
			os.system(" start date")
			pys.speak(" start date")
		else:
			pys.speak("Sorry, Its an invalid operation,try something else.")
			print("\t\tSorry, Its an invalid operation,try something else")	
		
			
		
		
	if (("exit" in choice) or ("stop" in choice) or ("quit" in choice)) or (("done" in choice) or ("out" in choice)):
		break
	
	

print("\n\t \t :-:-:-:-:-:-:-:-:-:-:-:ThankYou:-:-:-:-:-:-:-:-:-:-:-:")
pys.speak("Thanks we are  Hoping to see you again!!!")

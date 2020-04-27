import random
import time
import speech_recognition as sr


def print_scaffold(guesses, wd): # prints the scaffold
		if (guesses == 0):
				print ("_________")
				print ("|	 |")
				print ("|")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 1):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (guesses == 2):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	 |")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (guesses == 3):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (guesses == 4):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (guesses == 5):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ ")
				print ("|________")
		elif (guesses == 6):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ \ ")
				print( "|________")
				print ("\n")
				print ("The word was %s." %wd)
				print ("\n")
				print ("\nYOU LOSE! TRY AGAIN!")
				print ("\nWould you like to play again, type 1 for yes or 2 for no?")
				again = str(raw_input("> "))
				again = again.lower()
				if again == "1":
				  hangMan()
				return


def recognize_speech_from_mic(recognizer,microphone) :
	if not isinstance(recognizer, sr.Recognizer):
		raise TypeError("`recognizer` must be `Recognizer` instance")

	if not isinstance(microphone, sr.Microphone):
		raise TypeError("`microphone` must be `Microphone` instance")
    	
	with microphone as source :
		recognizer.adjust_for_ambient_noise(source)
		print("alphabet? ")
		audio = recognizer.listen(source)
		print("TIME UP !")
	
	
		
	response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    
	try:
		response["transcription"] = recognizer.recognize_google(audio)
	except sr.RequestError:
		
		response["success"] = False
		response["error"] = "API unavailable"
	except sr.UnknownValueError:
		
		response["error"] = "Unable to recognize speech"

	return response
    

if __name__ == "__main__" :
	
	WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
	
	word= random.choice(WORDS)
	
	recognizer=sr.Recognizer()
	microphone=sr.Microphone()
	


	guesses = 0					
	  				
	word_list = list(word)	
	blanks = "_"*len(word)	
	blanks_list = list(blanks) 
	new_blanks_list = list(blanks)
	guess_list = []
	  
	print ("Let's play hangman!\n")
	print_scaffold(guesses, word)
	print ("\n")
	print ("" + ' '.join(blanks_list))
	print( "\n")
	print ("Guess a letter.\n")
	  
	while guesses < 6:
	  
	  		guess = recognize_speech_from_mic(recognizer,microphone)
	  		if (guess['success']== True) :
	  		
	  			try :
		  			guess = guess['transcription'].lower()
		  		except AttributeError :
		  			print("COUND NOT HERE YOU ? SAY AGAIN !")
		  			guess = recognize_speech_from_mic(recognizer,microphone)
		  			guess = guess['transcription'].lower()
		  		if len(guess) > 1:
		  				if (guess[0]==guess[1]) :
		  					guess=guess[0]
		  				else :
		  					print ("Stop cheating! Enter one letter at time.")
		  		elif guess == "":
		  				print ("Don't you want to play? Enter one letter at a time.")
		  		elif guess in guess_list:
		  				print ("You already guessed that letter! Here is what you've guessed:")
		  				print (' '.join(guess_list))
		  		else:
		  				guess_list.append(guess)
		  				i = 0
		  				while i < len(word):
		  						if guess == word[i]:
		  								new_blanks_list[i] = word_list[i]
		  						i = i+1
		  
		  				if new_blanks_list == blanks_list:
		  						print ("Your letter isn't here.")
		  						guesses = guesses + 1
		  						print_scaffold(guesses, word)
		  						
		  						if guesses < 6:
		  								print ("Guess again.")
		  								print (' '.join(blanks_list))
		  						
		  				elif word_list != blanks_list:
		  						
		  						blanks_list = new_blanks_list[:]
		  						print (' '.join(blanks_list))
		  						
		  						if word_list == blanks_list:
		  						  print ("\nYOU WIN! Here is your prize:")
		  						  print ("\n")
		  						  print ("Would you like to play again?")
		  						  print ("Type 1 for yes or 2 for no.")
		  						  again = str(raw_input("> "))
		  						  if again == "1":
		  						    hangMan()
		  						  quit()
		  						
		  						else:
		  								print ("Great guess! Guess another!")
													




		        
		        
		        
		        
		        
		        
		        
		        
		        
		        

#============================================================================================#
#                                                                                            #
#                           Code made by James Garrick                                       #
#              Description: Quiz that determines user's preferred dog breed                  #
#                                                                                            #
#============================================================================================#

# Notes:

# Need to adjust spaceScore, homeScore, and cost values for each dog and questions to balance.

# Debug.userinfo does not reset upon quiz restart.

# Dog definitions from hillspet.com

#============================================================================================#

import time
import sys
import os

#============================================================================================#

# Config Values for Quiz

debug = False # Debug mode, allows access to certain commands. Question system doesn't work correctly yet if set to true.

dogsShown = 2 # Number of dogs that are shown to user 
maxDogsShown = 4 # Maximum number of dogs that are shown to user if select show more results

sleepInterval = 1 # Standard time for pauses within quiz.

startText = "This is a quiz to find out which dog breed best suits you!\nThere are lots of dog breeds to choose from!"
endText = "Thank you for taking the quiz!"

#============================================================================================#

# Classes for dogs and questions.

class dog:
    def __init__(breed, spaceScore, homeScore, size, coatLength, cost, personality, name, definition = 'Sorry, there is no definition for this dog.'):
      breed.spaceScore = spaceScore
      breed.homeScore = homeScore
      breed.size = size  
      breed.name = name
      breed.coatLength = coatLength
      breed.cost = cost
      breed.personality = personality
      breed.definition = definition
Husky = dog(45, 80, 'medium', 'medium', 50, 'family', 'Husky',
 'The classic northern dogs, Siberian huskies are friendly and intelligent but somewhat independent and stubborn. They thrive on human company, but need firm, gentle training from puppyhood.')
Pug = dog(15, 15, 'small', 'short', 30, 'friendly', 'Pug',
'Serious with a laid-back attitude, pugs are robust and easy to care for.')
German_Shepard = dog(40, 65, 'large', 'medium', 40, 'protective', "German Sheperd,",
'Smart and easily trained, the ever-popular German shepherd is quite active and likes to have something to do.')
Labrador = dog(30, 30, 'medium', 'short', 15, 'family', 'Labrador',
'The Labrador possesses numerous endearing traits — intelligence, easy to train and being an excellent family companion.')
Dalmation = dog(30, 30, 'medium', 'short', 30, 'family', 'Dalmation',
'Loyal, playful and intelligent, Dalmatians thrive on human companionship. They also need vigorous exercise to dispel boundless energy.')
Rottweiler = dog(15,15, 'medium', 'short', 15, 'friendly', 'Rottweiler',
'Not recommended for first-time owners, the rottweiler needs extensive and continuous socialization to be a good family companion. However, this intelligent, confident dog is easy to keep in spite of the size.')
Bulldog = dog(20, 20, 'small', 'short', 15, 'protective', 'Bulldog',
'Typically low-endurance dogs, English bulldogs have a sweet disposition, are predictable, dependable and excellent with children and need only moderate exercise.')
Great_Dane = dog(60, 60, 'large', 'short', 30, 'friendly', 'Great Dane',
'In spite of the size, Great Danes are considered gentle giants, are moderately playful and good with children.')
Boxer = dog(30, 45, 'small', 'short', 65, 'protective', 'Boxer',
'An intelligent, loyal pet, the boxer has a high need for companionship and exercise.')
Boston_Terrier = dog(55, 45, 'small', 'short', 65, 'friendly', 'Boston Terrier',
'A playful, fun breed, the Boston terrier is a great choice for people who want a cheerful and energetic companion.')
Chihuahua = dog(10, 10, 'small', 'short', 65, 'friendly', "Chihuahua",
'Chihuahuas are loyal, friendly and good family pets when treated respectfully.')
StBernard = dog(50, 50, 'large', 'short', 50, 'family', 'St. Bernard',
'Known to be loving, gentle and tolerant in spite of its size, Saint Bernards are a good with families with well-behaved children.')
Toy_Poodle = dog(10, 10, 'small', 'medium', 30, 'family', 'Toy Poodle',
'Toy Poodles are lively, active, fun-loving and family dogs with a sense of the ridiculous.')
Great_Pyranees = dog(45, 60, 'large', 'long', 30, 'family', 'Great Pyranees',
'If a family leads a placid life, the Great Pyrenees makes a great pet. The dog is calm, devoted and well-mannered.')
Golden_Retreiever = dog(55, 55, 'large', 'long', 30, 'family', 'Golden Retriever',
'Because golden retrievers are easy to please, they respond positively to obedience training. They complement this trait by being playful, affectionate and even-tempered.')
Pit_Bull = dog(35, 35, 'medium', 'short', 65, 'protective', 'Pit Bull',
'Most pit bulls are fun, gentle companions and patient with family members.')
Poodle = dog(25, 25, 'medium', 'long', 30, 'friendly', 'Poodle',
'Poodles are lively, active, fun-loving and family dogs with a sense of the ridiculous.')
Border_Collie = dog(65, 30, 'medium', 'medium', 65, 'family', 'Border Collie',
'A bright, clever breed, the border collie is best suited for country living.')
Fox_Hound = dog(35, 15, 'large', 'short', 65, 'protective', 'Fox Hound',
'An active, athletic and energetic dog, the English foxhound needs a great deal of exercise to thrive and is best suited for the countryside.')
Broholmer = dog(35, 20, 'large', 'short', 65, 'friendly', 'Broholmer',
'The Broholmer is a large purebred dog that is calm, protective, and friendly')
English_CockerSpaniel = dog(15, 15, 'small', 'long', 30, 'family', 'English Cocker Spaniel',
'The English cocker spaniel is cheerful, playful and thrives on companionship and being part of the family. He does require significant exercise.')
Maltese = dog(15, 15, 'small', 'long', 65, 'family', 'Maltese',
'Highly suitable for indoor living and small areas, the diminutive Maltese is gentle, responsive and intelligent.')
Schnauzer = dog(30, 15, 'small', 'medium', 65, 'family', 'Schnauzer',
'Quick, sociable learners and adaptable, Schnauzers can be just as happy living in a city apartment or in the country.')
Dobermann = dog(30, 45, 'large', 'short', 30, 'protective', 'Dobermann',
'Dobermans are powerful, energetic dogs that need plenty of exercise. If not exercised, they are likely to become irritable or even aggressive. Careful socialization and obedience training from a young age are essential.')
Shih_Tzu = dog(15, 15, 'small', 'long', 50, 'family', 'Shih Tzu',
'Perky and happy, the shih tzu tends to require a large amount of personal attention. Because it thrives on human company, it can easily become spoiled.')
AussieDog = dog(65, 30, 'medium', 'long', 65, 'friendly', 'Australian Shepard', 
'An active yet easy-going dog, the Australian shepherd loves to play with children and tends to get along well with other pets.')

class question:
    def __init__(question, questionAsked, choices, trait, method, userValues):
      question.question = question
      question.questionAsked = questionAsked
      question.choices = choices
      question.trait = trait
      question.method = method
      question.userValues = userValues

#============================================================================================#

# Variables relation to quiz.

          #this is the default list of dog. It includes all of the possible dogs included as answers
dogList = (Husky, Pug, Great_Dane, German_Shepard, Toy_Poodle, Labrador, Chihuahua, Rottweiler, 
           Dalmation, StBernard, Great_Pyranees, Boxer, Boston_Terrier, Bulldog, Golden_Retreiever,
           Pit_Bull, Poodle, Border_Collie, Fox_Hound, Maltese, Schnauzer, Dobermann, Broholmer, 
           English_CockerSpaniel, Shih_Tzu, AussieDog) 
dogChosen = list(dogList) # New list copy of dogList that is used for narrowing down selection.
dogExcluded = [] # Used for debugging. Any dogs that are removed from dogChosen are added to this list.

questionsCompleted = 0 # Value that increments for each question the user completes.

#============================================================================================#

# Values that are incremented based on user input, used for comparing to each dog's score for values.

valuesChosen = {
  'chosenSpace' : 0,
  'chosenHome' : 0,
  'chosenCost' : 0
}

#============================================================================================#

# Dictionaries that define possible answer options with index[0] being choice option and index [1] being value. This value is compared to each dog using chosen logic, defined in question.

choices1 = {
    'a' : ['Small', 'small'],
    'b' : ['Medium', 'medium'],
    'c' : ['Large', 'large'],
    'd' : ['No preference', '']
    }
choices2 = {
    'a' : ['Small Home', 15],
    'b' : ['Medium Home', 30],
    'c' : ['Large Home', 50]
    } 
choices3 = {
    'a' : ['Small Yard', 15],
    'b' : ['Medium Yard', 30],
    'c' : ['Large Large', 50],
    'd' : ['No Yard', 0]
    } 
choices4 = {
  'a' : ['Short Coat', 'short'],
  'b' : ['Medium Coat', 'medium'],
  'c' : ['Long Coat', 'long'],
  'd' : ['No preference', 'dog']
}
choices5 = {
  'a' : ['Inexpensive', 50],
  'b' : ['Somewhat expensive', 30],
  'c' : ['Expensive', 15],
  'd' : ['Money is not a problem', 100]
}
choices6 = {
  'a' : ['Yes, one', 50],
  'b' : ['Yes, more than one', 30],
  'c' : ['No', 50]
}
choices7 = {
  'a' : ['Yes', 15],
  'b' : ['No', 0]
}
choices8 = {
  'a' : ['Very often', 15],
  'b' : ['Occasionally', 30],
  'c' : ['Once in a while', 50],
  'd' : ['Never', 75]
}
choices9 = {
    'a' : ['Friendly', 'friendly'],
    'b' : ['Protective', 'protective'],
    'c' : ['Family Friendly', 'family'],
    'd' : ['No preference', '']  
}

#============================================================================================#

# Initializes all questions as instances of base question class, variable is created for later reference

question1 = question("What size of dog do you want?", choices1, "size", 'filter', '') 
question2 = question("How much space do you have in your home?", choices2, "spaceScore", 'compare', 'chosenSpace')
question3 = question("How much yard space do you have?", choices3, 'spaceScore', 'compare', 'chosenSpace')
question4 = question("How long do you want your dog's coat to be", choices4, 'coatLength', 'filter', '') 
question5 = question("How much money are you able to spend on a dog?", choices5, 'cost', 'compare', 'chosenCost') 
question6 = question("Are there kids under the age of 10 in your household?", choices6, "homeScore", 'compare', 'chosenHome') 
question7 = question("Can you deal with a loud dog?", choices7, 'homeScore', 'compare', 'chosenHome')
question8 = question("How frequently do you travel?", choices8, 'homeScore', 'compare', 'chosenHome')
question9 = question("What personality type do you want your dog to be?", choices9, 'personality', 'filter', '')

#============================================================================================#

# Checks if there is only 1 answer choice left.

def endCheck(choices):
  if len(dogChosen) <= 1:
    endTest(choices)
    
#============================================================================================#

# Function that clears console in case of restart. Does not work in replit.

def clearConsole():
  os.system('cls')

#============================================================================================#

# Called upon completion of questions that combine to influence a certain trait in a dog.

def removeCompare(trait, comparator):
  global dogChosen
  global valuesChosen
  global dogExcluded
  
  for x in dogChosen[:]:
    if int(getattr(x, trait)) != '':
      if int(getattr(x, trait)) > valuesChosen[comparator]:
        dogChosen.remove(x)
        dogExcluded.append(x)
    else:
      pass
#============================================================================================#

# Restarts the quiz, resets all changed values.

def restartQuiz():
  global questionsCompleted
  global dogChosen
  global valuesChosen
  global sleepInterval
  
  print('')
  print("Quiz will restart in" + str(sleepInterval) + "seconds.")
  
  time.sleep(sleepInterval)
  
  dogExcluded.clear()
  
  questionsCompleted = 0
  
  valuesChosen['chosenCost'] = 0
  valuesChosen['chosenHome'] = 0
  valuesChosen['chosenSpace'] = 0
  
  dogChosen = list(dogList)
  
  clearConsole()
  startTest(startText)

#============================================================================================#

# Function that ends quiz, gives dog(s) preferred, and gives option to restart or end.

def endTest(dogsShown):
    global dogChosen
    global dogList
    global startTest
    global endText
    global maxDogsShown
    global sleepInterval
    
    print('')
    
    if len(dogChosen) == 1:
        print("Based on our test, your preferred dog is the")
        for x in dogChosen:
            print(x.name)  

            time.sleep(sleepInterval)
            print('')
            print(x.definition)
            print('')
    elif len(dogChosen) > 1:
        print("Based on our quiz, your recommended dog breeds are the")
        for x in dogChosen[0: dogsShown]:
          print('')
          print(str(x.name) + ':')
          dogChosen.remove(x)

          time.sleep(sleepInterval)

          print(x.definition)
          print('')
        if len(dogChosen) >= dogsShown:
          print('Would you like to see more results?\n A. Yes\n B. No')
          print('')
          answer = input().lower()
          print('')
          if answer == 'a':
            print('Here are some other potential dog options for you:')
            print('')
            
            time.sleep(sleepInterval)
            
            for x in dogChosen[0: maxDogsShown]:
              print(x.name)
          elif answer == 'b':
            pass
          else:
            print('Sorry, ' + str(answer) + ' is not a valid response.')
            endTest(dogsShown)

    else:
        print("Sorry, we couldnt't find a dog that matched you.")
      
    print('')
    time.sleep(sleepInterval)
    print("Would you like to restart the quiz?\n A. Yes\n B. No")
    print('')
    answerRestart = input().lower()
    
    if answerRestart == 'a':
        dogChosen = list(dogList)
        clearConsole()
        startTest(startText) 
    elif answerRestart == 'b':
        print('')
        print(endText)
        print('')
        time.sleep(sleepInterval)
        sys.exit()
    else:
        print('')
        print("Sorry, " + answerRestart + " is not a valid response.")
        endTest(2)
    
#============================================================================================#

# Defines question function with variable number of questions and variable logic based on function input.

def standardQuestion(question):
    global dogChosen
    global dogList
    global questionsCompleted
    global chosenList
    global chosenHome
    global chosenSpace
    global chosenCost
    global sleepInterval
    global debug
    
    print('')
    print(question.questionAsked)
    for key in question.choices:
        print(' ' + key.upper() + '. ' + question.choices[key][0])
    
    print('')

    time.sleep(0.75)
    answer = input("  > ").lower()

    if answer in question.choices.keys():
        questionsCompleted += 1
        #logic switch that is defined by question function.
        if question.method == 'filter':
          if answer != 'd': #placeholder. 'd' is for no preference, meaning no dog gets removed.
            #looping through each dog.
              for x in dogChosen[:]:
                  #this logic is filter logic. remove entries based on answer against given trait defined in questions. Need to add new question.
                  if getattr(x,question.trait) != question.choices[answer][1]:  
                    dogChosen.remove(x)
                    dogExcluded.append(x)
                    endCheck(dogsShown)
        elif question.method == 'compare':
          valuesChosen[str(question.userValues)] = int(valuesChosen[question.userValues]) + int(question.choices[answer][1])
          endCheck(dogsShown)
          
    elif 'debug' in answer and debug == False:
      print('')  
      print('Debug mode is currently disabled.')
      print('')
      standardQuestion(question)
    # Debug commands 
    elif debug == True:
      if answer == 'debug.skip':
        print('')
        print("Question Skipped.") 
        print('')
      elif answer == 'debug.exit':
        print('')
        sys.exit('Program Exited.')
      elif answer == 'debug.skipquiz':
        print('')
        print('Quiz Skipped.')
        endTest(sleepInterval)
      elif answer == 'debug.dog':
        print('')
        print('Dogs currently in answer pool:')
        for x in dogChosen:
          print(x.name)
        print('')
        time.sleep(sleepInterval)
        standardQuestion(question)
      elif answer == 'debug.excluded':
        if len(dogExcluded) == 0:
          print('')
          print('No dogs currently excluded.')
        else:
          print('')
          print('Dogs currently not in answer pool:')
          for x in dogExcluded:
            print(x.name)
          print('')
        standardQuestion(question)
      elif answer == 'debug.restart':
        restartQuiz()
      elif answer == 'debug.userinfo':
        print('')
        print('User homeScore: ' + str(valuesChosen.get('chosenHome')))
        print('User spaceScore: ' + str(valuesChosen.get('chosenSpace')))
        print('User costScore: ' + str(valuesChosen.get('chosenCost')))
        print('')
        print('The user has completed ' + str(questionsCompleted) + ' question(s).')
        standardQuestion(question)
      elif answer == 'debug.clear':
        print('')
        print('Log will be cleared in 3 seconds.')
        time.sleep(sleepInterval)
        clearConsole()
        standardQuestion(question)
      elif answer == 'debug.endcheck':
        endCheck(dogsShown)
    elif answer not in question.choices.keys():
      print('')
      print('Sorry, ' + str(answer) + ' is not a valid response.')
      standardQuestion(question)

#============================================================================================#

# Starts text, and includes all question functions.

def startTest(quizHeader): 
  global chosenSpace
  global chosenCost
  global chosenHome
  global valuesChosen
  global dogsShown
  global startText
   
  clearConsole()
  
  print('')
  print(quizHeader)
  print('')
  print('')
  print("=================================================================")
  print('')
  print('')
  
  time.sleep(sleepInterval)
  
  standardQuestion(question1)
  standardQuestion(question2)
  standardQuestion(question3)
  standardQuestion(question4)
  standardQuestion(question5)
  standardQuestion(question6)
  standardQuestion(question7)
  standardQuestion(question8)
  standardQuestion(question9)
  
  removeCompare('spaceScore', 'chosenSpace')
  removeCompare('cost', 'chosenCost')
  removeCompare('homeScore', 'chosenHome')
  
  endTest(dogsShown)

#============================================================================================#

# Starts program
           
startTest(startText) 

#============================================================================================#
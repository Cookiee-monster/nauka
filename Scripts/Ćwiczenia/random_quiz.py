capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
   'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

import random
import os
folder = os.path.join('C:\\','Desktop', 'testy')

try: os.makedirs(folder)

except: print("Folder już istnieje")
os.chdir(folder)

# Generate 35 quiz files.
for quizNum in range(35):
    # Tworzenie 35 plików z quizem i odpowiedziami
    quiz_file = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answer_file = open('capitalsquiz%s_answers.txt' % (quizNum + 1), 'w')

    # Dodanie nagłówka w kązdym quizie:

    quiz_file.write('Name: \n\n Date: \n\n Period \n\n ')
    quiz_file.write(('' * 20) + 'State Capitals Quiz No%s' % (quizNum+1))
    quiz_file.write('\n\n')

    # Shuffle the order of states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Stworzenie pytań dla wszystkich stanów
    for questionnum in range(50):
        correctanswer = capitals[states[questionnum]]
        wronganswers = list(capitals.values())
        del wronganswers[wronganswers.index(correctanswer)]
        wronganswers = random.sample(wronganswers, 3)
        answeroptions = wronganswers + [correctanswer]
        random.shuffle(answeroptions)

        # Zapisanie pytań do plików
        quiz_file.write(' %s. What is the capitol '
                        'of %s?\n' % (questionnum + 1,
                                      states[questionnum]))
        for i in range(4):
            quiz_file.write('%s. %s\n ' % ('ABCD'[i], answeroptions[i]))
        quiz_file.write('\n')

        # Zapisanie odpowiedzi do plików
        answer_file.write('%s. %s\n' % (questionnum + 1, 'ABCD'[
            answeroptions.index(correctanswer)]))
    quiz_file.close()
    answer_file.close()

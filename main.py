#Braden Leach
#January 29 2024
#Python Trivia


#---Python Trivia Game---#
score = 0 
questions = [
    {
        'question': 'In the game Halo, what is the name of Master Chief\'s AI sidekick? Microsoft later re-used this name for their own product?',
        'answer':'Cortana'
    },
    {
        'question': 'Sun, Moon, Diamond, Pearl, and SoulSilver have all been names of games in what iconic video game franchise?',
        'answer':'Pokemon'
    },
    {
        'question': 'Skyrim is the fifth installment of what epic open-world videogame series by Bethesda Softworks?',
        'answer':'Elder Scrolls'
    },
    {
        'question': 'What gothic video game franchise debuted in 1986 with Simon Belmont as protagonist? Simon was a member of the Belmont clan, a family of vampire hunters.',
        'answer':'Castlevania'
    },
    {
        'question': 'The website Ranker named GLaDOS, a fictional artificially intelligent computer system, the greatest video game villain of all time. GLaDOS was introduced in what groundbreaking computer game?',
        'answer':'Portal'
    }
]
#---Loop Questions---#
for question in questions:
    #--Question--#
    question_text = question.get('question')
    print(f'\n{question_text}')

    #--Answer--#
    user_answer = input("Enter answer: ").title()
    correct_answer = question.get('answer')
    if user_answer == correct_answer:
        score += 10

#---Print---#
print('\nYour score =',  score)#--Print score at end


#---Score Response---#
if score <= 20:
    print('you got a low score, run again to try and get higher!\n')
else:
    print('You got a high score, good job!\n')
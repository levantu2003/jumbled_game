import random

words = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
print(f'These are the words: {words}')
word = random.choice(words)
jumble = ' '.join(random.sample(word, len(word)))
print(f'The jumble word is {jumble}')
answer = input('What is your answer? ')
if answer == word:
      print('Correct!')
else:
      print(f'Incorrect. The answer is {word}')
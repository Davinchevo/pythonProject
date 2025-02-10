from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'hangman_word' not in session:
        # This is where we initialize the game when the page loads for the first time
        hangman_word = input("Enter a word: ")  # Getting the word for the game
        session['hangman_word'] = hangman_word
        session['lives'] = 6
        session['incorrect_guesses'] = ''
        session['guessed_word'] = '*' * len(hangman_word)
        
    if request.method == 'POST':
        input_char = request.form['guess']
        if len(input_char) != 1:
            return render_template('index.html', guessed_word=session['guessed_word'], lives=session['lives'],
                                   incorrect_guesses=session['incorrect_guesses'], message="Please guess one character.")
        
        # Game logic for guessing the character
        if input_char in session['incorrect_guesses'] or input_char in session['guessed_word']:
            return render_template('index.html', guessed_word=session['guessed_word'], lives=session['lives'],
                                   incorrect_guesses=session['incorrect_guesses'], message="You have already guessed that character.")

        guessed = False
        for i in range(len(session['hangman_word'])):
            if input_char == session['hangman_word'][i]:
                session['guessed_word'] = session['guessed_word'][:i] + input_char + session['guessed_word'][i+1:]
                guessed = True

        if guessed:
            message = "Correct guess!"
        else:
            session['lives'] -= 1
            session['incorrect_guesses'] += input_char
            message = f"Wrong guess! You have {session['lives']} lives left."
        
        # Check if the player has won
        if '*' not in session['guessed_word']:
            message = f"You won! The word was: {session['guessed_word']}"
            session.pop('hangman_word', None)  # End the game by removing the word

        # Check if the player lost
        if session['lives'] <= 0:
            message = f"You lost! The word was: {session['hangman_word']}"
            session.pop('hangman_word', None)  # End the game by removing the word

        return render_template('index.html', guessed_word=session['guessed_word'], lives=session['lives'],
                               incorrect_guesses=session['incorrect_guesses'], message=message)

    return render_template('index.html', guessed_word=session['guessed_word'], lives=session['lives'],
                           incorrect_guesses=session['incorrect_guesses'], message="Start guessing!")

if __name__ == "__main__":
    app.run(debug=True)

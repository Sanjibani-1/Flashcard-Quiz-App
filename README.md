# Flashcard-Quiz-App


This code implements a basic Flashcard Quiz App using Python's tkinter library for the graphical user interface (GUI). Below is a breakdown of its components and how it functions:

1. Class Definition (FlashcardApp)
The main class FlashcardApp handles the flashcard app logic and GUI setup. It accepts root, which is a tk.Tk() object that represents the main window of the application.
The class keeps track of flashcards, the current question index, correct answers, and total questions asked.
2. Instance Variables
self.flashcards: A list to store tuples of questions and answers.
self.current_index: Tracks the index of the flashcard currently being shown in the quiz.
self.correct_answers: Tracks the number of correctly answered questions.
self.total_questions: Stores the total number of questions available in the quiz.
3. GUI Components
Labels: tk.Label components for showing "Question" and "Answer" fields to the user.
Entry Widgets: tk.Entry fields for the user to input questions and answers.
Buttons:
Add Flashcard: Adds the current question and answer to the flashcards list.
Start Quiz: Starts the quiz, allowing the user to answer the flashcards one by one.
4. Core Functions
add_flashcard():

Adds a flashcard (question, answer) to the list.
Clears the input fields after adding.
Alerts the user if either the question or answer field is left empty.
start_quiz():

Initiates the quiz if flashcards exist.
Resets the correct answer count and shows the first flashcard.
Warns the user if no flashcards are available.
show_flashcard():

Displays the current flashcard's question.
Allows the user to input their answer and check it by clicking "Submit".
If the answer is correct, the correct answer count is incremented.
A message box informs the user if their answer was correct or incorrect, along with the correct answer.
After submitting an answer, the app moves to the next flashcard.
show_score():

Displays the total score at the end of the quiz.
Offers buttons to restart the quiz or quit the application.
5. Quiz Flow
When the "Start Quiz" button is clicked, the app switches to quiz mode.
It displays each flashcard question in sequence and prompts the user to submit their answer.
Once all flashcards are answered, it shows the user's score and gives options to either restart the quiz or quit.
6. Use of Message Boxes
The messagebox module from tkinter is used to:
Inform the user of the success of flashcard addition.
Alert the user about empty input fields or missing flashcards for the quiz.
Give feedback on correct/incorrect answers during the quiz.
7. Restart and Quit Options
After the quiz ends, users can restart it (which resets the quiz state) or quit the application via buttons.
Summary of Flow:
User adds flashcards (question-answer pairs).
They click "Start Quiz" to begin.
The app shows one question at a time, allowing the user to input their answer.
After all questions are answered, the app displays the score and gives options to restart or quit.

import tkinter as tk
from tkinter import messagebox


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")

        self.flashcards = []  # List to store flashcards (question, answer)
        self.current_index = 0  # To track which flashcard is being shown
        self.correct_answers = 0  # To track correct answers
        self.total_questions = 0  # Total questions asked

        # GUI components
        self.question_label = tk.Label(root, text="Question:", font=('Arial', 16))
        self.question_label.pack(pady=10)

        self.question_entry = tk.Entry(root, width=50)
        self.question_entry.pack(pady=5)

        self.answer_label = tk.Label(root, text="Answer:", font=('Arial', 16))
        self.answer_label.pack(pady=10)

        self.answer_entry = tk.Entry(root, width=50)
        self.answer_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Flashcard", command=self.add_flashcard)
        self.add_button.pack(pady=10)

        self.quiz_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.quiz_button.pack(pady=10)

        self.quiz_frame = tk.Frame(root)
        self.quiz_frame.pack(pady=10)

    def add_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()

        if question and answer:
            self.flashcards.append((question, answer))
            messagebox.showinfo("Success", "Flashcard Added!")
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Please enter both a question and an answer.")

    def start_quiz(self):
        if self.flashcards:
            self.current_index = 0
            self.correct_answers = 0
            self.total_questions = len(self.flashcards)
            self.show_flashcard()
        else:
            messagebox.showwarning("Error", "No flashcards available to quiz.")

    def show_flashcard(self):
        # Clear previous quiz elements
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        if self.current_index < len(self.flashcards):
            question, answer = self.flashcards[self.current_index]

            question_label = tk.Label(self.quiz_frame, text=f"Question: {question}", font=('Arial', 16))
            question_label.pack(pady=10)

            user_answer_entry = tk.Entry(self.quiz_frame, width=50)
            user_answer_entry.pack(pady=5)

            def check_answer():
                user_answer = user_answer_entry.get()
                if user_answer.lower() == answer.lower():
                    self.correct_answers += 1
                    messagebox.showinfo("Correct!", "You got it right!")
                else:
                    messagebox.showinfo("Incorrect", f"The correct answer was: {answer}")

                self.current_index += 1
                self.show_flashcard()

            submit_button = tk.Button(self.quiz_frame, text="Submit", command=check_answer)
            submit_button.pack(pady=10)
        else:
            self.show_score()

    def show_score(self):
        # Clear quiz frame
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        score_label = tk.Label(self.quiz_frame, text=f"Quiz Finished!\nScore: {self.correct_answers}/{self.total_questions}", font=('Arial', 16))
        score_label.pack(pady=10)

        restart_button = tk.Button(self.quiz_frame, text="Restart Quiz", command=self.start_quiz)
        restart_button.pack(pady=10)

        quit_button = tk.Button(self.quiz_frame, text="Quit", command=self.root.quit)
        quit_button.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

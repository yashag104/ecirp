from tkinter import *
from quiz_brain import QuizBrain
from self import self

THEME_COLOR = "#375362"


class UI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.answer = None

        self.windows = Tk()
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)
        self.windows.title("Quizzer")

        self.canvas = Canvas(self.windows, highlightthickness=0, height=250, width=300, )
        self.question = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.score = Label(text="Score: 0", font=("Arial", 20), bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(self.windows, image=false_img, highlightthickness=0, command=self.false_button_click)
        self.false_button.grid(column=1, row=2, padx=10, pady=10)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(self.windows, image=true_img, highlightthickness=0, command=self.true_button_click)
        self.true_button.grid(column=0, row=2, padx=10, pady=10)

        self.get_next_question()

        self.windows.mainloop()

    def true_button_click(self):
        self.check_answer("True")

    def false_button_click(self):
        self.check_answer("False")

    def check_answer(self, answer):
        if self.quiz.check_question(answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.get_next_question)
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.question_number == 10:
            self.windows.after(1000, self.windows.destroy)

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question, text=self.quiz.next_question())

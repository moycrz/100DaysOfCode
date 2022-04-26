from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        r_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=r_button_img, highlightthickness=0, command=self.get_check_answer)
        self.right_button.grid(column=0, row=2)

        w_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=w_button_img, highlightthickness=0, command=self.get_check_answer)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        try:
            q_text = self.quiz.next_question()
        except IndexError:
            self.canvas.itemconfig(self.question_text, text="Game Over")
        else:
            self.canvas.itemconfig(self.question_text, text=q_text)

    def get_check_answer(self):
        correct_answer = self.quiz.check_answer("True")
        score = self.quiz.score
        if correct_answer:
            self.score_label.config(text=f"Score: {score}")
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_feedback)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_feedback)

    def get_feedback(self):
        self.canvas.config(bg="white")
        self.get_next_question()

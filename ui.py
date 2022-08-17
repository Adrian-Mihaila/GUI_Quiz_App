from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # Create a quiz_brain object with QuizBrain data type
        self.quiz = quiz_brain  # Create a propriety from a file
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 10, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=40)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="",
            font=("Arial", 17, "italic"),
            fill=THEME_COLOR)

        true_button_image = PhotoImage(file="C:/Users/night/PycharmProjects/Day_34_GUI_Quiz_App/images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0,
                                  bg=THEME_COLOR, command=self.true_button)
        self.true_button.grid(row=2, column=0, pady=20)

        false_button_image = PhotoImage(file="C:/Users/night/PycharmProjects/Day_34_GUI_Quiz_App/images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0,
                                   bg=THEME_COLOR, command=self.false_button)
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true_button.config(state="disabled")  # DISABLE THE BUTTON
            self.false_button.config(state="disabled")  # DISABLE THE BUTTON

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)  # choose function, don't call it like this get_next_question()

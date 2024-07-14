import tkinter as tk
import random

class Hangman:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("1600x1000")
        self.wordlist = ["revolve","maker", "paste", "joker", "adieu", "hunger", "magic"]
        self.word = self.choose_word()
        self.attempts = 7
        self.incorrect = set()
        self.correct = set()
        self.createcanvas()

    def createcanvas(self):
        self.canvasframe = tk.Frame(self.master, width=1600, height=1000, bg="#A1ACC2", bd=20, relief="ridge")
        self.canvasframe.pack_propagate(False)
        self.canvasframe.pack()
        titleframe = tk.Frame(self.canvasframe, width=1600, height=150, bg="#A1ACC2")
        titleframe.pack_propagate(False)
        titleframe.pack()
        header = tk.Label(titleframe, text="Welcome to Hangman game", font="Helvetica 50 bold", fg="navyblue", bg="#A1ACC2")
        header.pack(pady=20)
        self.drawingframe = tk.Canvas(self.canvasframe, width=300, height=300, bg="white")
        self.drawingframe.pack_propagate(False)
        self.drawingframe.pack(pady=10)
        self.questionframe = tk.Label(self.canvasframe, text="_ " * len(self.word), font="helvetica 30", bg="#A1ACC2",fg="black")
        self.questionframe.pack(pady=20)
        self.reset = tk.Button(self.canvasframe, text="Reset Game", font="helvetica 20 bold", bg="navyblue", fg="white", command=self.reset_game)
        self.reset.pack(pady=20)
        self.buttons = tk.Frame(self.canvasframe)
        self.buttons.pack(pady=20)
        self.create_alpha()

    def create_alpha(self):
        button_bg = "black"
        button_fg = "white"
        button_font = "Helvetica 13 bold"

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper_row = alphabet[:13]
        lower_row = alphabet[13:]

        upper_frame = tk.Frame(self.buttons)
        upper_frame.pack()
        lower_frame = tk.Frame(self.buttons)
        lower_frame.pack()

        for letter in upper_row:
            button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=2, pady=2)

        for letter in lower_row:
            button = tk.Button(lower_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=2, pady=2)

    def choose_word(self):
        return random.choice(self.wordlist).upper()

    def guess_letter(self, letter):
        if letter in self.word:
            self.correct.add(letter)
        elif letter not in self.incorrect:
            self.incorrect.add(letter)
            self.attempts -= 1
            self.update()
            
        self.word_update()

    def word_update(self):

        display_word = ""
        for word_letter in self.word:
            if word_letter in self.correct:
                display_word += word_letter + " "
            else:
                display_word += "_ "

        self.questionframe.config(text=display_word)

        self.check_game_over(display_word.strip().replace(" ", ""))

    def update(self):
        self.drawingframe.delete("all")
        stages = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm,
                  self.draw_left_leg, self.draw_right_leg, self.draw_face]
        for i in range(len(self.incorrect)):
            if i < len(stages):
                stages[i]()

    def draw_head(self):
        self.drawingframe.create_oval(125, 50, 185, 110, outline="black")

    def draw_body(self):
        self.drawingframe.create_line(155, 110, 155, 170, fill="black")

    def draw_left_arm(self):
        self.drawingframe.create_line(155, 130, 125, 150, fill="black")

    def draw_right_arm(self):
        self.drawingframe.create_line(155, 130, 185, 150, fill="black")

    def draw_left_leg(self):
        self.drawingframe.create_line(155, 170, 125, 200, fill="black")

    def draw_right_leg(self):
        self.drawingframe.create_line(155, 170, 185, 200, fill="black")

    def draw_face(self):
        self.drawingframe.create_line(140, 70, 150, 80, fill="black")
        self.drawingframe.create_line(160, 70, 170, 80, fill="black")
        self.drawingframe.create_arc(140, 85, 170, 105, start=0, extent=-180, fill="black")


    def check_game_over(self, display_word):
        if display_word == self.word:
            self.display_game_over_message("Congratulations, you've won!")
        elif self.attempts == 0:
            self.display_game_over_message(f"Game over!! :( The word was: {self.word}")

    def display_game_over_message(self, message):
        self.buttons.pack_forget()
        self.reset.pack_forget()
        self.questionframe.pack_forget()

        self.game_over = tk.Label(self.canvasframe, text=message, font="Helvetica 30 bold", fg="darkred", bg="#A1ACC2", bd=2)
        self.game_over.pack(pady = 20)

        if not hasattr(self, 'restart_button'):
            self.restart_button = tk.Button(self.canvasframe, text="Restart Game", command=self.reset_game, width=20, height=2, bg="navyblue", fg="white", font="helvetica 20 bold")
        self.restart_button.pack(pady=20)

    def reset_game(self):
        self.word = self.choose_word()
        self.correct = set()
        self.incorrect = set()
        self.attempts = 7

        self.drawingframe.delete("all")
        display_word = "_ " * len(self.word)
        self.questionframe.config(text=display_word)

        for frame in self.buttons.winfo_children():
            for button in frame.winfo_children():
                button.configure(state=tk.NORMAL)

        if hasattr(self, 'game_over') and self.game_over.winfo_exists():
            self.game_over.pack_forget()
        if hasattr(self, 'restart_button') and self.restart_button.winfo_exists():
            self.restart_button.pack_forget()

        self.questionframe.pack(pady=20)
        self.reset.pack(pady=20)
        self.buttons.pack(pady=20)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Hangman(root)
    root.mainloop()


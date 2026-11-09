import tkinter as tk
from tkinter import font as tkfont

QUESTIONS = [
    "What was the last song you listened to?",
    "Do you remember when our last lesson was?",
    "What do you want to feel when you enter a room?",
    "Which environments attract you and which ones make you uncomfortable?",
    "How would you use the space?",
    
]


class FlashCardApp:
    BG_COLOR = "#556B2F"       # фон
    CARD_COLOR = "#FF00FF"     # цвет карточки
    ACCENT = "#FF1493"         # акцент (кнопка/прогресс)
    TEXT_COLOR = "#f5f5fa"
    MUTED = "#FF00FF"

    def __init__(self, root):
        self.root = root
        self.root.title("Question cards")
        self.root.geometry("600x420")
        self.root.configure(bg=self.BG_COLOR)
        self.root.resizable(False, False)

        self.index = 0

        # Шрифты
        self.title_font = tkfont.Font(family="Palace Script MT", size=80, weight="bold")
        self.card_font = tkfont.Font(family="DotumChe", size=16, weight="bold")
        self.small_font = tkfont.Font(family="Palace Script MT", size=22)

        # Верхняя панель со счётчиком
        self.counter_label = tk.Label(
            root, text="", font=self.small_font,
            bg=self.BG_COLOR, fg=self.MUTED
        )
        self.counter_label.pack(pady=(25, 10))

        # Контейнер "карточки"
        self.card_frame = tk.Frame(
            root, bg=self.CARD_COLOR,
            highlightbackground=self.ACCENT,
            highlightthickness=2,
            bd=0
        )
        self.card_frame.pack(padx=40, pady=10, fill="both", expand=True)

        # Текст вопроса
        self.question_label = tk.Label(
            self.card_frame, text="", font=self.card_font,
            bg=self.CARD_COLOR, fg=self.TEXT_COLOR,
            wraplength=460, justify="center"
        )
        self.question_label.pack(expand=True, padx=25, pady=25)

        # Кнопки внизу
        btn_frame = tk.Frame(root, bg=self.BG_COLOR)
        btn_frame.pack(pady=20)

        self.prev_btn = self._make_button(btn_frame, "◀ Home", self.prev_card)
        self.prev_btn.pack(side="left", padx=10)

        self.next_btn = self._make_button(btn_frame, "End ▶", self.next_card)
        self.next_btn.pack(side="left", padx=10)

        # Привязка клавиш
        root.bind("<Left>", lambda e: self.prev_card())
        root.bind("<Right>", lambda e: self.next_card())
        root.bind("<space>", lambda e: self.next_card())

        self.update_card()

    def _make_button(self, parent, text, command):
        btn = tk.Button(
            parent, text=text, command=command,
            font=self.small_font,
            bg=self.ACCENT, fg="white",
            activebackground="#FF00FF",
            activeforeground="white",
            relief="flat", bd=0,
            padx=22, pady=10,
            cursor="hand2"
        )
        # Плавная смена цвета при наведении
        btn.bind("<Enter>", lambda e: btn.config(bg="#FF00FF"))
        btn.bind("<Leave>", lambda e: btn.config(bg=self.ACCENT))
        return btn

    def update_card(self):
        # Плавное появление — обновляем текст и подпись
        self.question_label.config(text=QUESTIONS[self.index])
        self.counter_label.config(
            text=f"Card {self.index + 1} of {len(QUESTIONS)}"
        )
        # Блокируем кнопку «Назад» на первой карточке
        state = "normal" if self.index > 0 else "disabled"
        self.prev_btn.config(
            state=state,
            bg=self.ACCENT if state == "normal" else "#FF69B4",
            disabledforeground=self.MUTED
        )

    def next_card(self):
        if self.index < len(QUESTIONS) - 1:
            self.index += 1
            self.update_card()

    def prev_card(self):
        if self.index > 0:
            self.index -= 1
            self.update_card()


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashCardApp(root)
    root.mainloop()
import tkinter as tk
import random
import time

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect, so keep typing.",
    "Python is a great programming language to learn.",
    "Typing fast and accurately is a valuable skill.",
    "Stay focused and don't rush while typing."
]

class TypingTutor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typist.com‑style Typing Tutor")
        self.geometry("800x300")
        self.resizable(False, False)
        
        self.target_text = random.choice(sentences)
        self.start_time = None
        
        # Display target sentence
        self.prompt = tk.Text(self, height=2, wrap="word", padx=10, pady=10, font=("Consolas", 16))
        self.prompt.insert("1.0", self.target_text)
        self.prompt.config(state="disabled")
        self.prompt.pack(pady=(20,10))
        
        # Input widget
        self.input_box = tk.Text(self, height=2, wrap="word", padx=10, pady=10, font=("Consolas", 16))
        self.input_box.pack()
        self.input_box.bind("<KeyRelease>", self.on_type)
        
        # Stats labels
        self.status = tk.Label(self, text="Start typing to begin...", font=("Arial", 14))
        self.status.pack(pady=(10,0))
        
    def on_type(self, event):
        content = self.input_box.get("1.0", "end-1c")
        if not content:
            return
        
        if self.start_time is None:
            self.start_time = time.time()
        
        # Color feedback
        self.input_box.tag_remove("correct", "1.0", "end")
        self.input_box.tag_remove("incorrect", "1.0", "end")
        
        correct_chars = 0
        for i, ch in enumerate(content):
            target_ch = self.target_text[i] if i < len(self.target_text) else ""
            tag = "correct" if ch == target_ch else "incorrect"
            self.input_box.tag_add(tag, f"1.{i}", f"1.{i+1}")
            if ch == target_ch:
                correct_chars += 1
        
        self.input_box.tag_config("correct", foreground="green")
        self.input_box.tag_config("incorrect", foreground="red")
        
        elapsed = time.time() - self.start_time
        words_typed = len(content.split())
        wpm = (words_typed / elapsed) * 60 if elapsed > 0 else 0
        accuracy = (correct_chars / len(self.target_text)) * 100
        
        self.status.config(text=f"WPM: {wpm:.1f}    Accuracy: {accuracy:.1f}%")
        
        # Completed?
        if content == self.target_text:
            total_time = elapsed
            final_wpm = (len(content.split()) / total_time) * 60
            final_acc = (correct_chars / len(self.target_text)) * 100
            self.status.config(text=f"🎉 Finished! Time: {total_time:.1f}s | WPM: {final_wpm:.1f} | Accuracy: {final_acc:.1f}%")
            self.input_box.config(state="disabled")

if __name__ == "__main__":
    app = TypingTutor()
    app.mainloop()

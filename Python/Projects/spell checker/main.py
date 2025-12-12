import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from textblob import TextBlob
from textblob import Word
import re

class SpellCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Spell Checker")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Configure styles
        self.setup_styles()
        
        # Create GUI
        self.create_widgets()
        
        # Word dictionary for custom words
        self.custom_dictionary = set()
        self.load_custom_dictionary()
    
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        self.colors = {
            'bg': '#f0f0f0',
            'fg': '#333333',
            'button_bg': '#4CAF50',
            'button_fg': 'white',
            'error_bg': '#ffebee',
            'correct_bg': '#e8f5e9'
        }
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="🔤 Advanced Spell Checker",
            font=("Arial", 24, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        title_label.pack(pady=20)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg=self.colors['bg'])
        input_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Input Label
        input_label = tk.Label(
            input_frame,
            text="Enter your text:",
            font=("Arial", 12, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        input_label.pack(anchor="w", pady=(0, 5))
        
        # Text Input Area
        self.text_input = scrolledtext.ScrolledText(
            input_frame,
            height=10,
            width=80,
            font=("Arial", 11),
            wrap=tk.WORD,
            bg="white",
            fg="black",
            relief=tk.SOLID,
            borderwidth=1
        )
        self.text_input.pack(fill="both", expand=True)
        self.text_input.bind("<KeyRelease>", self.real_time_check)
        
        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg=self.colors['bg'])
        buttons_frame.pack(pady=20)
        
        # Check Button
        check_button = tk.Button(
            buttons_frame,
            text="Check Spelling",
            command=self.check_spelling,
            bg=self.colors['button_bg'],
            fg=self.colors['button_fg'],
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        check_button.grid(row=0, column=0, padx=10)
        
        # Auto Correct Button
        autocorrect_button = tk.Button(
            buttons_frame,
            text="Auto Correct",
            command=self.auto_correct,
            bg="#2196F3",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        autocorrect_button.grid(row=0, column=1, padx=10)
        
        # Clear Button
        clear_button = tk.Button(
            buttons_frame,
            text="Clear Text",
            command=self.clear_text,
            bg="#ff9800",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        clear_button.grid(row=0, column=2, padx=10)
        
        # Results Frame
        results_frame = tk.Frame(self.root, bg=self.colors['bg'])
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Results Label
        results_label = tk.Label(
            results_frame,
            text="Spelling Suggestions:",
            font=("Arial", 12, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        results_label.pack(anchor="w", pady=(0, 5))
        
        # Results Text Area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            height=8,
            width=80,
            font=("Arial", 10),
            wrap=tk.WORD,
            bg="white",
            fg="black",
            relief=tk.SOLID,
            borderwidth=1,
            state="disabled"
        )
        self.results_text.pack(fill="both", expand=True)
        
        # Stats Frame
        stats_frame = tk.Frame(self.root, bg=self.colors['bg'])
        stats_frame.pack(fill="x", padx=20, pady=10)
        
        # Word Count
        self.word_count_label = tk.Label(
            stats_frame,
            text="Words: 0 | Characters: 0",
            font=("Arial", 10),
            bg=self.colors['bg'],
            fg="#666666"
        )
        self.word_count_label.pack(side="left")
        
        # Error Count
        self.error_count_label = tk.Label(
            stats_frame,
            text="Errors: 0",
            font=("Arial", 10),
            bg=self.colors['bg'],
            fg="#f44336"
        )
        self.error_count_label.pack(side="right")
        
        # Custom Dictionary Frame
        dict_frame = tk.Frame(self.root, bg=self.colors['bg'])
        dict_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Add to Dictionary
        dict_label = tk.Label(
            dict_frame,
            text="Add word to dictionary:",
            font=("Arial", 10),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        dict_label.pack(side="left", padx=(0, 10))
        
        self.dict_entry = tk.Entry(
            dict_frame,
            font=("Arial", 10),
            width=20
        )
        self.dict_entry.pack(side="left", padx=(0, 10))
        
        add_dict_button = tk.Button(
            dict_frame,
            text="Add",
            command=self.add_to_dictionary,
            bg="#9c27b0",
            fg="white",
            font=("Arial", 10),
            padx=10
        )
        add_dict_button.pack(side="left")
    
    def check_spelling(self):
        """Check spelling in the text"""
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("No Text", "Please enter some text to check.")
            return
        
        # Clear previous highlights
        self.clear_highlights()
        
        # Get words from text
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        total_words = len(words)
        errors = 0
        
        # Check each word
        suggestions_text = ""
        for word in words:
            w = Word(word.lower())
            suggestions = w.spellcheck()
            
            if word.lower() in self.custom_dictionary:
                continue  # Skip custom dictionary words
            
            if not suggestions or suggestions[0][0].lower() != word.lower():
                errors += 1
                # Highlight incorrect word
                self.highlight_word(word)
                
                # Get suggestions
                if suggestions:
                    suggestions_text += f"❌ '{word}' → Suggestions: "
                    for i, (suggestion, confidence) in enumerate(suggestions[:3]):
                        suggestions_text += f"'{suggestion}' ({confidence*100:.0f}%)"
                        if i < 2:
                            suggestions_text += ", "
                    suggestions_text += "\n"
                else:
                    suggestions_text += f"❌ '{word}' → No suggestions found\n"
        
        # Update results
        self.update_results(suggestions_text, total_words, errors)
    
    def auto_correct(self):
        """Auto-correct the text"""
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("No Text", "Please enter some text to correct.")
            return
        
        # Create TextBlob object
        blob = TextBlob(text)
        
        # Correct spelling
        corrected_text = str(blob.correct())
        
        # Update text input
        self.text_input.delete("1.0", tk.END)
        self.text_input.insert("1.0", corrected_text)
        
        # Show message
        messagebox.showinfo("Auto Correct", "Text has been auto-corrected!")
        
        # Update word count
        self.update_word_count()
    
    def real_time_check(self, event=None):
        """Real-time spell checking"""
        self.update_word_count()
    
    def highlight_word(self, word):
        """Highlight a misspelled word in the text"""
        text = self.text_input.get("1.0", tk.END)
        start_index = "1.0"
        
        while True:
            # Search for the word
            pos = self.text_input.search(r'\b' + word + r'\b', start_index, tk.END, regexp=True)
            
            if not pos:
                break
            
            # Calculate end position
            line, col = map(int, pos.split('.'))
            end_pos = f"{line}.{col + len(word)}"
            
            # Add tag for highlighting
            self.text_input.tag_add("highlight", pos, end_pos)
            self.text_input.tag_config("highlight", background="#ffcdd2", foreground="black")
            
            # Move to next occurrence
            start_index = end_pos
    
    def clear_highlights(self):
        """Clear all highlights from text"""
        self.text_input.tag_remove("highlight", "1.0", tk.END)
    
    def update_results(self, suggestions_text, total_words, errors):
        """Update results text area"""
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        
        if suggestions_text:
            self.results_text.insert("1.0", suggestions_text)
        else:
            self.results_text.insert("1.0", "✅ No spelling errors found!\n")
        
        self.results_text.config(state="disabled")
        
        # Update error count
        self.error_count_label.config(text=f"Errors: {errors}")
        
        # Update stats
        chars = len(self.text_input.get("1.0", tk.END)) - 1
        self.word_count_label.config(text=f"Words: {total_words} | Characters: {chars}")
    
    def update_word_count(self):
        """Update word count statistics"""
        text = self.text_input.get("1.0", tk.END).strip()
        words = text.split()
        chars = len(text)
        self.word_count_label.config(text=f"Words: {len(words)} | Characters: {chars}")
    
    def clear_text(self):
        """Clear all text"""
        self.text_input.delete("1.0", tk.END)
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.config(state="disabled")
        self.clear_highlights()
        self.update_word_count()
        self.error_count_label.config(text="Errors: 0")
    
    def add_to_dictionary(self):
        """Add word to custom dictionary"""
        word = self.dict_entry.get().strip().lower()
        
        if not word:
            messagebox.showwarning("No Word", "Please enter a word to add to dictionary.")
            return
        
        if word in self.custom_dictionary:
            messagebox.showinfo("Already Exists", f"'{word}' is already in the dictionary.")
            return
        
        # Add to dictionary
        self.custom_dictionary.add(word)
        
        # Save to file
        self.save_custom_dictionary()
        
        # Clear entry
        self.dict_entry.delete(0, tk.END)
        
        messagebox.showinfo("Success", f"'{word}' has been added to your custom dictionary.")
    
    def load_custom_dictionary(self):
        """Load custom dictionary from file"""
        try:
            with open("custom_dictionary.txt", "r") as f:
                for line in f:
                    word = line.strip().lower()
                    if word:
                        self.custom_dictionary.add(word)
        except FileNotFoundError:
            # Create empty file if it doesn't exist
            with open("custom_dictionary.txt", "w") as f:
                pass
    
    def save_custom_dictionary(self):
        """Save custom dictionary to file"""
        with open("custom_dictionary.txt", "w") as f:
            for word in sorted(self.custom_dictionary):
                f.write(word + "\n")

def main():
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
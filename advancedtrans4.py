#The provided code uses Tkinter for a GUI application. It manages a dictionary of words, allowing users to add, search, delete, update, and export words. It also offers dark mode functionality for a personalized interface.

import tkinter as tk
from tkinter import messagebox, filedialog
import csv

def load_words():
    try:
        with open("words.txt", "r") as file:
            lines = file.readlines()
            word_dict = {}
            for line in lines:
                word, meaning = line.strip().split(":")
                word_dict[meaning.strip().lower()] = word.strip().lower()  # Swap the key-value pair
            return word_dict
    except FileNotFoundError:
        return {}

def save_words(word_dict):
    with open("words.txt", "w") as file:
        for meaning, word in word_dict.items():  # Swap the items
            file.write(f"{word}:{meaning}\n")

def add_word():
    meaning = entry_word.get().strip().lower()
    word = entry_meaning.get().strip().lower()  # Swap the meaning and word
    
    if word and meaning:
        word_dict[meaning] = word  # Swap the key-value pair
        save_words(word_dict)
        listbox_translated.insert(tk.END, f"{meaning}: {word}")
        messagebox.showinfo("Success", f"Added '{meaning}' to the dictionary!")
    else:
        messagebox.showerror("Error", "Please enter both word and meaning.")

def translate_word_by_word():
    sentence = entry_word_by_word.get()
    translated_sentence = ' '.join([word_dict.get(word.lower(), word) for word in sentence.split()])
    entry_translated_word_by_word.delete(0, tk.END)
    entry_translated_word_by_word.insert(0, translated_sentence)

def search_words():
    query = entry_search.get().strip().lower()
    if query:
        filtered_words = {meaning: word for meaning, word in word_dict.items() if query in meaning}
        listbox_translated.delete(0, tk.END)
        for meaning, word in filtered_words.items():
            listbox_translated.insert(tk.END, f"{meaning}: {word}")
    else:
        listbox_translated.delete(0, tk.END)
        for meaning, word in word_dict.items():
            listbox_translated.insert(tk.END, f"{meaning}: {word}")

def delete_word():
    selected_index = listbox_translated.curselection()
    if selected_index:
        meaning = listbox_translated.get(selected_index).split(":")[0].strip()
        del word_dict[meaning.lower()]
        save_words(word_dict)
        listbox_translated.delete(selected_index)
        messagebox.showinfo("Success", f"Deleted '{meaning}' from the dictionary.")
    else:
        messagebox.showerror("Error", "Please select a word to delete.")

def update_word():
    selected_index = listbox_translated.curselection()
    if selected_index:
        meaning = listbox_translated.get(selected_index).split(":")[0].strip()
        new_word = entry_word.get().strip().lower()
        if new_word:
            word_dict[meaning] = new_word
            save_words(word_dict)
            listbox_translated.delete(selected_index)
            listbox_translated.insert(selected_index, f"{meaning}: {new_word}")
            messagebox.showinfo("Success", f"Updated '{meaning}' in the dictionary.")
        else:
            messagebox.showerror("Error", "Please enter a new word.")
    else:
        messagebox.showerror("Error", "Please select a word to update.")

def word_frequency_analysis():
    word_freq = {}
    for word in word_dict.values():
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    messagebox.showinfo("Word Frequency Analysis", f"Word Frequency Analysis:\n\n{word_freq}")

def export_dictionary():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for meaning, word in word_dict.items():
                writer.writerow([word, meaning])
        messagebox.showinfo("Export Dictionary", "Dictionary exported successfully!")

def toggle_dark_mode():
    if dark_mode.get():
        root.config(bg="#333")
        header_frame.config(bg="#333")
        word_frame.config(bg="#333")
        translation_frame.config(bg="#333")
        label_word.config(fg="white", bg="#333")
        label_meaning.config(fg="white", bg="#333")
        label_word_by_word.config(fg="white", bg="#333")
        label_translated_word_by_word.config(fg="white", bg="#333")
        label_search.config(fg="white", bg="#333")
        label_translated_words.config(fg="white", bg="#333")
        listbox_translated.config(bg="#555", fg="white")
        button_add.config(bg="#555", fg="white")
        button_translate_word_by_word.config(bg="#555", fg="white")
        button_search.config(bg="#555", fg="white")
        button_delete.config(bg="#555", fg="white")
        button_update.config(bg="#555", fg="white")
        button_frequency_analysis.config(bg="#555", fg="white")
        button_export_dict.config(bg="#555", fg="white")
    else:
        root.config(bg="#e0e0e0")
        header_frame.config(bg="#e0e0e0")
        word_frame.config(bg="#e0e0e0")
        translation_frame.config(bg="#e0e0e0")
        label_word.config(fg="black", bg="#e0e0e0")
        label_meaning.config(fg="black", bg="#e0e0e0")
        label_word_by_word.config(fg="black", bg="#e0e0e0")
        label_translated_word_by_word.config(fg="black", bg="#e0e0e0")
        label_search.config(fg="black", bg="#e0e0e0")
        label_translated_words.config(fg="black", bg="#e0e0e0")
        listbox_translated.config(bg="white", fg="black")
        button_add.config(bg="#333", fg="white")
        button_translate_word_by_word.config(bg="#333", fg="white")
        button_search.config(bg="#333", fg="white")
        button_delete.config(bg="#333", fg="white")
        button_update.config(bg="#333", fg="white")
        button_frequency_analysis.config(bg="#333", fg="white")
        button_export_dict.config(bg="#333", fg="white")

root = tk.Tk()
root.title("Advanced ML Translation Innovation")
root.geometry("800x500")
root.configure(bg="#e0e0e0")

word_dict = load_words()
dark_mode = tk.BooleanVar()
dark_mode.set(False)

header_frame = tk.Frame(root, bg="#e0e0e0")
header_frame.pack(pady=10)

word_frame = tk.Frame(root, bg="#e0e0e0")
word_frame.pack(pady=10)

translation_frame = tk.Frame(root, bg="#e0e0e0")
translation_frame.pack(pady=10)

header_label = tk.Label(header_frame, text="Advanced ML Translation Innovation", fg="black", bg="#e0e0e0", font=("Arial", 18))
header_label.pack()

label_word = tk.Label(word_frame, text="Enter a word:", fg="black", bg="#e0e0e0", font=("Arial", 12))
entry_word = tk.Entry(word_frame, bg="white", fg="black", font=("Arial", 12))
label_meaning = tk.Label(word_frame, text="Meaning of the word:", fg="black", bg="#e0e0e0", font=("Arial", 12))
entry_meaning = tk.Entry(word_frame, bg="white", fg="black", font=("Arial", 12))
button_add = tk.Button(word_frame, text="Add Word", command=add_word, bg="#333", fg="white", font=("Arial", 12))

label_word_by_word = tk.Label(translation_frame, text="Enter a sentence to translate word by word:", fg="black", bg="#e0e0e0", font=("Arial", 12))
entry_word_by_word = tk.Entry(translation_frame, bg="white", fg="black", font=("Arial", 12))
button_translate_word_by_word = tk.Button(translation_frame, text="Translate Word by Word", command=translate_word_by_word, bg="#333", fg="white", font=("Arial", 12))
label_translated_word_by_word = tk.Label(translation_frame, text="Translated sentence (word by word):", fg="black", bg="#e0e0e0", font=("Arial", 12))
entry_translated_word_by_word = tk.Entry(translation_frame, bg="white", fg="black", font=("Arial", 12))

entry_search = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))

label_translated_words = tk.Label(root, text="Translated words:", fg="black", bg="#e0e0e0", font=("Arial", 14))
listbox_translated = tk.Listbox(root, bg="white", fg="black", font=("Arial", 12))

for meaning, word in word_dict.items():
    listbox_translated.insert(tk.END, f"{meaning}: {word}")

label_word.grid(row=0, column=0, pady=5, padx=5, sticky="w")
entry_word.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
label_meaning.grid(row=1, column=0, pady=5, padx=5, sticky="w")
entry_meaning.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
button_add.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

label_word_by_word.grid(row=0, column=0, pady=5, padx=5, sticky="w")
entry_word_by_word.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
button_translate_word_by_word.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
label_translated_word_by_word.grid(row=2, column=0, pady=5, padx=5, sticky="w")
entry_translated_word_by_word.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

entry_search.pack(pady=5, padx=10, fill=tk.X, expand=True)

label_translated_words.pack(pady=10, padx=10, fill=tk.X)
listbox_translated.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

# Buttons for delete, update, frequency analysis, and export dictionary
button_delete = tk.Button(root, text="Delete Word", command=delete_word, bg="#333", fg="white", font=("Arial", 12))
button_delete.pack(pady=5, padx=10, fill=tk.X)
button_update = tk.Button(root, text="Update Word", command=update_word, bg="#333", fg="white", font=("Arial", 12))
button_update.pack(pady=5, padx=10, fill=tk.X)
button_frequency_analysis = tk.Button(root, text="Word Frequency Analysis", command=word_frequency_analysis, bg="#333", fg="white", font=("Arial", 12))
button_frequency_analysis.pack(pady=5, padx=10, fill=tk.X)
button_export_dict = tk.Button(root, text="Export Dictionary", command=export_dictionary, bg="#333", fg="white", font=("Arial", 12))
button_export_dict.pack(pady=5, padx=10, fill=tk.X)

# Dark mode toggle button
dark_mode_button = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode, onvalue=True, offvalue=False, command=toggle_dark_mode, bg="#e0e0e0", font=("Arial", 12))
dark_mode_button.pack(pady=5, padx=10, anchor=tk.W)

root.mainloop()

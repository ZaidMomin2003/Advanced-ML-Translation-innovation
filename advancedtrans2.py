#This Python code utilizes Tkinter to create a GUI application for translating sentences and managing word dictionaries. It allows users to add words, translate sentences, upload CSV files, and toggle dark mode.

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
                word_dict[word.strip().lower()] = meaning.strip().lower()
            return word_dict
    except FileNotFoundError:
        return {}

def save_words(word_dict):
    with open("words.txt", "w") as file:
        for word, meaning in word_dict.items():
            file.write(f"{word}:{meaning}\n")

def translate_and_add_sentence():
    sentence = entry_sentence.get()
    sentence_meaning = entry_sentence_meaning.get().strip().lower()
    
    translated_words = []
    for word in sentence.split():
        translated_word = word_dict.get(word.lower(), None)
        if translated_word is None:
            messagebox.showwarning("Word Not Found", f"The word '{word}' is not in the dictionary. Please add it.")
            return
        translated_words.append(translated_word)
    translated_sentence = ' '.join(translated_words)
    entry_translated.delete(0, tk.END)
    entry_translated.insert(0, translated_sentence)
    
    word_dict[sentence.lower()] = sentence_meaning
    save_words(word_dict)
    listbox_translated.insert(tk.END, f"{sentence}: {sentence_meaning}")
    messagebox.showinfo("Success", f"Added '{sentence}' to the dictionary!")

def add_word():
    word = entry_word.get().strip().lower()
    meaning = entry_meaning.get().strip().lower()

    if word and meaning:
        word_dict[word] = meaning
        save_words(word_dict)
        listbox_translated.insert(tk.END, f"{word}: {meaning}")
        messagebox.showinfo("Success", f"Added '{word}' to the dictionary!")
    else:
        messagebox.showerror("Error", "Please enter both word and meaning.")

def translate_word_by_word():
    sentence = entry_word_by_word.get()
    translated_sentence = ' '.join([word_dict.get(word.lower(), word) for word in sentence.split()])
    entry_translated_word_by_word.delete(0, tk.END)
    entry_translated_word_by_word.insert(0, translated_sentence)

def add_words_from_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if len(row) == 2:
                    word_dict[row[0].strip().lower()] = row[1].strip().lower()
            save_words(word_dict)
            messagebox.showinfo("Success", "Words added from CSV file.")

root = tk.Tk()
root.title("Advanced ML Translation Innovation")
root.geometry("800x500")
root.configure(bg="#e0e0e0")

word_dict = load_words()

header_frame = tk.Frame(root, bg="#e0e0e0")
header_frame.pack(pady=10)

sentence_frame = tk.Frame(root, bg="#e0e0e0")
sentence_frame.pack(pady=10)

word_frame = tk.Frame(root, bg="#e0e0e0")
word_frame.pack(pady=10)

translation_frame = tk.Frame(root, bg="#e0e0e0")
translation_frame.pack(pady=10)

header_label = tk.Label(header_frame, text="Advanced ML Translation Innovation", fg="black", bg="#e0e0e0", font=("Arial", 18))
header_label.pack()

label_sentence = tk.Label(sentence_frame, text="Enter a sentence to translate:", fg="black", bg="#e0e0e0", font=("Arial", 12))
entry_sentence = tk.Entry(sentence_frame, bg="white", fg="black", font=("Arial", 12))
label_sentence_meaning = tk.Label(sentence_frame, text="Meaning of the sentence:", fg="black", bg="#e0e0e0", font=("Arial", 12))
entry_sentence_meaning = tk.Entry(sentence_frame, bg="white", fg="black", font=("Arial", 12))
button_translate = tk.Button(sentence_frame, text="Translate Sentence and Add to Database", command=translate_and_add_sentence, bg="#333", fg="white", font=("Arial", 12))

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

button_upload_csv = tk.Button(root, text="Upload CSV File", command=add_words_from_csv, bg="#333", fg="white", font=("Arial", 12))
button_upload_csv.pack(pady=5, padx=5, fill=tk.X)

label_translated_sentence = tk.Label(root, text="Translated sentence:", fg="black", bg="#e0e0e0", font=("Arial", 14))
entry_translated = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))

label_translated_words = tk.Label(root, text="Translated words:", fg="black", bg="#e0e0e0", font=("Arial", 14))
listbox_translated = tk.Listbox(root, bg="white", fg="black", font=("Arial", 12))

for word, meaning in word_dict.items():
    listbox_translated.insert(tk.END, f"{word}: {meaning}")

label_sentence.grid(row=0, column=0, pady=5, padx=5, sticky="w")
entry_sentence.grid(row=0, column=1, pady=5, padx=5, sticky="ew")
label_sentence_meaning.grid(row=1, column=0, pady=5, padx=5, sticky="w")
entry_sentence_meaning.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
button_translate.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

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

label_translated_sentence.pack(pady=10, padx=10, fill=tk.X)
entry_translated.pack(pady=5, padx=10, fill=tk.X)

label_translated_words.pack(pady=10, padx=10, fill=tk.X)
listbox_translated.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()

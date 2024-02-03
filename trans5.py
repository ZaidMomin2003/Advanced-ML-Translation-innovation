from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator
from gtts import gTTS
import os
import pygame

root = Tk()
root.title('Language Translator')
root.geometry('590x370')

def translate_text():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        translated_text = output.text
        text_entry2.insert('end', translated_text)

def speak_text():
    translated_text = text_entry2.get("1.0", "end-1c")
    if translated_text == '':
        messagebox.showerror('Language Translator', 'No translated text to speak!')
    else:
        tts = gTTS(translated_text)
        tts.save("translated_text.mp3")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("translated_text.mp3")
        pygame.mixer.music.play()

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

framel = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#F7DC6F')
framel.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#F7DC6F').pack(pady=10)

auto_select = ttk.Combobox(framel, width=27, state='readonly', font=('verdana', 10, 'bold'))
auto_select['values'] = ('Auto Select',)
auto_select.place(x=15, y=60)
auto_select.current(0)

l = StringVar()
choose_language = ttk.Combobox(framel, width=27, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))
choose_language['values'] = (
    'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Aymara', 'Azerbaijani', 'Bambara', 'Basque',
    'Belarusian', 'Bengali', 'Bhojpuri', 'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chinese', 'Corsican', 'Croatian',
    'Czech', 'Danish', 'Dhivehi', 'Dogri', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Ewe', 'Finnish', 'French',
    'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Guarani', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian',
    'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Ilocano', 'Indonesian', 'Irish', 'Italian', 'Japanese',
    'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Konkani', 'Korean', 'Krio', 'Kurdish', 'Kyrgyz', 'Lao',
    'Latin', 'Latvian', 'Lingala', 'Lithuanian', 'Luganda', 'Luxembourgish', 'Macedonian', 'Maithili', 'Malagasy', 'Malay',
    'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Meiteilon', 'Mizo', 'Mongolian', 'Myanmar', 'Nepali', 'Norwegian', 'Nyanja',
    'Odia', 'Oromo', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Samoan',
    'Sanskrit', 'Scots Gaelic', 'Sepedi', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian',
    'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tigrinya',
    'Tsonga', 'Turkish', 'Turkmen', 'Twi', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa',
    'Yiddish', 'Yoruba', 'Zulu'
)
choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(framel, command=translate_text, text="Translate", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
              bg='#248aa2', fg="white", cursor="hand2")
btn1.place(x=80, y=300)

btn2 = Button(framel, command=speak_text, text="Speak", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
              bg='#248aa2', fg="white", cursor="hand2")
btn2.place(x=180, y=300)

btn3 = Button(framel, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
              bg='#248aa2', fg="white", cursor="hand2")
btn3.place(x=280, y=300)

root.mainloop()

from time import sleep
from tkinter import *
from paste_from_clipboard import *
from get_processed_subs import get_processed_subs
from translate_subs import *

from datetime import datetime
text_to_translate = str(get_clipboard_text())[2:len(str(get_clipboard_text()))-1]


root = Tk()
root['bg'] = '#fafafa'
root.title('STS - SubsToStudy')
root.geometry("700x180")
time_with_text = get_processed_subs()


def click_button_to_translate():
    global text_to_translate
    translated_copied_text = translate_text(text_to_translate)
    translated_output.delete('1.0', END)
    translated_output.insert(END, translated_copied_text + "\n")
    translated_output.update()


def click_button_to_start():
    global text_to_translate
    print(text_to_translate)
    if str(get_clipboard_text())[2:len(str(get_clipboard_text())) - 1] == "4":

        click_button_to_translate()
        while True:

            if str(get_clipboard_text())[2:len(str(get_clipboard_text())) - 1] == "345489494":
                break

    if str(get_clipboard_text())[2:len(str(get_clipboard_text()))-1] == "45478745548":

        while True:

            if str(get_clipboard_text())[2:len(str(get_clipboard_text()))-1] == "345489494":
                break
    output.delete('1.0', END)
    output.insert(END, time_with_text[0][1])
    output.update()
    text_to_translate = str(get_clipboard_text())[2:len(str(get_clipboard_text())) - 1]


    if len(time_with_text) - 1 != 0:
        dt = time_with_text[1][0] - time_with_text[0][0]
    else:
        dt = 0
    time_with_text.pop(0)

    root.after(int(dt*1000), click_button_to_start)



output = Text(root, width=86, height=3)
translated_output = Text(root, width=86, height=3)
a = "Pls, place it in the most suitable place and press start"
output.insert(END, a)
output.grid(row=5, column=1, columnspan=2, padx=5, pady=(0,10))
translated_output.insert(END,"translated text will be appear here")
translated_output.grid(row=7, column=1, columnspan=2, padx=5, pady=(0,10))
btn_to_start = Button(root, text="Start", command=click_button_to_start)
#btn_to_translate = Button(root, text="Translate", command=click_button_to_translate)
btn_to_start.grid(row=6, column=1, columnspan=2, padx=5, pady=(0,10))
#btn_to_translate.grid(row=6, column=2, columnspan=2, padx=5, pady=(0,10))

root.mainloop()



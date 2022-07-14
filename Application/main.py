from tkinter import *
from set_and_get_data_from_clipboard import *
from get_processed_sub import get_processed_sub
from translate_sub import *
from time import sleep
import os

#That function saves pathname to sub
def save_path_in_file(text):
    path_to_script = os.path.dirname(os.path.abspath(__file__))
    my_filename = os.path.join(path_to_script, "file_where_i_save_path.txt")
    if os.path.exists(my_filename):
        file1 = open(my_filename, "w")
        file1.write(text)
        file1.close()
    else:
        file1 = open(my_filename, "w")
        file1.write(text)
        file1.close()

#Creates new window but now isn't used
def openNewWindow():
    #gets a path to file, close the new window, starts sub play
    def get_input():
        #click_button_to_continue()
        time_with_text2 = get_processed_sub()
        text = my_text_box.get("1.0", "end-1c")
        #save_it_in_file(text)
        newWindow.destroy()

#Gui newWindow
    newWindow = Toplevel(root)
    newWindow.title("Settings")
    newWindow.geometry("700x100")
    btn_to_continue = Button(newWindow, text="Continue", command=get_input)
    my_text_box = Text(newWindow, width=86, height=2)
    my_text_box.pack()
    Label(newWindow,text="But before place Absolute Path to your subtitles here").pack()
    btn_to_continue.pack()


def translate():
    global text_to_translate
    translated_copied_text = translate_text(text_to_translate)
    translated_output.delete('1.0', END)
    translated_output.insert(END, translated_copied_text + "\n")
    translated_output.update()

def click_button_to_start():

    time_with_text2 = get_processed_sub()
    text = output.get("1.0", "end-1c")
    if text != "Pls, write absolute path to sub or just press start to continue with last one":
        save_path_in_file(text)
    else:
        save_path_in_file(r"C:\Users\Никита\PycharmProjects\pythonProject\dj.sub")
    continuation()
#works after button is pressed
def continuation():
    global text_to_translate
    global stop_checker
    #partition that is used to pinpoint the case when the button is pressed in the browser

    if str(get_clipboard_text()) == "4323232":
        translate()
        set_clipboard_text("45478745548")
        root.after(300, continuation)
        return None
    if str(get_clipboard_text()) == "345489494":
        stop_checker = 0
    if str(get_clipboard_text()) == "45478745548" or stop_checker == 1:
        root.after(300, continuation)
        stop_checker = 1
        text_to_translate = str(get_clipboard_text())
        return None

    output.delete('1.0', END)
    output.insert(END, time_with_text[0][1])
    output.update()

    text_to_translate = str(get_clipboard_text())
    #Sub part
    if len(time_with_text) - 1 != 0:
        #time between pair of sub
        dt = time_with_text[1][0] - time_with_text[0][0]
    else:
        dt = 0
    time_with_text.pop(0)
    #Start this function again after some time
    root.after(int(dt*1000), continuation)


#GUI partition

#Let's create a main window
root = Tk()
#gives the window some properties(color: white, name: 'STS - SubToStudy', size of window:"700x180")
root['bg'] = '#fafafa'
root.title('STS - SubToStudy')
root.geometry("700x160")
#The first window, where subtitles appear
output = Text(root, width=86, height=3)
output.insert(END, "Pls, write absolute path to sub or just press start to continue with last one")
output.grid(row=5, column=1, columnspan=2, padx=5, pady=(0,10))
#The Second window, where translated sub appears
translated_output = Text(root, width=86, height=3)
translated_output.insert(END,"To translate unknown words from sub you need to copy them and press translate in your browser. After that this app and video will stop until you press button start in the Browser")
translated_output.grid(row=6, column=1, columnspan=2, padx=5, pady=(0,10))
#Button
btn_to_start = Button(root, text="Start", command=click_button_to_start)
btn_to_start.grid(row=7, column=1, columnspan=2, padx=5, pady=(0,10))


#Logic partition
#need to understand if programm stop or not
stop_checker = 0
text_to_translate = str(get_clipboard_text())
#data that is like [(time, subtitle),....]
time_with_text = get_processed_sub()

root.mainloop()

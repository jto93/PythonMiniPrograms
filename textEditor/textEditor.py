#Simple Text Editor built in tkinter for Windows using Codemy.com's lessons
# Pick up here: https://www.youtube.com/watch?v=CtENi3AhuY4&ab_channel=Codemy.com

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('My Text Editor')
root.iconbitmap('C:/Users/j_t_o/Desktop/Python Projects/Text_Projects/textEditor/img/Cool-icon.ico')
root.geometry('1200x680')

#Setting variable for open filename
global open_name
open_name = False

#Selected Variable
global selected
selected = False

#Menu Functions------------------------------------------------

#Create new file
def new_file(): 
    global open_name
    open_name = False
    my_text.delete("1.0", END)
    root.title('New File')
    status_bar.config(text='New File    ')
    #Add a query to make sure user does not want to save

#Creat open file function
def open_file(): 
    my_text.delete("1.0", END)

    #Grab file name and asign to a global variable. 
    text_file = filedialog.askopenfilename(initialdir="C:/Users/j_t_o/Desktop", filetypes=(("Text Files","*.txt"), ("HTML Files","*.html"),("Python Files","*.py"), ("All Files", '*.*')))
    
    #Check to see if file name exists
    if text_file:
        global open_name
        open_name = text_file

    #Update status bar
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("C:/Users/j_t_o/Desktop/","")
    root.title(f'{name}     ')

    #Open file
    text_file = open(text_file, 'r')
    content = text_file.read()
    #add file to the textbox
    my_text.insert(END, content)
    #Close the text file
    text_file.close()

#Save File
def save_file(): 
    global open_name
    if open_name: 
        #Save File
        text_file = open(open_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text=f'Saved {open_name}     ')
    
    else: 
        save_as_file()

#Save As File
def save_as_file(): 
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/j_t_o/Desktop", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"),("All Files", "*.*")))
    if text_file: 
        #Update status bars
        name = text_file
        status_bar.config(text=f'Saved {name}     ')
        name = name.replace("C:/Users/j_t_o/Desktop", "")
        root.title(f'{name}     ')

        #Save File
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

#Cut 
def cut_text(e):
    global selected
    #Check to see if keyboard shortcut used
    if e: 
        selected = root.clipboard_get()

    if my_text.selection_get():
        #Get selected text
        selected = my_text.selection_get()

        #Clear and add selected text to clipboard
        root.clipboard_clear()
        root.clipboard_append(selected)
        #Delete Selected text
        my_text.delete("sel.first","sel.last")

#Copy
def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get(): 
        selected = my_text.selection_get()
        #Clear clipboard and append selected
        root.clipboard_clear()
        root.clipboard_append(selected)
#Paste
def paste_text(e):
    global selected
    #Check to see if shortcut used
    if e: 
        selected = root.clipboard_get()
    else: 
        if selected:
            position = my_text.index(INSERT) #Grabs wherever cursor is located
            my_text.insert(position, selected)

#Toolbar functions
#Bold
def bold_text(): 
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")
    
    current_tags = my_text.tag_names("sel.first")
    #Configure tag
    my_text.tag_configure("bold", font=bold_font)

    if "bold" in current_tags: 
        my_text.tag_remove("bold", "sel.first","sel.last")

    else: 
        my_text.tag_add("bold", "sel.first", "sel.last")


def italics_text():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")
    
    current_tags = my_text.tag_names("sel.first")
    #Configure tag
    my_text.tag_configure("italic", font=italics_font)

    if "italic" in current_tags: 
        my_text.tag_remove("italic", "sel.first","sel.last")

    else: 
        my_text.tag_add("italic", "sel.first", "sel.last")


### Adding a Toolbar-------------------------------------------------------------
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)


### Adding a Main Frame, Scroll Bars and Menus

#Create a Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#Create the Scroll Bars
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#horizontal scroll
horizontal_scroll = Scrollbar(my_frame, orient='horizontal')
horizontal_scroll.pack(side=BOTTOM, fill=X)


#Create Text Box
my_text = Text(my_frame, width=150, height=34, font=('Helvetica',12),selectbackground='yellow', selectforeground='black', undo=True, xscrollcommand=horizontal_scroll.set, yscrollcommand=text_scroll.set, wrap="none")
my_text.pack()

#Configure the Scrollbar
text_scroll.config(command=my_text.yview)
horizontal_scroll.config(command=my_text.xview)

#Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New File", command=new_file, accelerator="(CTRL+N)")
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

#Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(CTRL+X)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(CTRL+C)")
edit_menu.add_command(label="Paste ", command=lambda: paste_text(False), accelerator="(CTRL+P)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(CTRL+Z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(CTRL+Y)")

#Add a Status Bar to the Bottom of the App
status_bar = Label(root, text="Ready    ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

#Create Buttons
bold_button = Button(toolbar_frame, text="Bold", command=bold_text)
bold_button.grid(row=0, column=0, padx=1, sticky=W)

italics_button = Button(toolbar_frame, text="Italics", command=italics_text)
italics_button.grid(row=0, column=1, padx=1, sticky=W)

root.mainloop()


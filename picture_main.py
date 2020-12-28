from Huffman import Huffman
from lz4 import lz4
from Zip import files2zip, zip2files
from tkinter import *
from tkinter.tix import Tk,Control,ComboBox
from tkinter.messagebox import showinfo,showwarning,showerror
import time



# Booleans
NO=FALSE=OFF=0
YES=TRUE=ON=1

# -anchor and -sticky
N='n'
S='s'
W='w'
E='e'
NW='nw'
SW='sw'
NE='ne'
SE='se'
NS='ns'
EW='ew'
NSEW='nsew'
CENTER='center'

# -fill
NONE='none'
X='x'
Y='y'
BOTH='both'

# -side
LEFT='left'
TOP='top'
RIGHT='right'
BOTTOM='bottom'

# -relief
RAISED='raised'
SUNKEN='sunken'
FLAT='flat'
RIDGE='ridge'
GROOVE='groove'
SOLID = 'solid'

# -orient
HORIZONTAL='horizontal'
VERTICAL='vertical'

# -tabs
NUMERIC='numeric'

# -wrap
CHAR='char'
WORD='word'

# -align
BASELINE='baseline'

# -bordermode
INSIDE='inside'
OUTSIDE='outside'

# Special tags, marks and insert positions
SEL='sel'
SEL_FIRST='sel.first'
SEL_LAST='sel.last'
END='end'
INSERT='insert'
CURRENT='current'
ANCHOR='anchor'
ALL='all' # e.g. Canvas.delete(ALL)

# Text widget and button states
NORMAL='normal'
DISABLED='disabled'
ACTIVE='active'
# Canvas state
HIDDEN='hidden'

# Menu item types
CASCADE='cascade'
CHECKBUTTON='checkbutton'
COMMAND='command'
RADIOBUTTON='radiobutton'
SEPARATOR='separator'

# Selection modes for list boxes
SINGLE='single'
BROWSE='browse'
MULTIPLE='multiple'
EXTENDED='extended'

# Activestyle for list boxes
# NONE='none' is also valid
DOTBOX='dotbox'
UNDERLINE='underline'

# Various canvas styles
PIESLICE='pieslice'
CHORD='chord'
ARC='arc'
FIRST='first'
LAST='last'
BUTT='butt'
PROJECTING='projecting'
ROUND='round'
BEVEL='bevel'
MITER='miter'

# Arguments to xview/yview
MOVETO='moveto'
SCROLL='scroll'
UNITS='units'
PAGES='pages'



Algorithm_choice=0
Function_choice=0

def algorithm(choice,root_main):
    global Algorithm_choice
    Algorithm_choice=choice
    function_page(root_main)

def function(choice,root_function):
    global Function_choice
    Function_choice=choice
    location_page(root_function)

def get_location(root,location_entry):

    file_location=location_entry.get()
    hint="null"
    time_start = time.time()

    global Algorithm_choice
    global Function_choice

    if Algorithm_choice == 1:
        if Function_choice ==  1:
            hint = Huffman.file_encode(file_location)
        if Function_choice == 2:
            hint = Huffman.file_decode(file_location)
    elif Algorithm_choice == 2:
        if Function_choice ==  1:
            hint = files2zip.files2zip(file_location)
        if Function_choice == 2:
            hint = zip2files.zip2files(file_location)
    elif Algorithm_choice == 3:
        if Function_choice == 1:
            hint = lz4.main("-c",file_location)
        if Function_choice == 2:
            hint = lz4.main("-x", file_location)
    time_end = time.time()
    run_time=time_end-time_start

    root.destroy()
    final_page(hint,run_time)

def main_page(root_function):
    global Algorithm_choice
    Algorithm_choice=0

    root_function.destroy();

    root = Tk()
    root.title("A Compressed Software By Wang,Xu,Wu,Huang")
    root.geometry("999x666")
    root.resizable(width=True, height=True)
    root.eval('package require Tix')
    root['bg'] = '#FFFAF0'
    text1 = Label(root, text="-⭐-Choose the compressed algorithm you want-⭐-", bg="#FFFAF0",
                  fg="BLACK", font=("黑体", 25), width=50, height=2, anchor="center")
    text1.place(x=70, y=40)
    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#D8BFD8",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=70, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#DDA0DD",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=282, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#BA55D3",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=494, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#8B008B",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=706, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#D8BFD8",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=70, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#DDA0DD",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=282, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#BA55D3",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=494, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#8B008B",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=706, y=480)

    button1_1 = Button(root, text="Huffman", font=("宋体", 25), command=lambda: algorithm(1,root), width=15, height=2,
                       bg="#FFE4C4")
    button1_1.place(x=70, y=300)

    button1_2 = Button(root, text="Zip", font=("宋体", 25), command=lambda: algorithm(2,root), width=15, height=2,
                       bg="#F4A460")
    button1_2.place(x=363, y=300)

    button1_3 = Button(root, text="Lz4", font=("宋体", 25), command=lambda: algorithm(3,root), width=15, height=2,
                       bg="#CD5C5C")
    button1_3.place(x=656, y=300)

    button1_4 = Button(root, text="Exit", font=("宋体", 15), command=lambda: sys.exit(), width=5, height=1, bg="#E9967A")
    button1_4.place(x=860, y=600)

    root.mainloop()

def function_page(root_main_or_ocation):
    global Function_choice
    Function_choice=0

    root_main_or_ocation.destroy()

    root = Tk()
    root.title("A Compressed Software By Wang,Xu,Wu,Huang")
    root.geometry("999x666")
    root.resizable(width=True, height=True)
    root.eval('package require Tix')
    root['bg'] = '#FFFAF0'
    text1 = Label(root, text="-⭐-Compress Or Uncompress-⭐-", bg="#FFFAF0",
                  fg="BLACK", font=("黑体", 25), width=50, height=2, anchor="center")
    text1.place(x=70, y=40)
    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#D8BFD8",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=70, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#DDA0DD",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=282, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#BA55D3",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=494, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#8B008B",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=706, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#D8BFD8",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=70, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#DDA0DD",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=282, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#BA55D3",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=494, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#8B008B",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=706, y=480)

    button1_1 = Button(root, text="Compress", font=("宋体", 30), command=lambda: function(1,root), width=15, height=2,
                       bg="#87CEEB")
    button1_1.place(x=150, y=300)

    button1_2 = Button(root, text="Uncompress", font=("宋体", 30), command=lambda: function(2,root), width=15, height=2,
                       bg="#4682B4")
    button1_2.place(x=550, y=300)

    button1_3 = Button(root, text="Return", font=("宋体", 15), command=lambda:main_page(root), width=5, height=1, bg="#48D1CC")
    button1_3.place(x=780, y=600)

    button1_4 = Button(root, text="Exit", font=("宋体", 15), command=lambda: sys.exit(), width=5, height=1, bg="#20B2AA")
    button1_4.place(x=860, y=600)

    root.mainloop()

def location_page(root_function_or_final):
    global File_location
    File_location="null"

    root_function_or_final.destroy()

    root = Tk()
    root.title("A Compressed Software By Wang,Xu,Wu,Huang")
    root.geometry("999x666")
    root.resizable(width=True, height=True)
    root.eval('package require Tix')
    root['bg'] = '#FFFAF0'
    text1 = Label(root, text="-⭐-Input The Location Of File You Want To Deal With-⭐-", bg="#FFFAF0",
                  fg="BLACK", font=("黑体", 20), width=70, height=2, anchor="center")
    text1.place(x=10, y=40)
    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#D8BFD8",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=70, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#DDA0DD",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=282, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#BA55D3",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=494, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#8B008B",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=706, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#D8BFD8",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=70, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#DDA0DD",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=282, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#BA55D3",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=494, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#8B008B",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=706, y=480)

    location_input=StringVar()
    location_input=Entry(root,bg="#ADD8E6",width=100)
    location_input.place(x=100,y=330)

    button1_3 = Button(root, text="Start", font=("宋体", 10), command=lambda: get_location(root,location_input), width=5, height=1,
                       bg="#AFEEEE")
    button1_3.place(x=866, y=330)

    button1_3 = Button(root, text="Return", font=("宋体", 15), command=lambda: function_page(root), width=5, height=1,
                       bg="#48D1CC")
    button1_3.place(x=780, y=600)

    button1_4 = Button(root, text="Exit", font=("宋体", 15), command=lambda: sys.exit(), width=5, height=1, bg="#20B2AA")
    button1_4.place(x=860, y=600)

    root.mainloop()


def final_page(hint,time):

    root = Tk()
    root.title("A Compressed Software By Wang,Xu,Wu,Huang")
    root.geometry("999x666")
    root.resizable(width=True, height=True)
    root.eval('package require Tix')
    root['bg'] = '#FFFAF0'

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#D8BFD8",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=70, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#DDA0DD",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=282, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#BA55D3",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=494, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#8B008B",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=706, y=200)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#D8BFD8",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=70, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#DDA0DD",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=282, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#BA55D3",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=494, y=480)

    imige1 = Label(root, text="-⭐--⭐--⭐--⭐-", bg="#8B008B",
                   fg="#FFFAF0", font=("宋体", 8), width=34, height=1, anchor="center")
    imige1.place(x=706, y=480)

    text1 = Label(root, text=hint, bg="#FFFAF0",
                  fg="BLACK", font=("黑体", 10), width=100, height=2, anchor="center")
    text1.place(x=100, y=300)

    text2 = Label(root, text="程序运行时间：", bg="#FFFAF0",
                  fg="BLACK", font=("黑体", 10), width=100, height=2, anchor="center")
    text2.place(x=100, y=380)

    text3 = Label(root, text=time, bg="#FFFAF0",
                  fg="BLACK", font=("黑体", 10), width=100, height=2, anchor="center")
    text3.place(x=300, y=380)

    text4 = Label(root, text="s", bg="#FFFAF0",
                  fg="BLACK", font=("黑体", 10), width=3, height=2, anchor="center")
    text4.place(x=730, y=380)

    button1_3 = Button(root, text="Return", font=("宋体", 15), command=lambda: location_page(root), width=5, height=1,
                       bg="#48D1CC")
    button1_3.place(x=780, y=600)

    button1_4 = Button(root, text="Exit", font=("宋体", 15), command=lambda: sys.exit(), width=5, height=1, bg="#20B2AA")
    button1_4.place(x=860, y=600)

    root.mainloop()

if __name__ == "__main__":
    fake_root=Tk()
    main_page(fake_root);



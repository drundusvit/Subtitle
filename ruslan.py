# -*- coding: utf-8 -*-
import sys
from Tkinter import *
import os
 
 
try:
    inputfile = sys.argv[1]
    outputfile = inputfile + '_out'
except:
    print "You must type - python damir.py 'name of file'"
    quit()
 
in_open = open(inputfile, 'r')
in_read = in_open.read()
in_text = in_read.lower()
in_text = in_text.replace('#', '')
words = in_text.split()
tmp_words = words + ['']
in_open.close()
 
try:
    out_open = open(outputfile, 'r')
    out_read = out_open.read()
    out_open.close()
except:
    out_open = open(outputfile, 'w')
    out_open.close()
    out_open = open(outputfile, 'r')
    out_read = out_open.read()
    out_open.close()
 
i = 0
listout = ''
 
def know():
    global i
    global tmp_words
    tmp_words.remove(words[i])
    i+=1
    english.delete(1.0,END)
    russian.delete(1.0,END)
    english.insert(INSERT, words[i])
 
def d_know():
    global i
    global listout
    global english
    global tmp_words
    tmp_words.remove(words[i])
    rus = russian.get(1.0, END)[:-1]
    rus = rus.replace('#', '')
    listout = listout + '\"' + english.get(1.0, END)[:-1] + '\"' + '#' + '\"' + rus + '\"' + '\n'
    i+=1
    english.delete(1.0,END)
    russian.delete(1.0,END)
    english.insert(INSERT, words[i])
 
def translate():
    russian.delete(1.0,END)
    p = os.popen(('sdcv -n -u mueller ' + english.get(1.0, END)[:-1]),"r")
    while 1:
        line = p.readline()
        if not line: break
        russian.insert(INSERT, line)
 
def exit():
    global listout
    global out_read
    global in_open
    global words
    out_open = open(outputfile, 'w')
    print type(listout), 'before encode'
    listout = u''.join(listout).encode('utf-8').strip()    
    listout = out_read + listout 
    print type(listout), 'listout after'
    out_open.write(listout)
    out_open.close()
    print type(listout)
    in_open = open(inputfile, 'w')
    print type(in_open)
    for x in tmp_words:
        in_open.write(x + '\n')
    in_open.close()
    quit()
 
def select_all(e):
    e.widget.tag_add(SEL, '1.0', END)
 
root = Tk()
frame = Frame(root)
frame.pack()
 
root.bind('<Control-a>', select_all)
 
root.title('Damir')
scrollbar1 = Scrollbar(frame)
scrollbar1.grid(row = 0, column = 1, sticky = N + S + W)
scrollbar2 = Scrollbar(frame)
scrollbar2.grid(row = 1, column = 1, sticky = N + S + W)
english = Text(frame,bd=2, insertwidth = 1, font = 10, height = 5, width = 40, yscrollcommand = scrollbar1.set)
russian = Text(frame,bd=2, insertwidth = 1, font = 10, height = 10, width = 40, yscrollcommand = scrollbar2.set)
english.grid(row = 0, sticky = W)
russian.grid(row = 1, sticky = W)
scrollbar1.config(command = english.yview)
scrollbar2.config(command = russian.yview)
 
english.insert(INSERT, words[i])
 
b1 = Button(frame, text="add", height = 5, width=9, command = d_know)
b1.grid(row = 0, column = 1, padx = 20, sticky = SW)
b2 = Button(frame, text="remove", height = 5, width=9, command = know)
b2.grid(row = 0, column = 1, padx = 120, sticky = SW)
b3 = Button(frame, text="Save and exit", height = 3, width=22, command = exit)
b3.grid(row = 1, column = 1, padx = 20, sticky = SW)
b4 = Button(frame, text="Translate", height = 3, width=22, command = translate)
b4.grid(row = 1, column = 1, padx = 20, sticky = NW)
 
root.mainloop()

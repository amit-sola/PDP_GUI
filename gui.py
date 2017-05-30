from tkinter import *
import tkinter.messagebox

def load_file(event):
    print("Loading the file in Memory")
    tkinter.messagebox.showinfo('Load File','Loading the file...')

def goto_memory(event):
    print("Going to memory location")
    tkinter.messagebox.showinfo('Go to memory','Going to memory location...')


def set_memory(event):
    print("Setting the memory location ... to ...")

    tkinter.messagebox.showinfo('Set Memory','Setting memory location done')


def set_bp_memory(event):
    print("Setting the breakpoint at memory location ... ")

    tkinter.messagebox.showinfo('Set breakpoint', 'Setting the breakpoint at location done')


def remove_bp_memory(event):
    print("Removing the breakpoint at memory location ... ")

    tkinter.messagebox.showinfo('Remove breakpoint', 'Removing the breakpoint at location done')



def run(event):
    print("Running the simulator")
    tkinter.messagebox.showinfo('Run','Running the simulator.')


def single_stepping(event):
    print("Doing single stepping")
    '''call the appropriate function'''


root = Tk()

'''frame = Frame(root,width=500,height=500)
'''

project_label = Label(root,text="PDP-11 Simulator ")
project_label.grid(columnspan=2)

blank1_label = Label(root,text="                         ")
blank1_label.grid(columnspan=2)



'''###########################################'''
''' Memory space  '''

memory_map_label = Label(root,text="Memory space")
memory_map_label.grid(row=2,column=0,sticky=E)

memory_map_entry = Entry(root)
#memory_map_entry.grid(row=2,column=1)
memory_map_entry.grid(row=2,column=1)

blank2_label = Label(root,text="                         ")
blank2_label.grid(columnspan=2)


''' Memory space  '''
'''###########################################'''



'''###########################################'''
''' Register space  '''

register_map_label = Label(root,text="Register space")
register_map_label.grid(row=2,column=4,sticky=E)



register0_map_label = Label(root,text="R0")
register0_map_label.grid(row=4,column=3,sticky=E)

register0_map_entry = Entry(root)
register0_map_entry.grid(row=4,column=4)


register1_map_label = Label(root,text="R1")
register1_map_label.grid(row=5,column=3,sticky=E)

register1_map_entry = Entry(root)
register1_map_entry.grid(row=5,column=4)



register2_map_label = Label(root,text="R2")
register2_map_label.grid(row=6,column=3,sticky=E)

register2_map_entry = Entry(root)
register2_map_entry.grid(row=6,column=4)


register3_map_label = Label(root,text="R3")
register3_map_label.grid(row=7,column=3,sticky=E)

register3_map_entry = Entry(root)
register3_map_entry.grid(row=7,column=4)


register4_map_label = Label(root,text="R4")
register4_map_label.grid(row=8,column=3,sticky=E)

register4_map_entry = Entry(root)
register4_map_entry.grid(row=8,column=4)


register5_map_label = Label(root,text="R5")
register5_map_label.grid(row=9,column=3,sticky=E)

register5_map_entry = Entry(root)
register5_map_entry.grid(row=9,column=4)


register6_map_label = Label(root,text="SP / R6")
register6_map_label.grid(row=10,column=3,sticky=E)

register6_map_entry = Entry(root)
register6_map_entry.grid(row=10,column=4)



register7_map_label = Label(root,text="PC / R7")
register7_map_label.grid(row=11,column=3,sticky=E)

register7_map_entry = Entry(root)
register7_map_entry.grid(row=11,column=4)



blank2_label = Label(root,text="                         ")
blank2_label.grid(columnspan=2)


''' Register space  '''
'''###########################################'''








'''###########################################'''
''' Object file load / run  '''

obj_file_label = Label(root,text="Object file name")
obj_file_label.grid(row=14,column=0,sticky=E)


obj_file_entry = Entry(root)
obj_file_entry.grid(row=14,column=1)


load_button = Button(root,text="LOAD")
load_button.bind("<Button-1>",load_file)
load_button.grid(row=14,column=2)

blank3_label = Label(root,text="  ")
blank3_label.grid(row=14,column=3)

run_button = Button(root,text="RUN")
run_button.bind("<Button-1>",run)
run_button.grid(row=14,column=4)


blank3_label = Label(root,text="  ")
blank3_label.grid(row=14,column=5)


run_button = Button(root,text="STEP")
run_button.bind("<Button-1>",single_stepping)
run_button.grid(row=14,column=6)


blank4_label = Label(root,text="                         ")
blank4_label.grid(columnspan=2)


''' Object file load / run  '''
'''###########################################'''



'''###########################################'''
''' Go to memory location  '''

goto_memory_label = Label(root,text="Memory Address")
goto_memory_label.grid(row=16,column=0,sticky=E)

goto_memory_entry = Entry(root)
goto_memory_entry.grid(row=16,column=1)

goto_memory_button = Button(root,text="GO ")
goto_memory_button.bind("<Button-1>",goto_memory)
goto_memory_button.grid(row=16,column=2)



set_bp_memory_button = Button(root,text="Set BP")
set_bp_memory_button.bind("<Button-1>",set_bp_memory)
set_bp_memory_button.grid(row=16,column=4)


set_bp_memory_button = Button(root,text="Remove BP")
set_bp_memory_button.bind("<Button-1>",remove_bp_memory)
set_bp_memory_button.grid(row=16,column=6)



set_memory_label = Label(root,text="Set value")
set_memory_label.grid(row=17,column=0,sticky=E)

set_memory_entry = Entry(root)
set_memory_entry.grid(row=17,column=1)

set_memory_button = Button(root,text="SET ")
set_memory_button.bind("<Button-1>",set_memory)
set_memory_button.grid(row=17,column=2)



''' Go to memory location  '''
'''###########################################'''



root.mainloop()

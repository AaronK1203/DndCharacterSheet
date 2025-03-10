import Sheet
import Minstrel
import BuildACharacter as bac
import tkinter as tk

#Just calls Sheet.main (IDK why it makes me do this)
def call_first():
    Sheet.main(sheets[0])

def call_second():
    Sheet.main(sheets[1])

def call_new():
    
    def confirm():
        bac.build(des_slot.get())
    
    select_slot = tk.Toplevel(root)
    tk.Label(select_slot,text = 'Select a Slot to Overwrite').pack()

    des_slot = tk.IntVar()

    r0 = tk.Radiobutton(select_slot,text = sheets[0],variable = des_slot,value = 0)
    r1 = tk.Radiobutton(select_slot,text = sheets[1],variable = des_slot,value = 1)
    r2 = tk.Radiobutton(select_slot,text = sheets[2],variable = des_slot,value = 2)
    r3 = tk.Radiobutton(select_slot,text = sheets[3],variable = des_slot,value = 3)
    r0.pack(); r1.pack(); r2.pack(); r3.pack()
    
    des_slot.set(0)

    confirm_button = tk.Button(select_slot,text = 'Confirm',width = 10,height = 2,
                               command = confirm)
    confirm_button.pack();

    cancel_button = tk.Button(select_slot,text = 'Cancel',width = 10,height = 2,
                              command = select_slot.destroy)
    cancel_button.pack()
        
    
    
#Stores the character data sheets
sheets = ['Jose-Santiano.txt','Vedmid.txt','Vigamathur.txt','Engagah.txt']

root = tk.Tk()
root.title('Select Your Character')
root.geometry('1000x500')

tk.Label(root,text = 'Select Your Character').place(relx = 0.5,rely = 0.2,
                                                    anchor = tk.CENTER)

quit_button = tk.Button(root,text = 'Quit',width = 10,height = 2,
                        command = root.destroy)
quit_button.place(relx = 0.5,rely = 0.8,anchor = tk.CENTER)

make_button = tk.Button(root,text = 'New Character',width = 14,height = 2,
                        command = call_new)
make_button.place(relx = 0.8,rely = 0.2,anchor = tk.CENTER)


#Note: Utilizes a while loop so
#locks out the rest of the program while it runs
minst_button = tk.Button(root,text = 'Minstrel',width = 14,height = 2,
                         command = Minstrel.main)
minst_button.place(relx = 0.2,rely = 0.2,anchor = tk.CENTER)

character0 = tk.Button(root,text = sheets[0],width = 20,height = 10,
                       command = call_first)
character0.place(relx = 0.2,rely = 0.5,anchor = tk.CENTER)

character1 = tk.Button(root,text = sheets[1],width = 20,height = 10,
                       command = call_second)
character1.place(relx = 0.4,rely = 0.5,anchor = tk.CENTER)



root.mainloop()

import tkinter
from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator

root = Tk()
root.title("Google Translator 2.0")
root.geometry("1080x400")
root.resizable(False,
               False
               )
root.configure(background="white")

def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text = c1)
    label2.configure(text = c2)
    root.after(100,
               label_change
               )

def translte_now():
    #print("here")
    text_=text1.get(1.0,
                    END
                    )
    print('{}'.format(text_))
    if(combo1.get()=='Urdu' ):
        print('combo1 language is urdu')
    elif(combo1.get()=='English'):
        print('combo1 language is English')

    if(combo2.get()=='urdu'):
        print('combo2 language is urdu')
    t1=Translator()
    trans_text=t1.translate(text_,
                            src = combo1.get(),
                            dest = combo2.get()
                            )
    trans_text_31may=trans_text.text
    print('{}'.format(text_))
    if(combo1.get()=='urdu'):
        print('combo1 language is urdu')

    if(combo2.get()=='urdu'):
        print('combo2 language is urdu')
        #trans_text_31may=trans_text_31may.decode('utf-8')
    print(trans_text_31may)

    text2.delete(1.0,
                 END
                 )
    text2.insert(END,
                 trans_text_31may
                 )
    
    
# icon
image_icon=PhotoImage(file="images.png")
root.iconphoto(False,
               image_icon
               )

#arrow

arrow_image = PhotoImage(file="arrow.png")
image_label=Label(root,
                  image=arrow_image,
                  width=150
                  )
image_label.place(x=460,
                  y=50
                  )

language = googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

#first combobox
combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state = "r")
combo1.place(x=110,
             y=20
             )
combo1.set("ENGLISH")

label1 = Label(root,
               text="ENGLISH",
               font="segoe 30 bold",
               bg="white",
               width=15,
               bd=5,
               relief = GROOVE
               )
label1.place(x=10,
             y=50
             )
#second combobox
combo2=ttk.Combobox(root,
                    values=languageV,
                    font="Roboto 14",
                    state = "r"
                    )
combo2.place(x=730,
             y=20
             )
combo2.set("Select Language")
#combo1.set("Urdu")

label2 = Label(root,
               text="ENGLISH",
               font="segoe 30 bold",
               bg="white",
               width=15,
               bd=5,
               relief = GROOVE
               )
label2.place(x=620,
             y=50
             )

# first frame
f = Frame(root,
          bg="Black",
          bd=5
          )
f.place(x=10,
        y=118,
        width=430,
        height=210
        )

text1 = Text(f,
             font="Robote 20",
             bg="white",
             relief=GROOVE,
             wrap = WORD
             )
text1.place(x=0,
            y=0,
            width=420,
            height=200
            )

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",
                fill='y'
                )

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# second frame
f2 = Frame(root,
           bg="Black",
           bd=5
           )
f2.place(x=620,
         y=118,
         width=430,
         height=210
         )

text2 = Text(f2,
             font="Robote 20",
             bg="white",
             relief=GROOVE,
             wrap = WORD
             )
text2.place(x=0,
            y=0,
            width=420,
            height=200
            )

scrollbar2=Scrollbar(f2)
scrollbar2.pack(side="right",
                fill='y'
                )

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate button
translate = Button(root,
                   text="Translate",
                   font=("Roboto",15),
                   activebackground="white",
                   cursor="hand2",
                   bd=1,
                   width=8,
                   height=2,
                   bg="black",
                   fg="white",
                   command=translte_now
                   )
translate.place(x=466,
                y=250
                )


label_change()

root.mainloop()

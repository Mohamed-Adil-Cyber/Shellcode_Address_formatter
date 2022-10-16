from tkinter import *
 
def Sanitize():
    shellcodeAddress = str(e1.get())
    shellcodeAddress = shellcodeAddress.replace(" ", "")
    shellcodeAddress = shellcodeAddress.replace("0x", "")
    shellcodeAddress = shellcodeAddress.replace("h", "")
    if (len(shellcodeAddress) % 2) != 0:
       shellcodeAddress = "0" + shellcodeAddress
    vector = ""
    final_vector = ""
    for i in shellcodeAddress:
        vector+=i
         
        if len(vector)==2:
            final_vector = vector + final_vector
            vector = ""
    shellcodeAddress = final_vector
    shellcodeAddress = " ".join(shellcodeAddress[i:i+2] for i in range(0, len(shellcodeAddress), 2))
    shellcodeAddress = shellcodeAddress.replace(" ","\\x")
    shellcodeAddress = "\\x"+shellcodeAddress
    myText.set(shellcodeAddress)
    print(shellcodeAddress)
 
master = Tk()
myText=StringVar()
Label(master, text="address").grid(row=0, sticky=W)
Label(master, text="shellcode").grid(row=4, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=4,column=1, sticky=W)
 
e1 = Entry(master)

e1.grid(row=0, column=1)

 
b = Button(master, text="Sanitize", command=Sanitize)
b.grid(row=0, column=3,columnspan=1, rowspan=1,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()

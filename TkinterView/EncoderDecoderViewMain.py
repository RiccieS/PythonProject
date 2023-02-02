from tkinter import *
from EncodeLogics import base64logic as base64, CaesarsCipherLogic as caesar, RSALogic as rsa
import TkinterView.EncoderDecoderRSAView as RSAView
import TkinterView.EncoderDecoderView as View

class EncoderDecoderView:
    def __init__(self):
        '''Create a Tkinter Tk object and set the size and title of the window'''
        self.root = Tk()
        self.root.geometry("300x200")
        self.root.resizable(0,0)
        self.root.title("Message Encoder and Decoder")
        self.logic = base64.Logic()
        self.options = [
            "base64",
            "CaesarsCipher",
            "RSA"
        ]
            
        # Place a label with the text "Encoder and Decoder" at the top of the window
        Label(self.root, text="Encoder and Decoder", font = "arial 20 bold").pack()
        
        self.selection = StringVar()
        self.selection.set("Choose Encryption Method")

        self.drop = OptionMenu(self.root, self.selection, *self.options)
        self.drop.pack(padx=10, pady=10)
        
        self.button = Button(self.root, text="Open", command=lambda:self.open(self.selection.get()))
        self.button.pack(padx=10, pady=10)
        
        self.root.mainloop()
    
    def open(self, encoder):
        if (encoder == "RSA"):
            RSAView.EncoderDecoderView(rsa.Logic())
        else:
            if (encoder == "CaesarsCipher"):
                self.logic = caesar.Logic()
            elif(encoder == "base64"):
                self.logic = base64.Logic()
            View.EncoderDecoderView(self.logic)


        
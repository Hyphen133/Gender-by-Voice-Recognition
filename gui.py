import tkinter as tk                # python 3
from enum import Enum
from tkinter import font  as tkfont # python 3

from PIL import Image, ImageTk
import matplotlib.pyplot as plt



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('600x500')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (RecordingPage, GenederRecognitionPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("RecordingPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class RecordingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Start Recording",
                            command=lambda: controller.show_frame("GenederRecognitionPage"))
        button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button.pack()


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


class GenederRecognitionPage(tk.Frame):

    def __init__(self, parent, controller):
        self.gender = Gender.FEMALE

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.draw_widgets()

    def draw_widgets(self):
        label = tk.Label(self, text="Currently speaking gender", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.paint_image_label()

        button = tk.Button(self, text="End recording!",
                           command=lambda: self.controller.show_frame("RecordingPage"))

        button.pack()

        button2 = tk.Button(self, text="Change label!",
                            command=self.change_gender)

        button2.pack()

    def paint_image_label(self):
        # http://effbot.org/pyfaq/why-do-my-tkinter-images-not -appear.htm
        img = Image.open(self.gender.value + ".png").resize((300, 300))
        self.image_label = ImageTk.PhotoImage(img)
        self.label = tk.Label(self, image=self.image_label)
        self.label.pack()

        return img

    def set_gender(self, gender):
        if self.gender != gender:
            self.gender = gender
            self.redraw_widgets()


    def change_gender(self):
        if self.gender == Gender.MALE:
            self.gender = Gender.FEMALE
        else:
            self.gender = Gender.MALE

        self.redraw_widgets()

    def redraw_widgets(self):
        self.destroy_widgets()
        self.draw_widgets()

    def destroy_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
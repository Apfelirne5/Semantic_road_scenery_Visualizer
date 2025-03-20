from tkinter import *
from tkinter import filedialog
import xml.etree.ElementTree as ET
from pathlib import Path
from visualize_bssd import open_html
from visualize_one_way import open_html_way
from visualize_network import vis_network


root = Tk()
root.title('GUI BSSD')
root.geometry("1000x600")


def open_xml_file():
    file_path = filedialog.askopenfilename()
    my_label.config(text=file_path)
    path = Path(file_path)

    tree = ET.parse(path.name)
    bssd = tree.getroot()
    open_html(bssd)


def open_one_way():
    file_path = filedialog.askopenfilename()
    my_label.config(text=file_path)
    path = Path(file_path)

    tree = ET.parse(path.name)
    bssd = tree.getroot()
    way_id = str(e.get())
    open_html_way(bssd, way_id)

    
def open_network():
    file_path = filedialog.askopenfilename()
    my_label.config(text=file_path)
    path = Path(file_path)

    tree = ET.parse(path.name)
    bssd = tree.getroot()
    vis_network(bssd)


title = Label(root, text="BSSD Visualizer", font=("Arial", 44))
title.pack(padx=10, pady=(0, 0))

my_label = Label(root, text="")
my_label.pack(padx=10, pady=(50, 0))


label1 = Label(root, text="Visualize all ways", bg="lightgreen")
label1.pack(fill="x", padx=10, pady=(20, 0))

button_open_file = Button(root, text= "Display all BSSD Ways", padx=50, pady=20, bg="lightblue", command=open_xml_file)
button_open_file.pack()

label2 = Label(root, text="Enter BSSD way-ID to to visualize way", bg="lightgreen")
label2.pack(fill="x", padx=10, pady=(50, 0))

e = Entry(root, width=5, borderwidth=5)
e.pack()

button_open_one_way = Button(root, text= "Display BSSD Way", padx=50, pady=20, bg="lightblue", command=open_one_way)
button_open_one_way.pack()

label3 = Label(root, text="Visualize roadnetwork", bg="lightgreen")
label3.pack(fill="x", pady=(50, 0))

button_open_html = Button(root, text= "Display Network", padx=50, pady=20, bg="lightblue", command=open_network)
button_open_html.pack()

root.mainloop()


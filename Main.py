import os
import tkinter as tk
from tkinter import filedialog
from Utilization.undrestand_facilities import *
from Utilization.constants import *
from Utilization.source_meter import *

class Main:

    def __init__(self):
        self.main()

    def main(self):
        win = tk.Tk()
        win.title('Name Smell Detector And Readability Improvement')
        win.geometry('600x100')
        setPathbtn = tk.Button(win, text='SetPath', command=lambda: self.search_for_file_path(win))
        setPathbtn.pack(side=tk.LEFT)
        ExtractUdbsbtn = tk.Button(win, text='ExtractUdbs', command=create_understand_database_from_project)
        ExtractUdbsbtn.pack(side=tk.LEFT)
        ExtractSourceMeterbtn = tk.Button(win, text='ExtractSourceMeter', command=source_meter_extract)
        ExtractSourceMeterbtn.pack(side=tk.LEFT)
        win.mainloop()

    def search_for_file_path(self,root):
        directory = tk.filedialog.askdirectory(parent=root, initialdir=r'C:/', title='Please Select Java Project Directory TO Extract Udbs')
        rootpath = directory + "/"
        os.chdir(rootpath)
        return   rootpath

  
if __name__ == '__main__':
    Main()
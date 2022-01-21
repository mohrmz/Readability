import os
import tkinter as tk
import tkinter.filedialog
from Utilization.undrestand_facilities import *
from Utilization.constants import *
from Utilization.source_meter import *
from NameRecommendation.NameSmellRefactor import *


class Main:

    def __init__(self):
        self.main()

    def main(self):
        win = tk.Tk()
        win.title('Name Smell Detector And Readability Improvement')
        win.geometry('700x100')
        setPathbtn = tk.Button(win, text='Set Path', command=lambda: self.search_for_file_path(win))
        setPathbtn.pack(side=tk.LEFT)
        #ExtractUdbsbtn = tk.Button(win, text='Extract Udb Files', command=create_understand_database_from_project)
        #ExtractUdbsbtn.pack(side=tk.LEFT)
        ExtractSourceMeterbtn = tk.Button(win, text='Extract Source Meter Metrics', command=source_meter_extract_metrics)
        ExtractSourceMeterbtn.pack(side=tk.LEFT)
        PreProccessSourceMeterMetrics = tk.Button(win, text='Pre Proccess Source Meter Metrics Files', command=source_meter_pre_proccess_metric_csv_files)
        PreProccessSourceMeterMetrics.pack(side=tk.LEFT)
        NameSmellRefactor = tk.Button(win, text='NameSmell Refactor', command=namesmell_refactor)
        NameSmellRefactor.pack(side=tk.LEFT)
        win.mainloop()

    def search_for_file_path(self,root):
        directory = tk.filedialog.askdirectory(parent=root, initialdir=r'D:/RamezaniEftekharZadeh/java-med/java-med/training', title='Please Select Java Project Directory TO Extract Udbs')
        rootpath = directory + "/"
        os.chdir(rootpath)
        return   rootpath

  
if __name__ == '__main__':
    Main()
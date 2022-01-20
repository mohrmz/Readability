def split_files(self,inputfile,index):
    return [inputfile.iloc[:, index:], inputfile.iloc[:, :index]]


def pre_process(self,metric_file):   
    csv_file = pd.read_csv(metric_file, index_col=None, header=None, low_memory=False)
    csv_file = csv_file.iloc[1:, :]
    csv_file = csv_file.iloc[:, :].replace([None], np.nan)
    csv_file = csv_file.iloc[:, :].replace('None', np.nan)
    csv_file = csv_file.iloc[:, :].replace('NaN', np.nan)
    csv_file = csv_file[re[3].notna()]
    csv_file.iloc[:, 4:] = Normalizer().fit_transform(csv_file.iloc[:, 4:].replace(np.nan, 0))
    return normalized_files.append(csv_file)

def split_files(self,inputfile):
    return [inputfile.iloc[:, 4:], inputfile.iloc[:, :4]]
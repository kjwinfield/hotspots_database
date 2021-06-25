import pandas as pd

class Data:
    def __init__(self, data_path):
        self.create_dataframe(data_path)
    
    def create_dataframe(self, path):
        data_df = pd.read_excel(path)
        self.df = data_df
    
    def split_genomic_positions(self):
        for index, row in self.df.iterrows():
            
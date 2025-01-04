import yfinance as yf
import pandas as pd 


class DataImportEnginnering():

    def __init__(self,stock_list,start_date, end_date, period,colone):
        
        self.stock_list = stock_list
        self.start_date = start_date
        self.end_date = end_date
        self.period = period 
        self.colone = colone

    def RawData(self):
        self.rawdata = {stock:yf.download(stock,start=self.start_date,end=self.end_date,period=self.period)[self.colone] for stock in self.stock_list}
        return self.rawdata 
        

    def normalize(self,data): 
        self.data = data
        self.value = data.agg(['min','max'])
        self.data_normalized = (data - self.value.loc['min']) / (self.value.loc['max'] - self.value.loc['min'])
        self.data_normalized.fillna(method = 'ffill',inplace = True)

        return self.data_normalized 

    def Fill_Na(self,data):
        self.data = data 
        data.ffill(axis = 0,inplace =True )
        data.bfill(axis =0,inplace = True)
        return data
    
    def Dictionnary_to_Dataframe(self,dictionnaire):
        data_list = [dictionnaire[stock] for stock in dictionnaire.keys()]
        data = pd.DataFrame(data_list[0])
        for z in data_list[1:]:
            z= pd.DataFrame(z)
            stock_name = z.columns[0]
            data[stock_name] = z[stock_name]
        return data

    

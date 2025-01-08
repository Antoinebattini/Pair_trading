import numpy as np
import pandas as pd 

class Signaux():

    def __init__(self,data,threshold):
        self.data = data
        self.threshold = threshold


    def entry_points(self):
        df = self.data.copy()
        mean = df.mean(axis=0)
        std = df.std(axis =0)
        df = ((df< mean - self.threshold *std) ^( df> mean + self.threshold*std ))*1
        df = (df!=df.shift(1))*1
        df.iloc[0] = 0
        df = (df.cumsum()!=df.cumsum().shift(1))*(df.cumsum())
        #ici il faudra modifier le code pour essayer de créer de meilleur signaux
        # dans l'idée si j'ai 2 signaux qui se suivent je ne trade pas 
        # On verra ca une fois qu'on aura créer des fees pour le rebalancement
        # par exemple [1020030040050006],il peut être pas mal de mettre une 
        #période minimum de trade, comme tu le disais mais dasn ce cas on sort "déjà"
        #du cadre arbitrage pur
        df= df.applymap(
            lambda i: np.nan if i == 0 else ('green' if i % 2 == 1 else 'red')
            )
        df.iloc[:,:1] = self.data.iloc[:,:1]
        return df

        

    def trading_signals(data,colone):

        mean = data[colone].mean()
        std = data[colone].std()
        data['above_threshold'] = 0
        data['above_mean'] = 0
        data ['GAT'] = 0  #'GAT' stand for go above the threshold 
        data ['GUM'] = 0 
        data.loc[ (data[colone] > mean +std), 'above_threshold' ] = 1
        data.loc[ (data[colone] > mean), 'above_mean' ] = 1
        data.loc[ ( data['above_threshold'] - data['above_threshold'].shift(1)) >0, 'GAT'] = 1
        data.loc[ ( data['above_mean'] - data['above_mean'].shift(1)) <0, 'GUM'] = -1
        data['Signal'] = data['GAT'] + data['GUM']
        acc = 0 
        data['Signal_up'] = [(acc := min(acc + x, 1)) for x in data['Signal']]
        data['In'] = (data['Signal_up'] > data['Signal_up'].shift(1)) *1
        data['Out'] = (data['Signal_up'] < data['Signal_up'].shift(1)) * -1
        data ['Trading_points']= data['Out'] + data['In']
        data.drop(['above_threshold','above_mean','GAT','GUM','Signal','In','Out','Signal_up'], axis = 1, inplace = True)

        return data 








class Trading():
    def __init__(self):
        pass
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
        df.iloc[:,:1] = self.self.data.iloc[:,:1]
        return df

        

    def trading_signals_buy(self,colone):
        mean = self.data[colone].mean()
        std = self.data[colone].std()
        self.data['above_threshold'] = 0
        self.data['above_mean'] = 0
        self.data['GAT'] = 0  #'GAT' stand for go above the threshold 
        self.data['GUM'] = 0 
        self.data.loc[ (self.data[colone] > mean +std), 'above_threshold' ] = 1
        self.data.loc[ (self.data[colone] > mean), 'above_mean' ] = 1
        self.data.loc[ ( self.data['above_threshold'] - self.data['above_threshold'].shift(1)) >0, 'GAT'] = 1
        self.data.loc[ ( self.data['above_mean'] - self.data['above_mean'].shift(1)) <0, 'GUM'] = -1
        self.data['Signal'] = self.data['GAT'] + self.data['GUM']
        acc = 0 
        self.data['Signal_up'] = [(acc := max(min(acc + x, 1),0)) for x in self.data['Signal']]
        self.data['In'] = (self.data['Signal_up'] > self.data['Signal_up'].shift(1)) *1
        self.data['Out'] = (self.data['Signal_up'] < self.data['Signal_up'].shift(1)) * -1
        self.data['Trading_points']= self.data['Out'] + self.data['In']

        return self.data['Trading_points'] 

    def trading_signals_sell(self,colone):

        mean = self.data[colone].mean()
        std = self.data[colone].std()
        self.data['under_threshold'] = 0
        self.data['under_mean'] = 0
        self.data ['GUT'] = 0  #'GUT' stand for go under the threshold 
        self.data ['GAM'] = 0 
        self.data.loc[ (self.data[colone] < mean  - std), 'under_threshold' ] = 1
        self.data.loc[ (self.data[colone] > mean), 'under_mean' ] = 1
        self.data.loc[ ( self.data['under_threshold'] - self.data['under_threshold'].shift(1)) >0, 'GUT'] = 1
        self.data.loc[ ( self.data['under_mean'] - self.data['under_mean'].shift(1)) <0, 'GAM'] = -1
        self.data['Signal'] = self.data['GUT'] + self.data['GAM']
        acc = 0 
        self.data['Signal_up'] = [(acc := max(min(acc + x, 1),0)) for x in self.data['Signal']]
        self.data['In'] = (self.data['Signal_up'] < self.data['Signal_up'].shift(1)) *1
        self.data['Out'] = (self.data['Signal_up'] > self.data['Signal_up'].shift(1)) * -1
        self.data['Trading_points']= self.data['Out'] + self.data['In']

        return self.data['Trading_points'] 


    def trading_signals(self,colone):
        return Signaux.trading_signals_sell(self,colone) + Signaux.trading_signals_buy(self,colone)



class Trading():
    def __init__(self):
        pass
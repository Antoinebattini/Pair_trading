import numpy as np
import pandas as pd 

class Signaux():

    def __init__(self,data,threshold):
        self.data = data
        self.threshold = threshold


    def entry_points_up(self):
        portfolio = self.data.copy()
        mean = portfolio.mean(axis=0)
        std = portfolio.std(axis =0)
        signals_up = pd.DataFrame(np.array([portfolio,np.zeros(len(portfolio)),np.zeros(len(portfolio))]).T,columns=['Portfolio','up','center'])
        signals_up.loc[signals_up['Portfolio']> mean + self.threshold * std ,'up'] = 1
        signals_up.loc[signals_up['Portfolio']> mean ,'center'] = 1
        signals_up['Somme'] = signals_up.loc[:,'up'] + signals_up.loc[:,'center']
        signals_up['Signal'] = np.zeros(len(portfolio))
        i=0
        while i < len(portfolio):
            if signals_up.loc[i,'Somme'] == 2:
                # Vérifier si c'est un "2 majeur"
                if i == 0 or signals_up.loc[i-1,'Somme'] != 2:
                    signals_up.loc[i,'Signal'] = 1  # Marquer le "2 majeur"
                    # Chercher le premier 0 après ce "2 majeur"
                    j = i + 1
                    while j < len(original):
                        if signals_up.loc[j,'Somme'] == 0:
                            signals_up.loc[j,'Signal'] = -1
                            break
                        j += 1
            i += 1
        return signals_up

    def entry_points_down(self):
        portfolio = self.data.copy()
        mean = portfolio.mean(axis=0)
        std = portfolio.std(axis =0)
        signals_down = pd.DataFrame(np.array([portfolio,np.zeros(len(portfolio)),np.zeros(len(portfolio))]).T,columns=['Portfolio','down','center'])
        signals_down.loc[signals_down['Portfolio']< mean - self.threshold * std ,'down'] = 1
        signals_down.loc[signals_down['Portfolio']< mean ,'center'] = 1
        signals_down['Somme'] = signals_down.loc[:,'down'] + signals_down.loc[:,'center']
        signals_down['Signal'] = np.zeros(len(portfolio))
        i=0
        while i < len(portfolio):
            if signals_down.loc[i,'Somme'] == 2:
                # Vérifier si c'est un "2 majeur"
                if i == 0 or signals_down.loc[i-1,'Somme'] != 2:
                    signals_down.loc[i,'Signal'] = 1  # Marquer le "2 majeur"
                    # Chercher le premier 0 après ce "2 majeur"
                    j = i + 1
                    while j < len(original):
                        if signals_down.loc[j,'Somme'] == 0:
                            signals_down.loc[j,'Signal'] = -1
                            break
                        j += 1
            i += 1
        return signals_down

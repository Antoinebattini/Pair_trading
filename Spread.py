import statsmodels.api as sm
import numpy as np 
import pandas as pd

class Spread:

    def __init__(self, dictionnaire):
        self.dictionnaire = dictionnaire
        

    def dollar_neutral_spread(self):
        dictionnaire = self.dictionnaire
        for key,values in dictionnaire.items():
            values['Delta'] = np.abs(values[key[0]]/values[key[1]])
            values['Delta_norm'] = (values['Delta'] - values['Delta'].rolling(10).mean()) / values['Delta'].rolling(10).std()
            values.drop(['Delta'], axis = 1, inplace=True )
    
        return dictionnaire 

    def beta_neutral_spread(self): 

        dictionnaire = self.dictionnaire
        for key,values in dictionnaire.items():
            x = values[key[0]]
            y = values[key[1]]

            data = pd.concat([x, y], axis=1).replace([np.inf, -np.inf], np.nan).dropna()
            x_clean = data.iloc[:, 0]
            y_clean = data.iloc[:, 1]
            
            x_clean = sm.add_constant(x_clean)
            model =sm.OLS(x_clean,y_clean)
            results = model.fit()
            beta = results.params[1]

            values['Delta'] = np.abs(values[key[0]] - values[key[1]]*beta)
            values['Delta_norm'] = (values['Delta'] - values['Delta'].rolling(10).mean()) / values['Delta'].rolling(10).std()
            values.drop(['Delta'], axis = 1, inplace=True )
        return dictionnaire

    def dollar_neutral_spread2(self):
        dictionnaire = self.dictionnaire #non normalised data
        for key,values in dictionnaire.items():

            Series1 = values[key[0]]
            Series2 = values[key[1]]

            data = pd.concat([Series1, Series2], axis=1).replace([np.inf, -np.inf], np.nan).dropna()
            Series1_clean = data.iloc[:, 0]
            Series2_clean = data.iloc[:, 1]

            Series1_sum = Series1_clean.apply(np.sum)
            Series2_sum = Series2_clean.apply(np.sum)
            dollar_coef = Series1_sum/Series2_sum

            values['Delta'] = np.abs(values[key[0]] - values[key[1]]*dollar_coef)
            values['Delta_norm'] = (values['Delta'] - values['Delta'].rolling(10).mean()) / values['Delta'].rolling(10).std()
            values.drop(['Delta'], axis = 1, inplace=True )
        return dictionnaire            
            
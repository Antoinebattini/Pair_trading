import statsmodels.api as sm
import numpy as np 

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

            x = sm.add_constant(x)
            model =sm.OLS(x,y)
            results = model.fit()
            beta = results[1]

            values['Delta'] = np.abs(values[key[0]] - values[key[1]]*beta)
            values['Delta_norm'] = (values['Delta'] - values['Delta'].rolling(10).mean()) / values['Delta'].rolling(10).std()
            values.drop(['Delta'], axis = 1, inplace=True )
        return dictionnaire

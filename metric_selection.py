import numpy as np 
import pandas as pd 


class Pair_Selection:
    
    @staticmethod 
    def spread_time_series(x:list,y:list):
        model =sm.OLS(x,y)
        results = model.fit()
        #print(results.params)
        beta = results.params[0]
        return x - beta*y

    def compute_correlation(data):
        df = data.copy()
        data_1 = df.corr()
        return data_1 
    
    def __init__(self,data,number_of_pair,stock_list_sector,sector_list,sector_neutral):
        self.data = data
        self.number_of_pair = number_of_pair
        self.stock_list_sector = stock_list_sector
        self.sector_list = sector_list
        self.sector_neutral = sector_neutral
    
    def compute_euclidian_distance(self):
        data = self.data
        distances = np.zeros((data.shape[1], data.shape[1]))

        for col in data.columns:
            for col2 in data.columns:
                distances[data.columns.get_loc(col)][data.columns.get_loc(col2)] = np.sqrt(
                    ((data[col] - data[col2]) ** 2).sum()
                )
        
        distances_df = pd.DataFrame(distances, columns=data.columns, index=data.columns)
        return distances_df
    
    def compute_correlation(self):
        data = self.data
        data_1 = data.corr()
        return data_1 
    
    def metrics(self,name):
        if name=='angular_distance':
            return np.sqrt((1/2)*(1 - Pair_Selection.compute_correlation(self.data)))
        elif name == 'absolute_angular_distance':
            return np.sqrt(1 - np.abs(Pair_Selection.compute_correlation(self.data)))
        elif name == 'squared_angular_distance':
            return np.sqrt(1 - Pair_Selection.compute_correlation(self.data)**2)
    
  
    
    
    def augmented_dickey_fuller_selection(self,x:list,y:list,p =0.01):
        spread = Pair_Selection.spread_time_series(x,y)
        #print(spread)
        p_value = adfuller(spread,regression ='ct')[1]
        if p_value < p: 
            return True
        else:
            return False


    def paire_selection_2(self,pairs,p):
        selected_pairs = [pair*(Pair_Selection.augmented_dickey_fuller_selection(self,np.array(self.data[pair[0]]),np.array(self.data[pair[1]]),p=p)) for pair in pairs ]
        selected_pairs = [i  for i in selected_pairs if i!=()]

        return selected_pairs
    
    def paire_selection(self,distances,number_of_pair, stock_list_sector, sector_list,pairs):
        selected_pairs ={} 
        if self.sector_neutral :
            for sector in stock_list_sector:
                l = stock_list_sector[sector]
                distances1 = distances.loc[l][l] 
                #np.fill_diagonal(distances1.values, 1000)
                #minimum_values = np.unique((np.array(distances1).reshape(-1,1)))
                distances1.values[np.triu_indices_from(distances1, k=0)] = np.inf
                distances1 = distances1.stack()
                if distances1.shape[0]>2:
                    minimum_values = distances1.nsmallest(number_of_pair)
                    selected_pairs[sector] = minimum_values.index.tolist()            
                #if len(minimum_values) > 2:
                    #minimum_values = minimum_values[number_of_pair:number_of_pair+1]
                    #distances1 = distances1[distances1<minimum_values[0]]
                    #pair_list = list(distances1[distances1.notna()].stack().index)
                    #pair_list = [tuple(sorted(pair)) for pair in pair_list]
                    #selected_pairs[sector] = [values for values in pairs[sector] if values in pair_list]
                else:
                    selected_pairs[sector] = pairs[sector]
        else : 
            distances1 = distances.copy()
            distances1.values[np.triu_indices_from(distances1, k=0)] = np.inf
            distances1 = distances1.stack()
            smallest = distances1.nsmallest(number_of_pair)
            #print(smallest)
            selected_pairs = smallest.index.tolist()

        return selected_pairs




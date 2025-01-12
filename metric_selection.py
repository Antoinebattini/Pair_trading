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




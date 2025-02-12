

class portfolio():
    def __init__(self, data, capital, sl_threshold):
        self.data = data
        self.capital = capital
        self.stop_loss_threshold = sl_threshold
        
    def portfolio_creation(self):
        portfolio = {}
        window = 60

        for key,value in self.data.items():
            portfolio[key] = portfolio[key].drop([key[0],key[1]],axis=1)
            portfolio[key][key[0]] = value.loc[:,key[0]]
            portfolio[key][key[1]] = value.loc[:,key[1]]
            portfolio[key]['open_if_odd'] = np.cumsum(np.abs(portfolio[key]['trading_signals']))
            portfolio[key]['dollar_ratio'] = np.where((portfolio[key]['open_if_odd'] % 2 == 1) & (portfolio[key]['trading_signals'] != 0), portfolio[key][key[0]]/portfolio[key][key[1]], None)
            portfolio[key]['dollar_ratio'] = portfolio[key]['dollar_ratio'].ffill()
            portfolio[key]['Capital'] = self.capital/len(self.data) + np.cumsum(portfolio[key]['trading_signals']*(-portfolio[key][key[0]]+portfolio[key]['dollar_ratio']*portfolio[key][key[1]]))
            portfolio[key]['Portfolio'] = portfolio[key]['portfolio_units']*(portfolio[key][key[0]]-portfolio[key]['dollar_ratio']*portfolio[key][key[1]])
            portfolio[key]['spread_mean'] = portfolio[key]['Delta_norm'].rolling(window=window).mean()
            portfolio[key]['spread_std'] = portfolio[key]['Delta_norm'].rolling(window=window).std()
            portfolio[key]['upper_stop'] = portfolio[key]['spread_mean'] + self.stop_loss_threshold * portfolio[key]['spread_std']
            portfolio[key]['lower_stop'] = portfolio[key]['spread_mean'] - self.stop_loss_threshold * portfolio[key]['spread_std']
            portfolio[key]['stop_loss'] = np.where(
            ((portfolio[key]['Delta_norm'] > portfolio[key]['upper_stop']) & (portfolio[key]['portfolio_units'] != 0)) |
            ((portfolio[key]['Delta_norm'] < portfolio[key]['lower_stop']) & (portfolio[key]['portfolio_units'] != 0)),
            -portfolio[key]['portfolio_units'],0)
            for i in range(len(portfolio[key]['stop_loss'])):
                if portfolio[key].iloc[i]['stop_loss']!=0 :
                    for j in range(i+1,len(portfolio[key]['stop_loss'])):
                        if portfolio[key].iloc[j]['trading_signals']!=0 :
                            portfolio[key].iloc[i]['trading_signals'] = portfolio[key].iloc[j]['trading_signals']
                            portfolio[key].iloc[j]['trading_signals'] = 0
            portfolio[key] = portfolio[key].drop(['open_if_odd','spread_mean','spread_std','upper_stop','lower_stop'],axis=1)
            
        return portfolio
        
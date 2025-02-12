import numpy as np

class portfolio():
    def __init__(self, data, data_raw, capital, sl_threshold):
        self.data = data
        self.data_raw = data_raw
        self.capital = capital
        self.stop_loss_threshold = sl_threshold
        
    def portfolio_creation(self):
        self.portfolio = {}
        
        for key,value in self.data.items():
            self.portfolio[key] = value
            
        for key,value in self.data_raw.items():
            self.portfolio[key] = self.portfolio[key].drop([key[0],key[1]],axis=1)
            self.portfolio[key][key[0]] = value.loc[:,key[0]]
            self.portfolio[key][key[1]] = value.loc[:,key[1]]
            self.portfolio[key]['open_if_odd'] = np.cumsum(np.abs(self.portfolio[key]['trading_signals']))
            self.portfolio[key]['dollar_ratio'] = np.where((self.portfolio[key]['open_if_odd'] % 2 == 1) & (self.portfolio[key]['trading_signals'] != 0), self.portfolio[key][key[0]]/self.portfolio[key][key[1]], None)
            self.portfolio[key]['dollar_ratio'] = self.portfolio[key]['dollar_ratio'].ffill()
            self.portfolio[key]['Capital'] = self.capital/len(self.data_raw) + np.cumsum(self.portfolio[key]['trading_signals']*(-self.portfolio[key][key[0]]+self.portfolio[key]['dollar_ratio']*self.portfolio[key][key[1]]))
            self.portfolio[key]['portfolio'] = self.portfolio[key]['portfolio_units']*(self.portfolio[key][key[0]]-self.portfolio[key]['dollar_ratio']*self.portfolio[key][key[1]])
            self.portfolio[key]['spread_mean'] = self.portfolio[key]['Delta_norm'].rolling(window=window).mean()
            self.portfolio[key]['spread_std'] = self.portfolio[key]['Delta_norm'].rolling(window=window).std()
            self.portfolio[key]['upper_stop'] = self.portfolio[key]['spread_mean'] + self.stop_loss_threshold * self.portfolio[key]['spread_std']
            self.portfolio[key]['lower_stop'] = self.portfolio[key]['spread_mean'] - self.stop_loss_threshold * self.portfolio[key]['spread_std']
            self.portfolio[key]['stop_loss'] = np.where(
            ((self.portfolio[key]['Delta_norm'] > self.portfolio[key]['upper_stop']) & (self.portfolio[key]['portfolio_units'] != 0)) |
            ((self.portfolio[key]['Delta_norm'] < self.portfolio[key]['lower_stop']) & (self.portfolio[key]['portfolio_units'] != 0)),
            -self.portfolio[key]['portfolio_units'],0)
            for i in range(len(self.portfolio[key]['stop_loss'])):
                if self.portfolio[key].iloc[i]['stop_loss']!=0 :
                    for j in range(i+1,len(self.portfolio[key]['stop_loss'])):
                        if self.portfolio[key].iloc[j]['trading_signals']!=0 :
                            self.portfolio[key].iloc[i]['trading_signals'] = self.portfolio[key].iloc[j]['trading_signals']
                            self.portfolio[key].iloc[j]['trading_signals'] = 0
            self.portfolio[key] = self.portfolio[key].drop(['open_if_odd'],axis=1)
            
        return self.portfolio
    
    def stop_loss(self):
        window = 60
        
        for key,value in self.portfolio.items():
            self.portfolio[key]['spread_mean'] = self.portfolio[key]['Delta_norm'].rolling(window=window).mean()
            self.portfolio[key]['spread_std'] = self.portfolio[key]['Delta_norm'].rolling(window=window).std()
            self.portfolio[key]['upper_stop'] = self.portfolio[key]['spread_mean'] + self.stop_loss_threshold * self.portfolio[key]['spread_std']
            self.portfolio[key]['lower_stop'] = self.portfolio[key]['spread_mean'] - self.stop_loss_threshold * self.portfolio[key]['spread_std']
            self.portfolio[key]['stop_loss'] = np.where(
            ((self.portfolio[key]['Delta_norm'] > self.portfolio[key]['upper_stop']) & (self.portfolio[key]['portfolio_units'] != 0)) |
            ((self.portfolio[key]['Delta_norm'] < self.portfolio[key]['lower_stop']) & (self.portfolio[key]['portfolio_units'] != 0)),
            -self.portfolio[key]['portfolio_units'],0)
            for i in range(len(self.portfolio[key]['stop_loss'])):
                if self.portfolio[key].iloc[i]['stop_loss']!=0 :
                    for j in range(i+1,len(self.portfolio[key]['stop_loss'])):
                        if self.portfolio[key].iloc[j]['trading_signals']!=0 :
                            self.portfolio[key].iloc[i]['trading_signals'] = self.portfolio[key].iloc[j]['trading_signals']
                            self.portfolio[key].iloc[j]['trading_signals'] = 0
            self.portfolio[key] = self.portfolio[key].drop(['spread_mean','spread_std','upper_stop','lower_stop'],axis=1)
            
        return self.portfolio
                
        
    def time_stop(self):
        '''We want to estimate the time of mean reversion of the pair, so that we stop the trade when the trade is open for too long
        compared to the time of mean reversion. To do that we fit the Orstein Uhlenbeck model on the spread of the pair. Since we are
        in discrete time, we will approximate it by an AR(1) process. We have dx_t = (phi-1)*x_t-1 + (1-phi)*mu + epsilon_t. Let 
        alpha = (1-phi)*mu and beta = (phi-1), we obtain a linear equation for which we solve for the parameters with OLS. Then
        phi = beta - 1 and theta (speed of mean reversion) = -ln(phi) and finally T (half life) = ln(2)/theta.'''
        
        for key,value in self.portfolio.items():
            spread_lag = self.portfolio[key]['Delta_norm'].shift(1)
            spread_diff = self.portfolio[key]['Delta_norm'] - spread_lag

            spread_lag = spread_lag.dropna()
            spread_diff = spread_diff.dropna()

            X = sm.add_constant(spread_lag)
            model = sm.OLS(spread_diff, X).fit()
            beta = model.params[1]

            phi_est = beta + 1

            theta_est = -np.log(phi_est)

            half_life = np.log(2) / theta_est
            
            self.portfolio[key]['half_life'] = half_life
        
        return self.portfolio

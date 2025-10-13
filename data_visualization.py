import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np 

class Data_Visualization():

    def __init__(self):
        pass

    def metric(self,data,title,xlabel,ylabel):
        self.data = data
        self.title = title 
        self.xlabel = xlabel
        self.ylabel = ylabel 
        
        plt.figure(figsize=(8, 6))
        cmap = sns.diverging_palette(220, 20, as_cmap=True)
        sns.heatmap(data, cmap=cmap, annot=False, fmt=".1f", linewidths=.5)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.show()


    def pair_historic(self,data):
        df = data.copy()
        fig = go.Figure()
        buttons = []
        visibility=[]
        i = 0 
        for pair,dataframe in df.items():
            fig.add_trace(go.Scatter(
                    x=dataframe.index, 
                    y=dataframe[str(pair[0])], 
                    mode='lines', 
                    name=str(pair),
                    visible=False))
            visibility.append(False)
            fig.add_trace(go.Scatter(
                    x=dataframe.index, 
                    y=dataframe[str(pair[1])], 
                    mode='lines', 
                    name=str(pair),
                    visible=False))
            visibility.append(False)

            button_visibility = [False]*2*len(df)
            button_visibility[i * 2] = True  
            button_visibility[i * 2 + 1] = True 
            i+=1
            buttons.append({"label": str(pair),"method": "update","args": [{"visible": button_visibility}]}) 
        buttons.append({
                "label": "Show All",
                "method": "update",
                "args": [{"visible": [True] * len(visibility)}]
            })

        buttons.append({
                "label": "Hide All",
                "method": "update",
                "args": [{"visible": [False] * len(visibility)}]
            })

        fig.update_layout(
            updatemenus=[
                {
                    "buttons":buttons,
                    "direction": "down",
                    "showactive": True,
                    "x": 0.5,
                    "y": 1.15,
                    "xanchor": "right",
                    "yanchor": "top"
                }
            ]
            )

        fig.update_layout(
                title='normalized prices',
                
                xaxis_title="Date",
                yaxis_title="Normalized Prices",
                hovermode="x unified"
        )

        fig.show()
            


    def Entry_trading_points(self,data):
            df_test = data.copy()
            fig = go.Figure()
            buttons = []
            visibility=[]

            i = 0
            for pair,dataframe in df_test.items():
                
                up_signals =dataframe[dataframe['trading_signals'] == 1]
                down_signal = dataframe[dataframe['trading_signals'] == -1]

                fig.add_trace(go.Scatter(
                    x=dataframe.index, 
                    y=dataframe.Delta_norm, 
                    mode='lines', 
                    name=str(pair),
                    visible=False))
                visibility.append(False)
                fig.add_trace(go.Scatter(
                    x=up_signals.index, 
                    y=up_signals['Delta_norm'], 
                    mode='markers', 
                    name = f'Buy signal for {str(pair)}',
                    marker=dict(size=10, symbol='triangle-up', color='green'),
                    visible=False
                ))
                visibility.append(False)
                fig.add_trace(go.Scatter(
                    x=down_signal.index, 
                    y=down_signal['Delta_norm'], 
                    mode='markers', 
                    name = f'Sell_signal for {str(pair)}',
                    marker=dict(size=10, symbol='triangle-down', color='red'),
                    visible=False
                ))
                visibility.append(False)
                

                button_visibility = [False]*3*len(df_test)
                button_visibility[i * 3] = True  
                button_visibility[i * 3 + 1] = True  
                button_visibility[i * 3 + 2] = True 
                i+=1
                buttons.append({"label": str(pair),"method": "update","args": [{"visible": button_visibility}]}) 
            buttons.append({
                    "label": "Show All",
                    "method": "update",
                    "args": [{"visible": [True] * len(visibility)}]
                })
            buttons.append({
                    "label": "Hide All",
                    "method": "update",
                    "args": [{"visible": [False] * len(visibility)}]
                })

            fig.update_layout(
            updatemenus=[
                {
                    "buttons":buttons,
                    "direction": "down",
                    "showactive": True,
                    "x": 0.5,
                    "y": 1.15,
                    "xanchor": "right",
                    "yanchor": "top"
                }
            ]
            )

            fig.update_layout(
                title="Spread and Trading Signals",
                
                xaxis_title="Date",
                yaxis_title="Delta_norm",
                hovermode="x unified"
        )

            fig.show()
            

    def function_test():
        print('test')
        
    def portfolio_units(self,data):
        df = data.copy()
        fig = go.Figure()
        buttons = []
        visibility=[]
        i = 0 
        for pair,dataframe in df.items():
            fig.add_trace(go.Scatter(
                    x=dataframe.index, 
                    y=dataframe['portfolio_units'], 
                    mode='lines', 
                    name='Portfolio units to hold for' + str(pair),
                    visible=False))
            visibility.append(False)
            button_visibility = [False]*len(df)
            button_visibility[i] = True  
            button_visibility[i] = True 
            i+=1
            buttons.append({"label": str(pair),"method": "update","args": [{"visible": button_visibility}]}) 
        buttons.append({
                "label": "Show All",
                "method": "update",
                "args": [{"visible": [True] * len(visibility)}]
            })

        buttons.append({
                "label": "Hide All",
                "method": "update",
                "args": [{"visible": [False] * len(visibility)}]
            })
        fig.update_layout(
            updatemenus=[
                {
                    "buttons":buttons,
                    "direction": "down",
                    "showactive": True,
                    "x": 0.5,
                    "y": 1.15,
                    "xanchor": "right",
                    "yanchor": "top"
                }
            ]
            )

        fig.update_layout(
                title='Portfolio units',
                
                xaxis_title="Date",
                yaxis_title="Portfolio units to hold for the Pair",
                hovermode="x unified"
        )

        fig.show()
            

    def spread_plot(self,data):
        df = data.copy()
        fig = go.Figure()
        buttons = []
        visibility=[]
        i = 0 
        for pair,dataframe in df.items():
            fig.add_trace(go.Scatter(
                    x=dataframe.index, 
                    y=dataframe['Delta_norm'], 
                    mode='lines', 
                    name='Spread for pair' + str(pair),
                    visible=False))
            visibility.append(False)
            button_visibility = [False]*len(df)
            button_visibility[i] = True  
            button_visibility[i] = True 
            i+=1
            buttons.append({"label": str(pair),"method": "update","args": [{"visible": button_visibility}]}) 
        buttons.append({
                "label": "Show All",
                "method": "update",
                "args": [{"visible": [True] * len(visibility)}]
            })

        buttons.append({
                "label": "Hide All",
                "method": "update",
                "args": [{"visible": [False] * len(visibility)}]
            })

        fig.update_layout(
            updatemenus=[
                {
                    "buttons":buttons,
                    "direction": "down",
                    "showactive": True,
                    "x": 0.5,
                    "y": 1.15,
                    "xanchor": "right",
                    "yanchor": "top"
                }
            ]
            )

        fig.update_layout(
                title='Spread',
                
                xaxis_title="Date",
                yaxis_title="Spread for the Pair",
                hovermode="x unified"
        )

        fig.show()
            

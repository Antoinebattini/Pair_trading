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

        # Set up the matplotlib figure
        plt.figure(figsize=(8, 6))
        # Generate a custom colormap
        cmap = sns.diverging_palette(220, 20, as_cmap=True)
        # Draw the heatmap
        sns.heatmap(data, cmap=cmap, annot=False, fmt=".1f", linewidths=.5)
        # Add titles and labels
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        # Show the plot
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

            # Add a "Hide All" button
        buttons.append({
                "label": "Hide All",
                "method": "update",
                "args": [{"visible": [False] * len(visibility)}]
            })
        # Update layout for better visualization
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

        # Add layout properties
        fig.update_layout(
                title='normalized prices',
                
                xaxis_title="Date",
                yaxis_title="Normalized Prices",
                hovermode="x unified"
        )

        # Show plot
        fig.show()
            

        """plt.figure(figsize=(15, 20))
        x = data[key].index
        y1 = data[key][key[0]]
        y2 = data[key][key[1]]
        fig, ax1 = plt.subplots()

        # Plot on the first y-axis
        ax1.plot(x, y1, 'b-', label=f'{key[0]}')
        ax1.set_xlabel('Date')  # Common x-axis label
        ax1.set_ylabel(f'{key[0]}', color='b')  # First y-axis label
        ax1.tick_params(axis='y', labelcolor='b')  # Match tick labels with axis color

        # Create the second y-axis
        ax2 = ax1.twinx()  # This shares the same x-axis
        ax2.plot(x, y2, 'r-', label=f'{key[1]}')
        ax2.set_ylabel(f'{key[1]}', color='r')  # Second y-axis label
        ax2.tick_params(axis='y', labelcolor='r')  # Match tick labels with axis color

        # Add a legend
        fig.legend(loc="upper left", bbox_to_anchor=(0.01, 0.09))

        # Add a grid (optional)
        ax1.grid(True)

        # Show the plot
        plt.title(f"Plot for the pair ({key[0]},{key[1]})")
        plt.show()"""


    def portfolio_units(self,data,key):
        plt.figure(figsize=(20,5))
        plt.plot(data[key].index, data[key], 'orange', label = 'units to hold')
        plt.title("Portfolio units to hold")
        plt.xlabel("Date")
        plt.ylabel("Portfolio holdings")
        plt.legend()
        plt.show()

    def Entry_trading_points(self,data):
            df_test = data.copy()
            fig = go.Figure()
            buttons = []
            visibility=[]

            i = 0
            for pair,dataframe in df_test.items():
                
                 # Add the Delta_norm plot of the pair 'pair'
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
                

                # Add a button for this pair
                button_visibility = [False]*3*len(df_test)
                button_visibility[i * 3] = True  
                button_visibility[i * 3 + 1] = True  
                button_visibility[i * 3 + 2] = True 
                i+=1
                buttons.append({"label": str(pair),"method": "update","args": [{"visible": button_visibility}]}) 
                # Add a "Show All" button
            buttons.append({
                    "label": "Show All",
                    "method": "update",
                    "args": [{"visible": [True] * len(visibility)}]
                })

                # Add a "Hide All" button
            buttons.append({
                    "label": "Hide All",
                    "method": "update",
                    "args": [{"visible": [False] * len(visibility)}]
                })
                
        # Update layout for better visualization
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

        # Add layout properties
            fig.update_layout(
                title="Spread and Trading Signals",
                
                xaxis_title="Date",
                yaxis_title="Delta_norm",
                hovermode="x unified"
        )

        # Show plot
            fig.show()
            
            """
            # Plot X_i vs time as a line
            ax.plot(df_test.index, df_test[pair], label='X_i Value', color='blue', linewidth=2)

            # Plot upward triangles for 'green'
            green_points = df_test[df_test[h] == 1]
            ax.scatter(
                green_points.index,
                green_points[pair],
                marker=marker_map['green'],
                color=color_map['green'],
                s=100,  # Marker size
                label='Green Marker'
            )

            # Plot downward triangles for 'red'
            red_points = df_test[df_test[h]== -1]
            ax.scatter(
                red_points.index,
                red_points[pair],
                marker=marker_map['red'],
                color=color_map['red'],
                s=100,  # Marker size
                label='Red Marker'
            )

            # Customize the plot
            ax.set_xlabel('Time', fontsize=12)
            ax.set_ylabel(f'Spread pair {pair}', fontsize=12)
            ax.set_title(f'Trading entry points for the pair {pair}', fontsize=14)
            ax.legend()
            ax.grid(True)

            # Rotate x-axis labels for better readability
            plt.xticks(rotation=45)

            # Tight layout for better spacing
            plt.tight_layout()

            # Show the plot
            plt.show()"""


    def function_test():
        print(test)
import seaborn as sns 
import matplotlib.pyplot as plt 

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


    def pair_historic(self,data,key):
        plt.figure(figsize=(15, 20))
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
        plt.show()


    def portfolio_units(self,data,key):
        plt.figure(figsize=(20,5))
        plt.plot(data[key].index, data[key], 'orange', label = 'units to hold')
        plt.title("Portfolio units to hold")
        plt.xlabel("Date")
        plt.ylabel("Portfolio holdings")
        plt.legend()
        plt.show()


    def function_test():
        print(test)
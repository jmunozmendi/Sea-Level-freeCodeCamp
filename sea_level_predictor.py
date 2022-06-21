import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    regress = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_vals1 = np.arange(df['Year'].min(),2051,1)
    y_vals1 = regress.intercept + regress.slope * x_vals1
    plt.plot(x_vals1, y_vals1,'r')

    # Create second line of best fit
    new_df = df.loc[df['Year']>=2000]
    regress = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x_vals2 = np.arange(2000,2051,1)
    y_vals2 = regress.intercept + regress.slope * x_vals2
    plt.plot(x_vals2, y_vals2,'g')
    plt.show()

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
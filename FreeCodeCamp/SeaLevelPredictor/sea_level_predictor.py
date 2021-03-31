import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    df = pd.DataFrame(data)

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extra_years = list(range(1880, 2050, 1))
    line_best1 = [line1.intercept + line1.slope*xy for xy in extra_years]
    plt.plot(extra_years, line_best1, 'r')
    
    # Create second line of best fit
    data_only_after2000 = df[df['Year'] >= 2000]
    line2 = linregress(data_only_after2000['Year'], data_only_after2000['CSIRO Adjusted Sea Level'])
    other_years = list(range(2000, 2050, 1))
    line_best2 = [line2.intercept + line2.slope*exy for exy in other_years]
    plt.plot(other_years, line_best2, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    #Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea-level-plot.png')
    return plt.gca()

d = draw_plot()

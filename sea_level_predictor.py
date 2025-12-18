import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit (all data)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = range(1880, 2051)
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, color="red")

    # Line of best fit (from year 2000)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    x_recent = range(2000, 2051)
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    plt.plot(x_recent, y_recent, color="green")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()

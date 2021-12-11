import statistics
import csv
import pandas as pd
import plotly.express as plot_expres
data = [60,61,65,63,98,99,90,95,91,96]
data_std = statistics.stdev(data)
print(data_std)
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

read = pd.read_csv('data.csv')
data = read['reding_time'].tolist()

o_mean = statistics.mean(data)
print('Overall mean -->',o_mean)

def random_set(counter):
    dataset = []
    for i in range(0,counter):
        r = random.randint(0,len(data)-1) 
        value = data[r]
        dataset.append(value)
    mean = statistics.mean(dataset)

    return mean



mean_list = []
for i in range(1,100):
    blah = random_set(30)
    mean_list.append(blah)
mean1 = statistics.mean(mean_list)    
std = statistics.stdev(mean_list)
print('Mean of sample -->' , mean1)
print('SD of sample data -->',std)


def howFigure(meanlist):
    df = meanlist
    fig = ff.create_distplot([df],['Sample mean'], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean1 , mean1] , y= [0,0.12] , mode = "lines" , name = 'Mean of sample')) 
    fig.show()

howFigure(mean_list)            

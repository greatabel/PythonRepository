import plotly.graph_objects as go

trace1 = go.Scatter(  # <1>
    x=[1, 2, 3],  # <2>
    y=[4, 5, 6],  # <3>
    marker={'color': 'red', 'symbol': 104},  # <4>
    mode='markers+lines',  # <5>
    text=['one', 'two', 'three'],  # <6>
    name='1st Trace',
)


Defining a scatterplot in a procedural style
trace1 = go.Scatter()
trace1.x = [1, 2, 3]  # <1>
trace1.y = [4, 5, 6]
trace1.marker = {'color': 'red', 'symbol': 104, 'size': 10}
trace1.mode = 'markers+lines'

# import chart_studio.plotly as py
# py.iplot([trace1], filename = 'basic-line')
# py.show()
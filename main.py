import pandas as pd
import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go

app = dash.Dash()  # initialising dash app
#server=app.server


df = pd.read_csv('AID713.csv')
df.columns =['Date', 'Temp', 'Humidity', 'VPD' ,'PH' ]
print(df.head())

    #px.data.stocks()  # reading stock price dataset


def temperature():

    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Scatter(x=df['Date'], y=df['Temp'], \
                                line=dict(color='firebrick', width=4), name='Google')
                     ])
    fig.update_layout(title='Temperature over time',
                      xaxis_title='Dates',
                      yaxis_title='Temperature'
                      )
    return fig


def humidity():

    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Scatter(x=df['Date'], y=df['Humidity'], \
                                line=dict(color='firebrick', width=4), name='Google')
                     ])
    fig.update_layout(title='Humidity over time',
                      xaxis_title='Dates',
                      yaxis_title='Humidity'
                      )
    return fig

def vpd():

    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Scatter(x=df['Date'], y=df['VPD'], \
                                line=dict(color='firebrick', width=4), name='Google')
                     ])
    fig.update_layout(title='VPD ccc over time',
                      xaxis_title='Dates',
                      yaxis_title='VPD'
                      )
    return fig

def ph():

    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Bar(x=df['Date'], y=df['PH'],name='Google')
                        ])
    fig.update_layout(title='PH over time',
                      xaxis_title='Dates',
                      yaxis_title='PH'
                      )
    return fig

app.layout = html.Div(id='parent', children=[
    html.Div([
        html.H1(children='ClickFarm1 Environment Data'),

        html.Div(children='''
                Temperature over time.
            '''),

        dcc.Graph(
            id='graph1',
            figure=temperature()
        ),
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='ClickFarm1 Environment Data'),

        html.Div(children='''
                Humidity over time.
            '''),

        dcc.Graph(
            id='graph2',
            figure=humidity()
        ),
    ]),

# New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='ClickFarm1 Environment Data'),

        html.Div(children='''
                VPD over time.     Pressure Deficit, or VPD, is the difference (deficit) between the amount of moisture in the air and how much moisture the air can hold when it is saturated
            '''),

        dcc.Graph(
            id='graph3',
            figure=vpd()
        ),
    ]),
    # New Div for all elements in the new 'row' of the page])
])

if __name__ == '__main__':
    app.run_server()


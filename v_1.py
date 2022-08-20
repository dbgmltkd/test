from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import os

import pandas as pd

app = Dash(__name__)
file_path = 'C:/Users/kangh/Desktop/프로젝트/시각화/data'
file_list = os.listdir(file_path)
file_gu = []
file_meter = []
file_day = []
time_list = ['1타임','2타임','3타임','4타임','5타임']



for i in file_list:
    V= i.split("_")
    file_gu.append(V[0])
    file_day.append(V[1])
    file_meter.append(V[2])


file_gu = list(set(file_gu))
file_day = list(set(file_day))
file_meter = list(set(file_meter))


    
app.layout = html.Div(style={'backgroundColor': '#7882A4'},  children=[
    html.H1(
        children='개같은 시각화^^',
        style={
            'textAlign': 'center',
            'color': '#7FDBF'
        }
    ),
    ########################################################################################################
    html.Div(style={'backgroundColor': '#C9CCD5'}, children=[

        html.Div([
            html.Label('구 선택'),
            dcc.RadioItems(
                file_gu,
                '용산구',
                id='gu_select1'
            ),
        ], style={'width': '10%', 'display': 'inline-block', 'backgroundColor': '#E4D8DC'}),
        
        html.Div([
            html.Label('반경 선택'),
            dcc.RadioItems(
                file_meter,
                '500',
                id='meter_select1'
            ),
        ], style={'width': '10%', 'display': 'inline-block'}),

        html.Div([
            html.Label('평휴일 선택'),
            dcc.RadioItems(
                file_day,
                '평일.csv',
                id='day_select1',
            )
        ], style={'width': '10%', 'display': 'inline-block'}),
        
        html.Div([
            html.Label('행정동 선택'),
            dcc.Checklist(
                id='dong_select1'
                #multi = True
            )
        ], style={'width': '55%', 'display': 'inline-block'})
    ]),
    ########################################################################################################
    html.Div(style={'backgroundColor': '#C9CCD5'}, children=[

        html.Div([
            html.Label('구 선택'),
            dcc.RadioItems(
                file_gu,
                '용산구',
                id='gu_select2'
            ),
        ], style={'width': '10%', 'display': 'inline-block', 'backgroundColor': '#E4D8DC'}),
        
        html.Div([
            html.Label('반경 선택'),
            dcc.RadioItems(
                file_meter,
                '500',
                id='meter_select2'
            ),
        ], style={'width': '10%', 'display': 'inline-block'}),

        html.Div([
            html.Label('평휴일 선택'),
            dcc.RadioItems(
                file_day,
                '평일.csv',
                id='day_select2',
            )
        ], style={'width': '10%', 'display': 'inline-block'}),
        
        html.Div([
            html.Label('행정동 선택'),
            dcc.Checklist(
                id='dong_select2'
                #multi = True
            )
        ], style={'width': '55%', 'display': 'inline-block'})
    ]),
    ########################################################################################################
    html.Br(),
    
    html.Div([

        html.Div([
            html.Label('X값 선택'),
            dcc.Dropdown(
                id='X1_select'
                #multi = True
            ),
        ], style={'width': '20%', 'display': 'inline-block'}),
        
        html.Div([
            html.Label('Y값 선택'),
            dcc.Dropdown(
                id='Y1_select'
                #multi = True
            ),
        ], style={'width': '20%', 'display': 'inline-block'}),
        
        html.Div([
            html.Label('X값 선택'),
            dcc.Dropdown(
                id='X2_select'
                #multi = True
            ),
        ], style={'width': '20%', 'display': 'inline-block'}),
        
        html.Div([
            html.Label('Y값 선택'),
            dcc.Dropdown(
                id='Y2_select'
                #multi = True
            ),
        ], style={'width': '20%', 'display': 'inline-block'})
        
        
    ]),
    ########################################################################################################
    html.Br(),
    
    html.Div(style={'backgroundColor': '#7882A4'}, children=[
        html.Div(style={'backgroundColor': '#7882A4'}, children=[
        dcc.Graph(id='Graph1')
        ]),
        html.Div(style={'backgroundColor': '#7882A4'}, children=[
        dcc.Graph(id='Graph2')
        ])
        
    ])
       
])


@app.callback(
    Output('X1_select', 'options'),
    Output('Y1_select', 'options'),
    Output('X2_select', 'options'),
    Output('Y2_select', 'options'),
    Output('dong_select1', 'options'),
    Output('dong_select2', 'options'),
    Input('gu_select1', 'value'),
    Input('meter_select1', 'value'),
    Input('day_select1', 'value'),
    Input('gu_select2', 'value'),
    Input('meter_select2', 'value'),
    Input('day_select2', 'value')
    )
def file_select(gu1, meter1, day1,gu2, meter2, day2):
    df1 = pd.read_csv(f'{file_path}/{gu1}_{day1}_{meter1}_최종본.csv', encoding = 'CP949', parse_dates = ['단속날짜'])
    df2 = pd.read_csv(f'{file_path}/{gu2}_{day2}_{meter2}_최종본.csv', encoding = 'CP949', parse_dates = ['단속날짜'])
    column_list1 = df1.columns
    column_list2 = df2.columns
    ex_list = ['Unnamed: 0', '단속날짜', '단속타임', '장소', '단속동', '건수']
    X1_list = list(column_list1.difference(ex_list))
    X2_list = list(column_list2.difference(ex_list))
    dong_list1 = list(df1.단속동.unique())
    dong_list2 = list(df2.단속동.unique())
    
    return X1_list, X1_list, X2_list, X2_list, dong_list1, dong_list2

@app.callback(
    Output('X1_select', 'value'),
    Input('X1_select', 'options'))
def set_x_value(X1_list):
    return X1_list

@app.callback(
    Output('Y1_select', 'value'),
    Input('Y1_select', 'options'))
def set_y_value(Y1_list):
    return Y1_list

@app.callback(
    Output('X2_select', 'value'),
    Input('X2_select', 'options'))
def set_x_value(X2_list):
    return X2_list

@app.callback(
    Output('Y2_select', 'value'),
    Input('Y2_select', 'options'))
def set_y_value(Y2_list):
    return Y2_list


@app.callback(
    Output('dong_select1', 'value'),
    Input('dong_select1', 'options'))
def set_dong_value(dong_list1):
    return dong_list1

@app.callback(
    Output('dong_select2', 'value'),
    Input('dong_select2', 'options'))
def set_dong_value(dong_list2):
    return dong_list2

   
@app.callback(
    Output('Graph1', 'figure'),
    #Output("stack-table", "data"),
    Input('X1_select', 'value'),
    Input('Y1_select', 'value'),
    Input('dong_select1', 'value'),
    Input('gu_select1', 'value'),
    Input('meter_select1', 'value'),
    Input('day_select1', 'value')
    )

def update_graph1(X_value, Y_value, dong_value, gu, meter, day):
    df1 = pd.read_csv(f'{file_path}/{gu}_{day}_{meter}_최종본.csv', encoding = 'CP949', parse_dates = ['단속날짜'])
    #df2 = df1[(df1['측정일시'].dt.month<=month[1]) & (df1['측정일시'].dt.month>=month[0])]
    df1 = df1[df1.단속동.isin(dong_value)]
    fig1 = px.scatter(df1, x = f'{X_value}', y= f'{Y_value}', color = '단속타임', 
                      hover_data=['단속날짜','장소'],
                      template= 'seaborn') 


    fig1.update_layout(
        paper_bgcolor="#7882A4",
        plot_bgcolor='#EFEFEF'
        )


    return fig1

@app.callback(
    Output('Graph2', 'figure'),
    #Output("stack-table", "data"),
    Input('X2_select', 'value'),
    Input('Y2_select', 'value'),
    Input('dong_select2', 'value'),
    Input('gu_select2', 'value'),
    Input('meter_select2', 'value'),
    Input('day_select2', 'value')
    )

def update_graph1(X_value, Y_value, dong_value, gu, meter, day):
    df2 = pd.read_csv(f'{file_path}/{gu}_{day}_{meter}_최종본.csv', encoding = 'CP949', parse_dates = ['단속날짜'])
    #df2 = df1[(df1['측정일시'].dt.month<=month[1]) & (df1['측정일시'].dt.month>=month[0])]
    df2 = df2[df2.단속동.isin(dong_value)]
    fig2 = px.scatter(df2, x = f'{X_value}', y= f'{Y_value}', color = '단속타임', 
                      hover_data=['단속날짜','장소'],
                      template= 'seaborn') 


    fig2.update_layout(
        paper_bgcolor="#7882A4",
        plot_bgcolor='#EFEFEF'
        )


    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
    
    #return [{'label' : i, 'value' : i} for i in yaxis_list]
  #return available_options[0]['value']
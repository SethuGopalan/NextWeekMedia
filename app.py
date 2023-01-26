import dash
from dash import html,dcc
import dash_bootstrap_components as dbc
from turtle import Turtle


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE])

app.layout=dbc.Container(

     dbc.Row([

        html.Header(
            html.Div([

            html.H1("News Daily"),
            html.H5("______________________________________________________________________________________________________________"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H5("A magize for all the news update"),
            html.H5("______________________________________________________________________________________________________________"),
            
           
            ],style={'color': 'white',  'fontSize': 2, 'font-family': 'serif'})
            
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Col([

   
            html.Div([
                    
                    html.Br(),
                    html.Br(),
                    html.Br(),

                    html.H5("Latest News Boston")


                ],style={'color': 'white',  'fontSize': 2, 'font-family': 'serif'},),

        ], width={'size': 9, 'offset': 0}),


        dbc.Col([

            html.Div([
            html.Br(),
            html.Br(),
            html.Br(),

              html.H5("World news Today")

        ],style={'color': 'white',  'fontSize': 5, 'font-family': 'serif'},),

        ], width={'size': 9, 'offset': 0}),

        dbc.Col([

            html.Div([
            html.Br(),
            html.Br(),
            html.Br(),

              html.H5("US Today")

        ],style={'color': 'white',  'fontSize': 5, 'font-family': 'serif'},),

        ], width={'size': 9, 'offset': 0}),

        dbc.Col([

            html.Div([
            html.Br(),
            html.Br(),
            html.Br(),

              html.H5("US Sports Today")

        ],style={'color': 'white',  'fontSize': 5, 'font-family': 'serif'},),

        ], width={'size': 9, 'offset': 0}),


    
        html.H5("_____________________________________________________________________________________________________________________________________"),

       

            
          

       
           


    ]),

      

)

    

if __name__ == "__main__":
    app.run(debug=True)

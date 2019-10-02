import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='Where Should You Eat?'
tabtitle = 'Restaurants!'
list_of_meals=['Breakfast', 'Lunch', 'Dinner']
list_of_type=['Fast Casual', 'Sit Down', 'Surprise Me']
sourceurl = 'https://dash.plot.ly/getting-started-part-2'
githublink = 'https://github.com/austinlasseter/dash-callbacks-multi-input'


########## Set up the chart

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='pick-a-meal',
                options=[
                        {'label':list_of_meals[0], 'value':list_of_meals[0]},
                        {'label':list_of_meals[1], 'value':list_of_meals[1]},
                        {'label':list_of_meals[2], 'value':list_of_meals[2]},
                        ],
                value='',
                ),
        ],className='two columns'),
        html.Div([
            dcc.RadioItems(
                id='pick-a-type',
                options=[
                        {'label':list_of_type[0], 'value':list_of_type[0]},
                        {'label':list_of_type[1], 'value':list_of_type[1]},
                        {'label':list_of_type[2], 'value':list_of_type[2]},
                        ],
                value='',
                ),
        ],className='ten columns'),
        ], className = 'twelve columns'),
    html.Br(),
    html.Div([
        html.Div([
            html.H6('How hungry are you?'),
            dcc.Slider(
                id='hunger_level',
                min = 1,
                max = 3,
                step = 1,
                marks={i:str(i) for i in range(1, 4)},
                value  = 4,
                ),
        ],className='four columns'),
        ], className = 'twelve columns'),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div(id='your_output_here', children=''),
    ], className = 'twelve columns'),
    html.Br(),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ],
            style={'textAlign':'left',
                'fontColor':'#0800a8',
                'backgroundColor':'#fff5f8',}
)

########## Define Callback

@app.callback(Output('your_output_here', 'children'),
              [Input('pick-a-meal', 'value'),
               Input('pick-a-type', 'value'),
               Input('hunger_level', 'value')])
def radio_results(meal_you_picked, type_you_picked, hunger_level):
    if meal_you_picked in  ('Breakfast', 'Lunch', 'Dinner'):
        if type_you_picked == '':
            image_you_chose = f'{meal_you_picked.lower()}.jpg'
            message = 'Please select a meal type.'
            return html.Br(), message, html.Br() , html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': 'auto'}), html.Br(), html.Br()
        else:
            if hunger_level > 2:
                image_you_chose=f'{meal_you_picked}-{type_you_picked}-A.jpg'
                list_of_restaurants= {'Breakfast': {'Fast Casual': "Call Your Mother Deli", 'Sit Down': "Ted's Bulliten", 'Surprise Me':'Unconventional Diner'},
                              'Lunch': {'Fast Casual': "Bub & Pops", 'Sit Down': "Texas de Brazil", 'Surprise Me':'Florida Ave Grill'},
                              'Dinner': {'Fast Casual': "Chipotle", 'Sit Down': "Thai X-ing", 'Surprise Me':'Al Volo'}}
                message = f'You should eat at {list_of_restaurants[meal_you_picked][type_you_picked]}!'
                return html.Br(), message, html.Br() , html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': 'auto'}),html.Br(),html.Br()
            elif hunger_level > 1 and hunger_level <= 2:
                image_you_chose=f'{meal_you_picked}-{type_you_picked}-B.jpg'
                list_of_restaurants= {'Breakfast': {'Fast Casual': "Dolcezza", 'Sit Down': "Commissary", 'Surprise Me':'Busboys and Poets'},
                              'Lunch': {'Fast Casual': "Taco Bell", 'Sit Down': "Logan Tavern", 'Surprise Me':'Slipstream'},
                              'Dinner': {'Fast Casual': "Cava", 'Sit Down': "Surfside", 'Surprise Me':'Maydan'}}
                message = f'You should eat at {list_of_restaurants[meal_you_picked][type_you_picked]}!'
                return html.Br(), message, html.Br() , html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': 'auto'}),html.Br(),html.Br()
            elif hunger_level > 0 and hunger_level <= 1:
                image_you_chose=f'{meal_you_picked}-{type_you_picked}-C.jpg'
                list_of_restaurants= {'Breakfast': {'Fast Casual': "Fruitive", 'Sit Down': "A Baked Joint", 'Surprise Me':'Bluestone Lane'},
                              'Lunch': {'Fast Casual': "Sweetgreen", 'Sit Down': "Emmissary", 'Surprise Me':'Thip Khao'},
                              'Dinner': {'Fast Casual': "Hip City Veg", 'Sit Down': "Matchbox", 'Surprise Me':'Taqueria Nacional'}}
                message = f'You should eat at {list_of_restaurants[meal_you_picked][type_you_picked]}!'
                return html.Br(), message ,html.Br() , html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': 'auto'}),html.Br()
    else:
        return 'Please select a meal.'



if __name__ == '__main__':
    app.run_server()

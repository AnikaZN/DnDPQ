# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# @app.callback(Output('prediction-content', 'children'),
#              [Input('film', 'value'),
#               Input('year', 'value'),
#               Input('body_count', 'value'),
#               Input('length_minutes', 'value'),
#               Input('mpaa_rating', 'value'),
#               Input('genre', 'value')])
# def predict():
#     prediction =
#     return f'You are a {prediction}!'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions

            Answer the questions below, then scroll back up to the top to find out your D&D Player Personality!

            """
        ),
        html.H2('D&D Player Personality', className='mb-5'),
        # html.Div(id='prediction-content', className='lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Question 1: '),
        dcc.RadioItems(
            id='one',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 2: '),
        dcc.RadioItems(
            id='two',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 3: '),
        dcc.RadioItems(
            id='three',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 4: '),
        dcc.RadioItems(
            id='four',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 5: '),
        dcc.RadioItems(
            id='five',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 6: '),
        dcc.RadioItems(
            id='six',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 7: '),
        dcc.RadioItems(
            id='seven',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 8: '),
        dcc.RadioItems(
            id='eight',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 9: '),
        dcc.RadioItems(
            id='nine',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 10: '),
        dcc.RadioItems(
            id='ten',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 11: '),
        dcc.RadioItems(
            id='eleven',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 12: '),
        dcc.RadioItems(
            id='twelve',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 13: '),
        dcc.RadioItems(
            id='thirteen',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 14: '),
        dcc.RadioItems(
            id='fourteen',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 15: '),
        dcc.RadioItems(
            id='fifteen',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 16: '),
        dcc.RadioItems(
            id='sixteen',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 17: '),
        dcc.RadioItems(
            id='seventeen',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 18: '),
        dcc.RadioItems(
            id='eighteen',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 19: '),
        dcc.RadioItems(
            id='nineteen',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 20: '),
        dcc.RadioItems(
            id='twenty',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 21: '),
        dcc.RadioItems(
            id='twenty-one',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 22: '),
        dcc.RadioItems(
            id='twenty-two',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 23: '),
        dcc.RadioItems(
            id='twenty-three',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 24: '),
        dcc.RadioItems(
            id='twenty-four',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 25: '),
        dcc.RadioItems(
            id='twenty-five',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 26: '),
        dcc.RadioItems(
            id='twenty-six',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 27: '),
        dcc.RadioItems(
            id='twenty-seven',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 28: '),
        dcc.RadioItems(
            id='twenty-eight',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 29: '),
        dcc.RadioItems(
            id='twenty-nine',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 30: '),
        dcc.RadioItems(
            id='thirty',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 31: '),
        dcc.RadioItems(
            id='thirty-one',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 32: '),
        dcc.RadioItems(
            id='thirty-two',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 33: '),
        dcc.RadioItems(
            id='thirty-three',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 34: '),
        dcc.RadioItems(
            id='thirty-four',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 35: '),
        dcc.RadioItems(
            id='thirty-five',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 36: '),
        dcc.RadioItems(
            id='thirty-six',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 37: '),
        dcc.RadioItems(
            id='thirty-seven',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 38: '),
        dcc.RadioItems(
            id='thirty-eight',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 39: '),
        dcc.RadioItems(
            id='thirty-nine',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 40: '),
        dcc.RadioItems(
            id='forty',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 41: '),
        dcc.RadioItems(
            id='forty-one',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 42: '),
        dcc.RadioItems(
            id='forty-two',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 43: '),
        dcc.RadioItems(
            id='forty-three',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 44: '),
        dcc.RadioItems(
            id='forty-four',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 45: '),
        dcc.RadioItems(
            id='forty-five',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 46: '),
        dcc.RadioItems(
            id='forty-six',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 47: '),
        dcc.RadioItems(
            id='forty-seven',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 48: '),
        dcc.RadioItems(
            id='forty-eight',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 49: '),
        dcc.RadioItems(
            id='forty-nine',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 50: '),
        dcc.RadioItems(
            id='fifty',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 51: '),
        dcc.RadioItems(
            id='fifty-one',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 52: '),
        dcc.RadioItems(
            id='fifty-two',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 53: '),
        dcc.RadioItems(
            id='fifty-three',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 54: '),
        dcc.RadioItems(
            id='fifty-four',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 55: '),
        dcc.RadioItems(
            id='fifty-five',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 56: '),
        dcc.RadioItems(
            id='fifty-six',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 57: '),
        dcc.RadioItems(
            id='fifty-seven',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 58: '),
        dcc.RadioItems(
            id='fifty-eight',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 59: '),
        dcc.RadioItems(
            id='fifty-nine',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
        dcc.Markdown('#### Question 60: '),
        dcc.RadioItems(
            id='sixty',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
            ],
            value='MTL'
        ),
    ],
)

layout = dbc.Row([column1, column2])

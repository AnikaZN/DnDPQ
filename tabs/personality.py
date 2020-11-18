# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# @app.callback(Output("prediction-content", "children"),
#              [Input("film", "value"),
#               Input("year", "value"),
#               Input("body_count", "value"),
#               Input("length_minutes", "value"),
#               Input("mpaa_rating", "value"),
#               Input("genre", "value")])
# def predict():
#     prediction =
#     return f"You are a {prediction}!"

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Personality Test

            Answer the questions below, then scroll back up to the top to find out your D&D Player Personality!

            """
        ),
        html.H2("D&D Player Personality", className="mb-5"),
        # html.Div(id="prediction-content", className="lead")
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown("## Questions", className="mb-5"),
        dcc.Markdown("#### Question 1: I prefer..."),
        dcc.RadioItems(
            id="one",
            options=[
                {"label": "Opportunities to develop my character's personality and background.", "value": "acting"},
                {"label": "Having steady access to new abilities and spells.", "value": "optimizing"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 2: I prefer..."),
        dcc.RadioItems(
            id="two",
            options=[
                {"label": "Unexpected combat encounters.", "value": "fighting"},
                {"label": "When my character's background helps shape the story of the campaign.", "value": "storytelling"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 3: I prefer..."),
        dcc.RadioItems(
            id="three",
            options=[
                {"label": "Vivid descriptions of the havoc my character is wreaking in combat.", "value": "fighting"},
                {"label": "When magic items I want are rewards for adventuring.", "value": "optimizing"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 4: I prefer..."),
        dcc.RadioItems(
            id="four",
            options=[
                {"label": "Encounters that let my character shine.", "value": "optimizing"},
                {"label": "Encounters that advance the story in some way.", "value": "storytelling"},
            ],
            value="optimizing"
        ),
        dcc.Markdown("#### Question 5: I prefer..."),
        dcc.RadioItems(
            id="five",
            options=[
                {"label": "Combat encounters with large numbers of weak monsters.", "value": "fighting"},
                {"label": "Encounters that emphasize problem-solving.", "value": "problem solving"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 6: I prefer..."),
        dcc.RadioItems(
            id="six",
            options=[
                {"label": "New York City", "value": "optimizing"},
                {"label": "Montréal", "value": "problem solving"},
            ],
            value="optimizing"
        ),
        dcc.Markdown("#### Question 7: I prefer..."),
        dcc.RadioItems(
            id="seven",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "fighting"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 8: I prefer..."),
        dcc.RadioItems(
            id="eight",
            options=[
                {"label": "New York City", "value": "acting"},
                {"label": "Montréal", "value": "exploring"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 9: I prefer..."),
        dcc.RadioItems(
            id="nine",
            options=[
                {"label": "New York City", "value": "acting"},
                {"label": "Montréal", "value": "optimizing"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 10: I prefer..."),
        dcc.RadioItems(
            id="ten",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "fighting"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 11: I prefer..."),
        dcc.RadioItems(
            id="eleven",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "optimizing"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 12: I prefer..."),
        dcc.RadioItems(
            id="twelve",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "problem solving"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 13: I prefer..."),
        dcc.RadioItems(
            id="thirteen",
            options=[
                {"label": "New York City", "value": "exploring"},
                {"label": "Montréal", "value": "storytelling"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 14: I prefer..."),
        dcc.RadioItems(
            id="fourteen",
            options=[
                {"label": "New York City", "value": "fighting"},
                {"label": "Montréal", "value": "problem solving"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 15: I prefer..."),
        dcc.RadioItems(
            id="fifteen",
            options=[
                {"label": "New York City", "value": "exploring"},
                {"label": "Montréal", "value": "fighting"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 16: I prefer..."),
        dcc.RadioItems(
            id="sixteen",
            options=[
                {"label": "New York City", "value": "acting"},
                {"label": "Montréal", "value": "exploring"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 17: I prefer..."),
        dcc.RadioItems(
            id="seventeen",
            options=[
                {"label": "New York City", "value": "fighting"},
                {"label": "Montréal", "value": "storytelling"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 18: I prefer..."),
        dcc.RadioItems(
            id="eighteen",
            options=[
                {"label": "New York City", "value": "problem solving"},
                {"label": "Montréal", "value": "storytelling"},
            ],
            value="problem solving"
        ),
        dcc.Markdown("#### Question 19: I prefer..."),
        dcc.RadioItems(
            id="nineteen",
            options=[
                {"label": "New York City", "value": "acting"},
                {"label": "Montréal", "value": "instigating"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 20: I prefer..."),
        dcc.RadioItems(
            id="twenty",
            options=[
                {"label": "New York City", "value": "exploring"},
                {"label": "Montréal", "value": "storytelling"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 21: I prefer..."),
        dcc.RadioItems(
            id="twenty-one",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "optimizing"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 22: I prefer..."),
        dcc.RadioItems(
            id="twenty-two",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "problem solving"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 23: I prefer..."),
        dcc.RadioItems(
            id="twenty-three",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "fighting"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 24: I prefer..."),
        dcc.RadioItems(
            id="twenty-four",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "storytelling"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 25: I prefer..."),
        dcc.RadioItems(
            id="twenty-five",
            options=[
                {"label": "New York City", "value": "fighting"},
                {"label": "Montréal", "value": "storytelling"},
            ],
            value="fighting"
        ),
        dcc.Markdown("#### Question 26: I prefer..."),
        dcc.RadioItems(
            id="twenty-six",
            options=[
                {"label": "New York City", "value": "acting"},
                {"label": "Montréal", "value": "problem solving"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 27: I prefer..."),
        dcc.RadioItems(
            id="twenty-seven",
            options=[
                {"label": "New York City", "value": "acting"},
                {"label": "Montréal", "value": "storytelling"},
            ],
            value="acting"
        ),
        dcc.Markdown("#### Question 28: I prefer..."),
        dcc.RadioItems(
            id="twenty-eight",
            options=[
                {"label": "New York City", "value": "exploring"},
                {"label": "Montréal", "value": "optimizing"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 29: I prefer..."),
        dcc.RadioItems(
            id="twenty-nine",
            options=[
                {"label": "New York City", "value": "instigating"},
                {"label": "Montréal", "value": "optimizing"},
            ],
            value="instigating"
        ),
        dcc.Markdown("#### Question 30: I prefer..."),
        dcc.RadioItems(
            id="thirty",
            options=[
                {"label": "New York City", "value": "exploring"},
                {"label": "Montréal", "value": "fighting"},
            ],
            value="exploring"
        ),
        dcc.Markdown("#### Question 31: I prefer..."),
        dcc.RadioItems(
            id="thirty-one",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 32: I prefer..."),
        dcc.RadioItems(
            id="thirty-two",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 33: I prefer..."),
        dcc.RadioItems(
            id="thirty-three",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 34: I prefer..."),
        dcc.RadioItems(
            id="thirty-four",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 35: I prefer..."),
        dcc.RadioItems(
            id="thirty-five",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 36: I prefer..."),
        dcc.RadioItems(
            id="thirty-six",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 37: I prefer..."),
        dcc.RadioItems(
            id="thirty-seven",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 38: I prefer..."),
        dcc.RadioItems(
            id="thirty-eight",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 39: I prefer..."),
        dcc.RadioItems(
            id="thirty-nine",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 40: I prefer..."),
        dcc.RadioItems(
            id="forty",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 41: I prefer..."),
        dcc.RadioItems(
            id="forty-one",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 42: I prefer..."),
        dcc.RadioItems(
            id="forty-two",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 43: I prefer..."),
        dcc.RadioItems(
            id="forty-three",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 44: I prefer..."),
        dcc.RadioItems(
            id="forty-four",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 45: I prefer..."),
        dcc.RadioItems(
            id="forty-five",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 46: I prefer..."),
        dcc.RadioItems(
            id="forty-six",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 47: I prefer..."),
        dcc.RadioItems(
            id="forty-seven",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 48: I prefer..."),
        dcc.RadioItems(
            id="forty-eight",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 49: I prefer..."),
        dcc.RadioItems(
            id="forty-nine",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 50: I prefer..."),
        dcc.RadioItems(
            id="fifty",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 51: I prefer..."),
        dcc.RadioItems(
            id="fifty-one",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 52: I prefer..."),
        dcc.RadioItems(
            id="fifty-two",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 53: I prefer..."),
        dcc.RadioItems(
            id="fifty-three",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 54: I prefer..."),
        dcc.RadioItems(
            id="fifty-four",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 55: I prefer..."),
        dcc.RadioItems(
            id="fifty-five",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 56: I prefer..."),
        dcc.RadioItems(
            id="fifty-six",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 57: I prefer..."),
        dcc.RadioItems(
            id="fifty-seven",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 58: I prefer..."),
        dcc.RadioItems(
            id="fifty-eight",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 59: I prefer..."),
        dcc.RadioItems(
            id="fifty-nine",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
        dcc.Markdown("#### Question 60: I prefer..."),
        dcc.RadioItems(
            id="sixty",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
            ],
            value="MTL"
        ),
    ],
)

layout = dbc.Row([column1, column2])

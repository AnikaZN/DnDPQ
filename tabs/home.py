from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro
Greetings!
This web app allows you to determine your unique RPG player style!

More information on the different types is in the "Types" tab - I recommend visiting that tab *after* you finish the quiz!

Have fun!
""")]

# html.Img(src='/assets/dice-unsplash.jpg', style={'width':'100%'})]

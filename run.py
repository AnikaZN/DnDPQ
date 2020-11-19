from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import quiz, home, types

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# Your RPG Player Personality'),
    dcc.Tabs(id='tabs', value='tab-home', children=[
        dcc.Tab(label='Home', value='tab-home'),
        dcc.Tab(label='Quiz', value='tab-quiz'),
        dcc.Tab(label='Types', value='tab-types'),
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-home': return home.layout
    if tab == 'tab-quiz': return quiz.layout
    if tab == 'tab-types': return types.layout

if __name__ == '__main__':
    app.run_server(debug=True)

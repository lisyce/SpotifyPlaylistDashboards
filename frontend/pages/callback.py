import dash
from dash import html

dash.register_page(__name__, path='/callback')

layout = html.Div([
    html.H1('This is our Callback page'),
])
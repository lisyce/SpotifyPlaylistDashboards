import requests
from dash import html, Input, Output, State, callback, register_page

register_page(__name__, path='/')

layout = html.Div([
    html.H1('This is our Home page'),
    html.Button('Authorize', id='authorize-btn')
])


@callback(
    Input('authorize-btn', 'n_clicks'),
    prevent_initial_call=True
)
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )
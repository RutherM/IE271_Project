import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H4('Sampling Assitant', style={'fontWeight': 'bold'})
                    ]
                ),
                dbc.CardBody(
                    [
                        html.Hr(),
                        html.Div(
                            "This Sampling Assistant app was developed as a requirement for IE 271 as a guide for field samplers.", 
                            id='output_container',
                            style={'border': '2px dashed #777', 'border-radius': '5px',
                                   'padding': '1em'},
                            className='text-center'
                        ),
                    ]
                ),
            ],
            className='card text-white bg-dark mb-3'
        )
    ],
    style={
        'position': 'fixed',
        'top': '50%',
        'left': '50%',
        'transform': 'translate(-50%, -50%)',
        'width': '40%'
    }
)
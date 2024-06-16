import dash
from dash import dcc
from dash import html
from dash import callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pages.functions as functions

containers = functions.get_containers()[['code']]

dash.register_page(__name__)

layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H4('Sampling Assitant - Add Container', style={'fontWeight': 'bold'})
                    ]
                ),
                dbc.CardBody(
                    [
                        # Input
                        dbc.Row(
                            [
                                dbc.Label("Serial Number", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="serial", placeholder="input please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),                             
                        dbc.Row(
                            [
                                dbc.Label("Container Code", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="code", placeholder="inputs please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                                html.H6(
                                    " ", 
                                    id='code_container'
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Volume (ml)", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="volume", placeholder="inputs please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Material", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="material", placeholder="inputs please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        html.Br(),
                        html.Div(
                            dbc.Button("Submit", color="info", className="me-1", id='confirm_process'),
                            className='d-grid gap-2'
                        ), 
                        html.Hr(),
                        html.Div(
                            "No process yet", 
                            id='output_container_ac',
                            style={'border': '2px dashed #777', 'border-radius': '5px',
                                   'padding': '1em'},
                            className='text-center'
                        ),
                        html.Br(),
                        dcc.Location(id='url', refresh=False),
                        html.Div(id='page-content_ac'),
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

@callback(
    [   Output('code_container', 'children')
    ],
    [   Input('code','value')
    ]
)

def check_code(co):
    try:
        if containers['code'].tolist().index(co) >= 0:
            output_text = "Code Already Exist"
    except:
        output_text = " "
    return [output_text];

@callback(
    [   Output('output_container_ac', 'children')
    ],
    [   Input('confirm_process', 'n_clicks'),
    ],
    [   State('serial', 'value'),
        State('code', 'value'),
        State('volume', 'value'),
        State('material','value')
    ]
)

def run_process(btnclick,  se, co, vo, ma):
    try:
        if btnclick <= 1:
            try: 
                functions.add_containers(se, co, vo, ma)
                output_text = "Data Submitted"                
            except:
                output_text = "Container Code already exist. Use a different container code."
        else:
            output_text = "Click refresh page"
    except: 
        output_text = "Not Processed Yet"
    return [output_text];

@callback(
    Output('page-content_ac', 'children'),
    [Input('url', 'pathname')])

def display_page(relative_pathname):
    return html.Div([html.A(html.Button('Refresh Page'),href=relative_pathname)])

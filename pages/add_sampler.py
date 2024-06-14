import dash
from dash import dcc
from dash import html
from dash import callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import pages.functions as functions

samplers = functions.get_samplers()[['id']]

dash.register_page(__name__)

layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H4('Sampling Assitant - Add Sampler', style={'fontWeight': 'bold'})
                    ]
                ),
                dbc.CardBody(
                    [
                        # Input
                        dbc.Row(
                            [
                                dbc.Label("Sampler ID", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="id", placeholder="input please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                                html.H6(
                                    " ", 
                                    id='id_container'
                                ),
                            ],
                            className="mb-3",
                        ),                             
                         dbc.Row(
                            [
                                dbc.Label("Sampler Name", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="name", placeholder="inputs please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Gender", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="gender", placeholder="Male/Female",
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Birthdate", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="bdate", placeholder="MM/DD/YYYY",
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Address", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="address", placeholder="input please!",
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
                            id='output_container_as',
                            style={'border': '2px dashed #777', 'border-radius': '5px',
                                   'padding': '1em'},
                            className='text-center'
                        ),
                        html.Br(),
                        dcc.Location(id='url', refresh=False),
                        html.Div(id='page-content_as'),
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
    [   Output('id_container', 'children')
    ],
    [   Input('id','value')
    ]
)

def check_ID(si):
    try:
        if samplers['id'].tolist().index(si) >= 0:
            output_text = "Sampler ID Already Exist"
    except:
        output_text = " "
    return [output_text];

@callback(
    [   Output('output_container_as', 'children')
    ],
    [   Input('confirm_process', 'n_clicks'),
    ],
    [   State('id','value'),
        State('name', 'value'),
        State('gender', 'value'),
        State('bdate', 'value'),
        State('address', 'value'),
    ]
)

def run_process(btnclick, si, sn, sg, sb, sa):
    try:
        if btnclick <= 1:
            try:
                if samplers['id'].tolist().index(si) >= 0:
                    output_text = "Sampler ID already exist"
                else:
                    functions.add_samplers(si, sn, sg, sb, sa)
                    output_text = "Data Submitted"
            except:
                functions.add_samplers(si, sn, sg, sb, sa)
                output_text = "Data Submitted"                
        else:
            output_text = "Click refresh page"
    except: 
        output_text = "Not Processed Yet"
    return [output_text];

@callback(
    Output('page-content_as', 'children'),
    [Input('url', 'pathname')])

def display_page(relative_pathname):
    return html.Div([html.A(html.Button('Refresh Page'),href=relative_pathname)])

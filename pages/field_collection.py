import dash
from dash import dcc
from dash import html
from dash import callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import pages.functions as functions

methods = functions.get_methods()[['name','procedure']]
samplers = functions.get_samplers()[['id','name']]
containers = functions.get_containers()[['code']]

try:
    ex_data = functions.get_data().iloc[0]
except:
    si = 'Select from dropdown'
    cc = 'Select from dropdown'
    tc = 'tray-001'
    mp = 'Select from dropdown'
    rv = '0.00'
    co = 'latitude, longitude'
    ad = 'House no., street name, City, Province'
    sa = 'Example: Grab sampling at faucet during a sunny day'
    functions.add_collected_data(si, cc, tc, mp, rv, co, ad, sa) 
    ex_data = functions.get_data().iloc[0]

dash.register_page(__name__)

layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H4('Sampling Assitant - Sample Collection', style={'fontWeight': 'bold'})
                    ]
                ),
                dbc.CardBody(
                    [
                        # Input
                        dbc.Row(
                            [
                                dbc.Label("Sampler ID", width=3),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id='sampler_id',
                                        searchable=True,
                                        options = samplers['id'].tolist(),
                                        style={'color': 'black'}
                                    ),
                                    width=5,
                                ),
                                html.H6(
                                    " ", 
                                    id='sn_container'
                                ),                                
                            ],
                            className="mb-3",
                        ), 
                        dbc.Row(
                            [
                                dbc.Label("Container code", width=3),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id='container_code',
                                        searchable=True,
                                        options = containers['code'].tolist(),
                                        style={'color': 'black'}
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ), 
                        dbc.Row(
                            [
                                dbc.Label("Tray code", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="tray_code", placeholder=ex_data['tray_code'],
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),                               
                        dbc.Row(
                            [
                                dbc.Label("Parameter", width=3),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id='param',
                                        searchable=True,
                                        options = methods['name'].tolist(),
                                        style={'color': 'black'}
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),              
                        dbc.Row(
                            [
                                dbc.Label("Input Value", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="input_value", placeholder="inputs please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Coordinates", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="coordinates", placeholder=ex_data['coordinates'],
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
                                        type="text", id="address", placeholder=ex_data["address"],
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Sampling Description", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="sampling_desc", placeholder=ex_data["sampling_desc"],
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
                            id='output_container_sc',
                            style={'border': '2px dashed #777', 'border-radius': '5px',
                                   'padding': '1em'},
                            className='text-center'
                        ),
                        html.Br(),
                        dcc.Location(id='url', refresh=False),
                        html.Div(id='page-content_sc'),
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
    [   Output('sn_container', 'children')
    ],
    [   Input('sampler_id','value')
    ]
)

def check_name(si):
    try:
        output = samplers['name'][(samplers['id'].tolist().index(si))]
    except:
        output = " "
    return [output];

@callback(
    [   Output('output_container_sc', 'children')
    ],
    [   Input('confirm_process', 'n_clicks'),
        Input('param','value'),
    ],
    [   State('sampler_id', 'value'),
        State('container_code', 'value'),
        State('tray_code', 'value'),
        State('input_value', 'value'),
        State('coordinates', 'value'),
        State('address', 'value'),
        State('sampling_desc', 'value'),
    ]
)

def run_process(btnclick, dp, si, cc, tc, iv, co, ad, sa):
    try:
        if btnclick <= 1:
            try:
                functions.add_collected_data(si, cc, tc, dp, iv, co, ad, sa)
                output_text = "Data Submitted"
            except:
                output_text = "Container code already has data."
        else:
            output_text = "Click refresh page"
    except:
        output_text = methods[methods['name']==str(dp)]['procedure']
    return [output_text];

@callback(
    Output('page-content_sc', 'children'),
    [Input('url', 'pathname')])
def display_page(relative_pathname):
    return html.Div([html.A(html.Button('Refresh Page'),href=relative_pathname)])

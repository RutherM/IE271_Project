import dash
from dash import dcc
from dash import html
from dash import callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pages.functions as functions

receiving = functions.get_receiving()[['sample_code']]
data = functions.get_data()[['container_code']]

dash.register_page(__name__)

layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H4('Sampling Assitant - Sample Receiving', style={'fontWeight': 'bold'})
                    ]
                ),
                dbc.CardBody(
                    [
                        # Input
                        dbc.Row(
                            [
                                dbc.Label("Container Code", width=3),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id='container_code',
                                        searchable=True,
                                        options = data['container_code'].tolist(),
                                        style={'color': 'black'}
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),                             
                        dbc.Row(
                            [
                                dbc.Label("Sample Code", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="sample_code", placeholder="inputs please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                                html.H6(
                                    " ", 
                                    id='sample_code_container'
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Description", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="description", placeholder="input please!",
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
                            id='output_container_sr',
                            style={'border': '2px dashed #777', 'border-radius': '5px',
                                   'padding': '1em'},
                            className='text-center'
                        ),
                        html.Br(),
                        dcc.Location(id='url', refresh=False),
                        html.Div(id='page-content_sr'),
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
    [   Output('sample_code_container', 'children')
    ],
    [   Input('sample_code','value')
    ]
)

def check_ID(sc):
    try:
        if receiving['sample_code'].tolist().index(sc) >= 0:
            output_text = "Sample Code Already Exist"
    except:
        output_text = " "
    return [output_text];

@callback(
    [   Output('output_container_sr', 'children')
    ],
    [   Input('confirm_process', 'n_clicks'),
    ],
    [   State('container_code', 'value'),
        State('sample_code', 'value'),
        State('description', 'value')
    ]
)

def run_process(btnclick,  cc, sc, de):
    try:
        if btnclick <= 1:
            try: 
                if receiving['sample_code'].tolist().index(sc) >= 0:
                    output_text = "Sample code already exist"
                else:
                    functions.add_receiving(cc, sc, de)
                    output_text = "Data Submitted"
            except:
                functions.add_receiving(cc, sc, de)
                output_text = "Data Submitted"                
        else:
            output_text = "Click refresh page"
    except: 
        output_text = "Not Processed Yet"
    return [output_text];

@callback(
    Output('page-content_sr', 'children'),
    [Input('url', 'pathname')])

def display_page(relative_pathname):
    return html.Div([html.A(html.Button('Refresh Page'),href=relative_pathname)])
import dash
from dash import dcc
from dash import html
from dash import callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pages.functions as functions

methods = functions.get_methods()[['name']]

dash.register_page(__name__)

layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H4('Sampling Assitant - Add Method', style={'fontWeight': 'bold'})
                    ]
                ),
                dbc.CardBody(
                    [
                        # Input
                        dbc.Row(
                            [
                                dbc.Label("Method Name", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="name", placeholder="input please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                                html.H6(
                                    " ", 
                                    id='name_container'
                                ),
                            ],
                            className="mb-3",
                        ),                             
                         dbc.Row(
                            [
                                dbc.Label("Procedure", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="procedure", placeholder="inputs please!",
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
                            id='output_container_am',
                            style={'border': '2px dashed #777', 'border-radius': '5px',
                                   'padding': '1em'},
                            className='text-center'
                        ),
                        html.Br(),
                        dcc.Location(id='url', refresh=False),
                        html.Div(id='page-content_am'),
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
    [   Output('name_container', 'children')
    ],
    [   Input('name','value')
    ]
)

def check_ID(mn):
    try:
        if methods['name'].tolist().index(mn) >= 0:
            output_text = "Method Name Already Exist"
    except:
        output_text = " "
    return [output_text];

@callback(
    [   Output('output_container_am', 'children')
    ],
    [   Input('confirm_process', 'n_clicks'),
    ],
    [   State('name', 'value'),
        State('procedure', 'value')
    ]
)

def run_process(btnclick,  mn, mp):
    try:
        if btnclick <= 1:
            try: 
                if methods['name'].tolist().index(mn) >= 0:
                    output_text = "Method Name already exist"
                else:
                    functions.add_methods(mn, mp)
                    output_text = "Data Submitted"
            except:
                functions.add_methods(mn, mp)
                output_text = "Data Submitted"                
        else:
            output_text = "Click refresh page"
    except: 
        output_text = "Not Processed Yet"
    return [output_text];

@callback(
    Output('page-content_am', 'children'),
    [Input('url', 'pathname')])

def display_page(relative_pathname):
    return html.Div([html.A(html.Button('Refresh Page'),href=relative_pathname)])

import dash
from dash import dcc
from dash import html
from dash import callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pages.functions as functions

container = functions.get_containers()[['code','date_prepared']]
data = functions.get_data()[['container_code','address','sampling_desc','date_collected']]
receiving = functions.get_receiving()[['container_code','sample_code','date_received']]

dash.register_page(__name__)

layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H4('Sampling Assitant - Calculation', style={'fontWeight': 'bold'})
                    ]
                ),
                dbc.CardBody(
                    [
                        # Input
                        dbc.Row(
                            [
                                dbc.Label("Sample Code", width=3),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id='sample_code',
                                        searchable=True,
                                        options = receiving['sample_code'].tolist(),
                                        style={'color': 'black'}
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
                                        options = ['Calculate sampling to receiving time', 
                                                   'Show sampling description',
                                                   'Show sampling address',
                                                   'Show date of collection',
                                                   'Show container code'],
                                        style={'color': 'black'}
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
                            id='output_container_calc',
                            style={'border': '2px dashed #777', 'border-radius': '5px',
                                   'padding': '1em'},
                            className='text-center'
                        ),
                        html.Br(),
                        dcc.Location(id='url', refresh=False),
                        html.Div(id='page-content_calc'),
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
    [   Output('output_container_calc', 'children')
    ],
    [   Input('confirm_process', 'n_clicks'),
    ],
    [   State('sample_code', 'value'),
        State('param', 'value'),
    ]
)

def run_process(btnclick,  sc, param):
    try:
        sc_index = receiving['sample_code'].tolist().index(sc)
        cc = receiving['container_code'].tolist()[sc_index]
        cc_index = data['container_code'].tolist().index(cc)

        if param == 'Calculate sampling to receiving time':
            time = receiving['date_received'][sc_index] - data['date_collected'][cc_index]
            output_text = "Elapsed time from collection to receiving in the laboratory is " + str(time)
        elif param == 'Show sampling description':
            output_text = str(data['sampling_desc'][cc_index])
        elif param == 'Show sampling address':
            output_text = str(data['address'][cc_index])
        elif param == 'Show date of collection':
            output_text = str(data['date_collected'][cc_index])
        elif param == 'Show container code':
            output_text = str(data['container_code'][cc_index])
        else:
            output_text = "Not Processed Yet"

    except: 
        output_text = "Not Processed Yet"
    return [output_text];

@callback(
    Output('page-content_calc', 'children'),
    [Input('url', 'pathname')])

def display_page(relative_pathname):
    return html.Div([html.A(html.Button('Refresh Page'),href=relative_pathname)])
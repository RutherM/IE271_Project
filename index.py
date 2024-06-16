import dash
import dash_bootstrap_components as dbc
import webbrowser
from app import app

navbar = dbc.NavbarSimple(
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
        ],
    ),
    brand="The Sampling Assistant",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True,
)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/')
    app.run_server(debug=False)
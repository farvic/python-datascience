from dash import dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

# Create the app and set the stylesheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc.icons.BOOTSTRAP, {
    "href": "https://fonts.googleapis.com/css2?family=Roboto&display=swap",
    "rel": "stylesheet"
}, {
    "media": "(max-width: 536px)",
    "href": "assets/mobile.css",
}], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
])


# Define the list of images
images = ['https://via.placeholder.com/300x200.png?text=Image+1',
          'https://via.placeholder.com/300x200.png?text=Image+2',
          'https://via.placeholder.com/300x200.png?text=Image+3']

navbar = dbc.Navbar(
    [
        dbc.NavbarBrand("My Portfolio", href="/"),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("About", href="#about-section")),
                dbc.NavItem(dbc.NavLink("Projects", href="#projects-section")),
                dbc.NavItem(dbc.NavLink("Contactz", href="#contact-section")),
            ],
            className="ml-auto",
            navbar=True,
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
    ],
    color="dark",
    dark=True,
    sticky="top",
)


# Define the placeholder dashboard section
dashboard = dbc.Container(
    [

        html.H2("Placeholder Dashboard",
                className="text-info mb-4", id="projects-section", style={"size": "12", "offset": "0"},),
        dcc.Graph(
            figure=px.scatter(
                x=[1, 2, 3], y=[1, 2, 3], title="Placeholder Graph"),
            id="dashboard",
        ),
    ],

    # className="mt-4",
)


def new_card(title, description, screenshot_urls, technology_icons):

    return dbc.Card(
        [
            dbc.CardImg(
                src="https://via.placeholder.com/300x200.png?text=Image+1", top=True),
            dbc.CardBody(
                [
                    html.H4(title, className="card-title"),
                    html.P(
                        description,
                        className="card-text",
                    ),
                    dbc.Button("Go somewhere", color="primary",
                               className="mr-1"),
                    html.Div(
                        className="project-technologies",
                        children=[
                            html.Img(
                                src=icon, className="project-technology-icon", style={"margin": "2px"}) for icon in technology_icons
                        ],

                        style={"margin-top": "20px",
                               "margin-bottom": "-10px", "align": "space-between"},
                    ),
                ]
            ),
        ],
        style={"width": "18rem"},
        className="mb-4",
    )


left_jumbotron = dbc.Col(
    html.Div(
        [
            html.H2("Change the background", className="display-3"),
            html.Hr(className="my-2"),
            html.P(
                "Swap the background-color utility and add a `.text-*` color "
                "utility to mix up the look."
            ),
            dbc.Button("Example Button", color="light", outline=True),
        ],
        className="h-100 p-5 text-white bg-dark rounded-3",
    ),
    md=6,
)


jumbotron = dbc.Row(
    [left_jumbotron],
    className="align-items-md-stretch",
)


# Define contents of each section
about_section = html.Div(
    dbc.Col(
        [
            html.Div(
                [
                    html.H3('About', className='mb-4', id='about-section'),
                    html.P('I\'m Victor, a guy who likes to play with data!'),
                    html.P(
                        'If you\'ve got a project you\'d like to discuss, please get in touch through my LinkedIn profile.'),
                ]
            ),
            dbc.Button(
                html.I(className="bi bi-github 2x", children=" GitHub"),
                href="https://github.com/farvic",
                external_link=True,
                target="_blank",
                className="ml-2 btn btn-secondary",
                style={"margin-right": "10px"},
            ),
            dbc.Button(
                html.I(className="bi bi-linkedin 2x",
                       children=" LinkedIn"),
                href="https://www.linkedin.com/in/victorfa",
                external_link=True,
                target="_blank",
                className="ml-2 btn btn-info",
            ),

        ],
    ),
    className='mt-4 mb-8',
)


projects_section = html.Div(
    [
        dbc.Col(
            [
                dashboard,
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H2('Projects'),
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            new_card(title='Project 1', description='This is a description of project 1',
                                                     screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+1',
                                                                      'https://via.placeholder.com/300x200.png?text=Image+2'],
                                                     technology_icons=[
                                                         'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),
                                            xs=12, sm=6, md=4, lg=2
                                        ),
                                        dbc.Col(
                                            new_card(title='Project 2', description='This is a description of project 2',
                                                     screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+3',
                                                                      'https://via.placeholder.com/300x200.png?text=Image+2'],
                                                     technology_icons=[
                                                         'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),
                                            xs=12, sm=6, md=4, lg=2
                                        ),
                                        dbc.Col(
                                            new_card(title='Project 3', description='This is a description of project 3',
                                                     screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+3',
                                                                      'https://via.placeholder.com/300x200.png?text=Image+2'],
                                                     technology_icons=[
                                                         'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),
                                            xs=12, sm=6, md=4, lg=2
                                        ),
                                    ],
                                    style={"display": "flex",
                                           "flex-wrap": "wrap"},
                                ),
                            ]
                        )
                    ],

                )
            ]
        )
    ],
    className='container-fluid mt-4 mb-8'
)


# Contact section
contact_section = html.Div(id="contact-section", children=[
    html.H2("Contact"),
    html.P("You can contact me at:"),
    html.P("Email: example@example.com"),
    html.P("Phone: 123-456-7890"),
],
    className="section",
)


# Define layout of sidebar
sidebar = html.Div(
    [
        # html.H2("Victor", className="display-4"),
        # html.Hr(),
        dbc.Col(
            html.Button(
                # use the Bootstrap navbar-toggler classes to style the toggle
                html.Span(className="navbar-toggler-icon"),
                className="navbar-toggler",
                # the navbar-toggler classes don't set color, so we do it here
                style={
                    "color": "rgba(0,0,255,.5)",
                    "border-color": "rgba(0,0,255,1)",
                },
                id="toggle",
            ),
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
        dbc.Collapse(dbc.Nav(

            [
                dbc.NavItem(dbc.NavLink("About", href="#about-section")),
                dbc.NavItem(dbc.NavLink("Projects", href="#projects-section")),
                dbc.NavItem(dbc.NavLink("Contact", href="#contact-section")),
            ],
            vertical=True,
            pills=True,
        ),
            id="collapse",
        ),


    ],
    style={
        "position": "fixed",
        "top": "-1rem",
        "left": "0",
        "bottom": "0",
        "width": "15rem",
        "padding": "2rem 1rem",
    },
)


# Define main content layout
content = html.Div(
    [
        about_section,
        projects_section,
        contact_section
    ],
    className="content",
)


navbar_collapse = dbc.Collapse(
    navbar,
    id="navbar-collapse",
    navbar=True,
    is_open=False,
)

# Define the layout
app.layout = html.Div(
    [
        dbc.Row([
            sidebar,
            content,
            html.A(
                html.I(className="fas fa-chevron-up fa-3x"),
                href="#navbar-collapse",
                id="scroll-to-top",
            ),
        ]),

    ],
    className='container-fluid'
)

# callback to scroll to the contact section when the Contact link is clicked


# @app.callback(Output("page-content", "children"),
#               [Input("collapse", "is_open")],
#               [State("collapse", "is_open")],
#               prevent_initial_call=True)
# def scroll_to_contact(navbar_is_open, navbar_is_closed):
#     if not navbar_is_open and navbar_is_closed:
#         return [
#             about_section,
#             projects_section,
#             dcc.Location(id="url", refresh=False),
#             html.Div(id="contact-scroll-target"),
#             contact_section,
#         ]
#     else:
#         return [
#             about_section,
#             projects_section,
#             contact_section,
#         ]


# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open


# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open


if __name__ == '__main__':
    app.run_server(debug=True)

from dash import dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

# Create the app and set the stylesheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc.icons.BOOTSTRAP], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
])


# Define the list of images
images = ['https://via.placeholder.com/300x200.png?text=Image+1',
          'https://via.placeholder.com/300x200.png?text=Image+2',
          'https://via.placeholder.com/300x200.png?text=Image+3']

# Define the placeholder dashboard section
dashboard = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H2("Placeholder Dashboard",
                            className="text-center text-info mb-4", id="projects-section"),
                    width={"size": 12, "offset": 0},
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=px.scatter(
                            x=[1, 2, 3], y=[1, 2, 3], title="Placeholder Graph")
                    ),
                    width={"size": 8, "offset": 2},
                )
            ]
        ),
    ],
    className="mt-4",
)


def new_card(title, description, screenshot_urls, technology_icons):
    # return a dbc.Card with the given title, description, screenshot and technology icons
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
                    # dbc.CardFooter(
                    #     children=[html.Img(
                    #         src=icon) for icon in technology_icons]
                    # ),
                    html.Div(
                        className="project-technologies",
                        children=[html.Img(
                            src=icon, className="project-technology-icon") for icon in technology_icons],

                        style={"margin-top": "20px", "margin-bottom": "-10px"},
                    ),
                ]
            ),
        ],
        # className="rounded",
        style={"width": "18rem"},
    )


# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Welcome :)", className="display-5")),
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
    ]
)
# https://img.shields.io/badge/Python-white?logo=Python
# https://img.shields.io/badge/Jupyter-white?logo=Jupyter

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

right_jumbotron = dbc.Col(
    html.Div(
        [
            html.H2("Add borders", className="display-3"),
            html.Hr(className="my-2"),
            html.P(
                "Or, keep it light and add a border for some added definition "
                "to the boundaries of your content."
            ),
            dbc.Button("Example Button", color="secondary", outline=True),
        ],
        className="h-100 p-5 bg-light border rounded-3",
    ),
    md=6,
)

jumbotron = dbc.Row(
    [left_jumbotron, right_jumbotron],
    className="align-items-md-stretch",
)

# Define the app layout with the card element
project_section = html.Div(
    [
        dbc.Col(
            [
                dashboard,
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H2('Projects'),
                                jumbotron,
                                dbc.Row(
                                    [
                                        new_card(title='Project 1', description='This is a description of project 1',
                                                 screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+1',
                                                                  'https://via.placeholder.com/300x200.png?text=Image+2'],
                                                 technology_icons=[
                                                     'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),

                                        new_card(title='Project 2', description='This is a description of project 2',
                                                 screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+3',
                                                                  'https://via.placeholder.com/300x200.png?text=Image+2'],
                                                 technology_icons=[
                                                     'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),

                                        new_card(title='Project 3', description='This is a description of project 3',
                                                 screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+3',
                                                                  'https://via.placeholder.com/300x200.png?text=Image+2'],
                                                 technology_icons=[
                                                     'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),
                                    ],
                                ),
                            ]
                        )
                    ],
                    # md=8,
                )
            ]
        )
    ],
    className='container-fluid'
)

# Contact section
contact_section = html.Div(
    [
        html.H3("Contact", id="contact-section"),
        html.P("Content of the contact section..."),
    ],
    className="section",
)

sidebar = html.Div(
    [
        sidebar_header,
        about_section,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "Heeeeeeeey there, I'm a sidebar! "
                    ":)",
                    className="lead",
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink(
                        "Projects", href="#projects-section", active="exact"),
                    dbc.NavLink("Contact", href="#contact-section",
                                active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    className="sidebar col-md-2 ",
    # style={"position": "fixed", "height": "100%", "width": "200px",
    #        "top": "0", "left": "0", "zIndex": "999"},
)

content = html.Div(
    [
        project_section,
        contact_section
    ],
    className="content col-md-9"
)

app.layout = html.Div(
    [
        dbc.Row([sidebar, content])
    ],
    className="container-fluid"
)


@ app.callback(
    Output("collapse", "is_open"),
    [Input("toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)

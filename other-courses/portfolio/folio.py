from dash import dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

# Create the app and set the stylesheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
])


# Define the list of images
images = ['https://via.placeholder.com/300x200.png?text=Image+1',
          'https://via.placeholder.com/300x200.png?text=Image+2',
          'https://via.placeholder.com/300x200.png?text=Image+3']

# Project card


def project_card(title, description, screenshot_urls, technology_icons):
    screenshots_html = [
        html.Img(src=url, className="project-screenshot") for url in screenshot_urls]

    return html.Div(
        className="project-card",
        children=[
            html.Div(
                className="project-presentation",
                children=[html.Img(src=screenshot_urls[i], className="project-screenshot", style={"opacity": 1 if i == 0 else 0})
                          for i in range(len(screenshot_urls))]
            ),
            html.Div(
                className="project-info",
                children=[
                    html.H3(title),
                    html.P(description),
                    html.Div(
                        className="project-technologies",
                        children=[html.Img(
                            src=icon, className="project-technology-icon") for icon in technology_icons]
                    ),
                ],
            ),
        ],
    )


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

# sidebar = html.Div(
#     [
#         sidebar_header,
#         # we wrap the horizontal rule and short blurb in a div that can be
#         # hidden on a small screen
#         html.Div(
#             [
#                 html.Hr(),
#                 html.P(
#                     "Heeeeeeeey there, I'm a sidebar! "
#                     ":)",
#                     className="lead",
#                 ),
#             ],
#             id="blurb",
#         ),
#         # use the Collapse component to animate hiding / revealing links
#         dbc.Collapse(
#             dbc.Nav(
#                 [
#                     dbc.NavLink("About", href="/", active="exact"),
#                     dbc.NavLink("Projects", href="/projects-section",
#                                 active="exact"),
#                     dbc.NavLink("Contact", href="/contact-section",
#                                 active="exact"),
#                 ],
#                 vertical=True,
#                 pills=True,
#             ),
#             id="collapse",
#         ),
#     ],
#     className="sidebar col-md-2"
# )

# sidebar = html.Div(
#     [
#         html.H2("My Website", className="display-4"),
#         html.Hr(),
#         html.P("Navigate to:"),
#         dbc.Nav(
#             [
#                 dbc.NavLink("About", href="#about-section"),
#                 dbc.NavLink("Projects", href="#projects-section"),
#                 dbc.NavLink("Contact", href="#contact-section"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     className="sidebar",
# )

# Define layout of sidebar


about_section = html.Div(
    dbc.Col(
        [
            html.Div(
                [
                    html.H2('About', className='mb-4', id='about-section'),
                    html.P('Some text about you and your skills.'),
                    html.P(
                        'You can also add more text here if you want.'),
                    html.P('Contact me at email@example.com.')
                ]
            )
        ],
        md=4
    ),
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
                                html.H2('Projects', className='mb-4'),
                                new_card(title='Project 1', description='This is a description of project 1', screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+1', 'https://via.placeholder.com/300x200.png?text=Image+2'], technology_icons=[
                                    'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),
                                project_card(title='Project 1', description='This is a description of project 1', screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+1', 'https://via.placeholder.com/300x200.png?text=Image+2'], technology_icons=[
                                             'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),
                                project_card(title='Project 2', description='This is a description of project 2', screenshot_urls=['https://via.placeholder.com/300x200.png?text=Image+1', 'https://via.placeholder.com/300x200.png?text=Image+2'], technology_icons=[
                                             'https://img.shields.io/badge/Python-white?logo=Python', 'https://img.shields.io/badge/Jupyter-white?logo=Jupyter']),

                            ]
                        )
                    ],
                    md=8
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
        html.H2("My Portfolio", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("About", href="#about_section")),
                dbc.NavItem(dbc.NavLink("Projects", href="#projects_section")),
                dbc.NavItem(dbc.NavLink("Contact", href="#contact_section")),
            ],
            vertical=True,
            pills=True,
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

# Define the callback for the hover effect


# @ app.callback(
#     dash.Output('card-images', 'style'),
#     dash.Input('card-images', 'n_clicks'),
#     State('card-images', 'style')
# )
# def update_card_images(n_clicks, style):
#     current_image_index = images.index(
#         style['background-image'].replace('url(', '').replace(')', ''))
#     next_image_index = (current_image_index + 1) % len(images)
#     return {'background-image': f'url({images[next_image_index]})', 'transition': 'background-image 0.5s ease-in-out'}


content = html.Div(id="page-content")


# sidebar = html.Div(
#     [
#         html.H2("My Website", className="display-4"),
#         html.Hr(),
#         html.P("Navigate to:"),
#         dbc.Nav(
#             [
#                 dbc.NavLink("About", href="about-section"),
#                 dbc.NavLink("Projects", href="projects-section"),
#                 dbc.NavLink("Contact", href="contact-section"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     className="sidebar col-md-2"
# )

# content = html.Div(
#     [
#         about_section,
#         project_section,
#         contact_section
#     ],
#     className="content col-md-9"
# )

# app.layout = html.Div(
#     [
#         dbc.Row([sidebar, content])
#     ],
#     className="container-fluid"
# )

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@ app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return about_section
    elif pathname == "/projects-section":
        return project_section
    elif pathname == "/contact-section":
        return contact_section
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 rounded-3",
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

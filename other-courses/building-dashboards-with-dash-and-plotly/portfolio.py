import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Define cyberpunk colors
cyberpunk_colors = {
    'dark_bg': '#111111',
    'light_bg': '#333333',
    'light_fg': '#ffffff',
    'highlight': '#00ff99',
    'accent': '#ff00ff'
}

# Load sample data
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Define app layout
app = dash.Dash(__name__)
app.layout = html.Div(style={'backgroundColor': cyberpunk_colors['dark_bg']}, children=[
    html.H1(
        children='Data Science Dashboard',
        style={
            'textAlign': 'center',
            'color': cyberpunk_colors['light_fg']
        }
    ),

    html.Div(children='Gapminder Data (1952-2007)', style={
        'textAlign': 'center',
        'color': cyberpunk_colors['light_fg']
    }),

    # (
    #                 xaxis=dict(title="GDP per capita",
    #                            gridcolor=cyberpunk_colors['light_fg']),
    #                 yaxis=dict(title="Life expectancy",
    #                            gridcolor=cyberpunk_colors['light_fg']),
    #                 margin=dict(l=50, r=50, b=50, t=50),
    #                 hovermode="closest",
    #                 plot_bgcolor=cyberpunk_colors['dark_bg'],
    #                 paper_bgcolor=cyberpunk_colors['dark_bg'],
    #                 font=dict(color=cyberpunk_colors['light_fg']),
    #                 title=dict(
    #                     text="Life Expectancy vs GDP per Capita (1952-2007)",
    #                     font=dict(size=24, color=cyberpunk_colors['light_fg']),
    #                     x=0.5,
    #                     y=0.95,
    #                     xanchor='center',
    #                     yanchor='top'
    #                 )
    #             )

    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                px.scatter(
                    df.query("year=={}".format(i)), x="gdpPercap", y="lifeExp", size="pop", color="continent",
                    log_x=True, size_max=60, title="Year: {}".format(i)
                ).update_traces(marker=dict(sizemode='diameter', sizeref=0.1, opacity=0.7, line_width=0))
                for i in df.year.unique()
            ],
        },

    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

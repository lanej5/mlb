# main.py
"""Dashboard entry point."""
from dash import Dash, html, dcc
from flask import Flask
from visualize import postseason_race

server = Flask(__name__)

# get data
fig, created = postseason_race()
code_src = "[View source on github](https://github.com/lanej5/mlb)."
data_src = "Data from [FanGraphs](https://www.fangraphs.com/)."
updated = f"Last updated {created.strftime('%B %-d, %Y at %-I:%M %p')}"   
text = " ".join([code_src, data_src, updated])

# create the dashboard
app = Dash(__name__, server=server)
app.title = 'Postseason Race'
app.layout = html.Div(children=[
  dcc.Graph(
    id='postseason_race',
    figure=fig
  ),
  dcc.Markdown(children=text)
])

if __name__ == '__main__':
  app.run_server(debug=True)

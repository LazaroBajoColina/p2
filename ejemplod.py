import dash
from dash import dcc, html, Input, Output, callback_context
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = pd.DataFrame({
    "Fruta": ["Manzanas", "Naranjas", "Bananas", "Manzanas", "Naranjas", "Bananas"],
    "Cantidad": [4, 1, 2, 2, 4, 5],
    "Ciudad": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Crear la figura con Plotly
fig = px.bar(df, x="Fruta", y="Cantidad", color="Ciudad", barmode="group")

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Exponer el servidor Flask para Gunicorn
server = app.server

# Diseño del dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Frutas'),

    html.Div(children='''
        Un dashboard sencillo de ejemplo con Plotly Dash.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Ejecutar la aplicación (solo para desarrollo local)
if __name__ == '__main__':
    app.run(debug=False)
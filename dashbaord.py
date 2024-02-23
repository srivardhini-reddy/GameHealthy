import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Sample data (replace with your anomaly data)
anomaly_data = {
    'Skin': {'Metric1': 10, 'Metric2': 5},
    'Eyes': {'Metric1': 8, 'Metric2': 2},
    'Posture': {'Metric1': 8, 'Metric2': 2},
    
}

# Define layout
app.layout = html.Div([
    html.Img(src='Assets/silhouette-of-a-human-body-free-vector-removebg-preview.png', style={'width': '60%', 'height': 'auto'}),
    dcc.Graph(id='anomaly-graph')
])

# Callback for updating the graph
@app.callback(
    Output('anomaly-graph', 'figure'),
    Input('anomaly-graph', 'hoverData')
)
def update_graph(hover_data):
    # Implement logic to update graph based on hover_data
    # You can use hover_data to fetch corresponding metrics and display

    # For simplicity, let's just display a sample scatter plot
    figure = {
        'data': [
            {'x': list(anomaly_data.keys()), 'y': [data['Metric1'] for data in anomaly_data.values()], 'type': 'bar', 'name': 'Metric1'},
            {'x': list(anomaly_data.keys()), 'y': [data['Metric2'] for data in anomaly_data.values()], 'type': 'bar', 'name': 'Metric2'},
        ],
        'layout': {
            'title': 'Anomaly Metrics',
            'hovermode': 'closest',
        }
    }

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)



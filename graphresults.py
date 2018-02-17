import plotly.graph_objs as graph_objs
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

from datetime import datetime
import sqlite3

db_filename = "speedtest.db"

def plot_results(timestart, timeend):
    # connect to the db
    db = sqlite3.connect(db_filename)
    cur = db.cursor()

    # get tuples for the specified time
    cur.execute('''
        SELECT * FROM results WHERE timestamp>? AND timestamp<?;
    ''', (timestart, timeend))
    results = cur.fetchall()

    # create x and y data
    y_downloads = []
    y_uploads = []
    x_times = []
    for result in results:
        y_downloads.append(result[1])
        y_uploads.append(result[2])
        x_times.append(result[16])

    # Create a trace
    trace_downloads = graph_objs.Scatter(
        x=x_times,
        y=y_downloads,
        mode="lines+markers",
        name="Download"
    )
    trace_uploads = graph_objs.Scatter(
        x=x_times,
        y=y_uploads,
        mode="lines+markers",
        name="Upload"
    )
    layout = graph_objs.Layout(
        title="Internet Speed over Time",
        xaxis=dict(
            title="Time (HH:MM)"
        ),
        yaxis=dict(
            title="Speed (bps)"
        )
    )
    data = [trace_downloads, trace_uploads]
    figure = graph_objs.Figure(data=data, layout=layout)
    plot(figure)

def main():
    plot_results("2010-02-17T15:16:38.525305Z", "2019-02-17T15:16:38.525305Z")

if __name__ == "__main__":
    main()

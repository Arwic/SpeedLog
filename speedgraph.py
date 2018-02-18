import plotly.graph_objs as graph_objs
from plotly.offline import plot
import sqlite3
import dateutil.parser as dateparser
from dateutil import tz

db_filename = "speedresults.db"

def plot_results(timestart, timeend):
    # connect to the db
    db = sqlite3.connect(db_filename)
    cur = db.cursor()

    # get tuples for the specified time
    cur.execute('''
        SELECT * FROM results WHERE timestamp>? AND timestamp<?;
    ''', (timestart, timeend))
    results = cur.fetchall()

    # time zones
    tz_utc = tz.tzutc()
    tz_local = tz.tzlocal()

    # create x and y data
    y_downloads = []
    y_uploads = []
    x_times = []
    for r in results:
        y_downloads.append(r[1])
        y_uploads.append(r[2])
        ts_naive = dateparser.parse(r[16])
        ts_utc = ts_naive.replace(tzinfo=tz_utc)
        ts_local = ts_utc.astimezone(tz_local)
        x_times.append(ts_local.strftime("%Y-%m-%dT%H:%M:%S"))

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
    plot_results("0001-01-01T00:00:00.000000Z", "9999-01-01T00:00:00.000000Z")

if __name__ == "__main__":
    main()

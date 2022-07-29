# Imports and setup
import math
import statistics
from pathlib import Path
from typing import TextIO

import gpxpy
import gpxpy.gpx
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from zoom_center import mapbox_args

TIME_SEC = 60
FRAMES = 500
# Zoom levels between 0 and 20. Higher levels are more zoomed in.
ZOOM_BEGIN = 15
ZOOM_END = 12


# Utility functions from the other notebooks
def read_gpx(file: TextIO) -> pd.DataFrame:
    with open(file, "r", encoding="UTF-8") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    route_info = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                route_info.append(
                    {
                        "latitude": point.latitude,
                        "longitude": point.longitude,
                        "elevation": point.elevation,
                    }
                )

    # Convert to pandas dataframe
    route_df = pd.DataFrame(route_info[100:-100])
    route_df["title"] = gpx.tracks[0].name
    route_df["start_time"] = gpx.time

    return route_df


# Read all gpx files
routes = [read_gpx(gpx_file) for gpx_file in Path(__file__).parent.glob("*.gpx")]

center_lat = statistics.median([df.latitude[0] for df in routes])
center_lon = statistics.median([df.longitude[0] for df in routes])
max_length = max([df.shape[0] for df in routes])

# Animation
fig = go.Figure(
    data=[
        go.Scattermapbox(
            mode="lines",
            line=dict(width=3.5, color="rgba(255,50,10,.3)"),
            hovertemplate=f"{df.title[0]} ({df.start_time[0]:%e %b %Y})<extra></extra>",
        )
        for df in routes
    ]
    + [go.Scattermapbox(hoverinfo="skip")],
    layout=go.Layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox={
            "center": {"lat": center_lat, "lon": center_lon},
            "style": "carto-darkmatter",
            "zoom": ZOOM_BEGIN,
        },
        showlegend=False,
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                x=0,
                xanchor="left",
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": TIME_SEC * 1000 / FRAMES},
                            },
                        ],
                    ),
                    dict(
                        label="Pause",
                        method="animate",
                        args=[
                            [None],
                            {"frame": {"redraw": False}, "mode": "immediate"},
                        ],
                    ),
                    dict(
                        label="Dark",
                        method="relayout",
                        args=[
                            {
                                "mapbox": {
                                    "center": {"lat": center_lat, "lon": center_lon},
                                    "style": "carto-darkmatter",
                                    "zoom": ZOOM_BEGIN,
                                },
                            },
                        ],
                    ),
                    dict(
                        label="Light",
                        method="relayout",
                        args=[
                            {
                                "mapbox": {
                                    "center": {"lat": center_lat, "lon": center_lon},
                                    "style": "carto-positron",
                                    "zoom": ZOOM_BEGIN,
                                },
                            },
                        ],
                    ),
                ],
            )
        ],
    ),
    frames=[
        go.Frame(
            data=[
                go.Scattermapbox(
                    lat=df.latitude.iloc[:i],
                    lon=df.longitude.iloc[:i],
                )
                for df in routes
            ]
            + [
                go.Scattermapbox(
                    lat=[df.latitude[min(i - 1, df.shape[0] - 1)] for df in routes],
                    lon=[df.longitude[min(i - 1, df.shape[0] - 1)] for df in routes],
                )
            ],
            layout=go.Layout(mapbox=mapbox_args(routes, math.ceil(i / 50) * 50, 2)),
        )
        # for i in range(1, max_length, math.floor(max_length / FRAMES))
        for i in np.linspace(1, max_length, FRAMES).astype(int)
    ],
)
fig.show()

"""'zoom': round(ZOOM_BEGIN + (ZOOM_END - ZOOM_BEGIN) * i / max_length, 2)"""
"""'zoom': round(
                        ZOOM_END
                        + (ZOOM_BEGIN - ZOOM_END)
                        * abs(math.pow((i - max_length) / max_length, 3)),
                        2,
                    )"""

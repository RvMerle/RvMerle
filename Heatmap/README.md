# Heatmap

The main idea of this project is to make a heatmap out of gps data from my runs and bike rides. For this, I downloaded a number of .gpx files from Strava and visualised them with Python. The order in which I made the files is as follows:

1. [Initial exploration (gpx.ipynb)](https://nbviewer.org/github/RvMerle/RvMerle/blob/main/Heatmap/gpx.ipynb)
2. [Plotting multiple gpx files in a single figure and attempt of a heatmap (gpx_multiple.ipynb)](https://nbviewer.org/github/RvMerle/RvMerle/blob/main/Heatmap/gpx_multiple.ipynb)
3. [Animating the heatmap (gpx_animation.ipynb)](https://nbviewer.org/github/RvMerle/RvMerle/blob/main/Heatmap/gpx_animation.ipynb)
4. [Browser implementation of animated heatmap (gpx_animation.py)](gpx_animation.py)

# Results

These two images are both from [gpx_multiple.ipynb](gpx_multiple.ipynb):

<img src="https://user-images.githubusercontent.com/8127492/181770586-333e8975-755e-4131-a2f8-5bf6a0d5a5c1.png" width="48%"> <img src="https://user-images.githubusercontent.com/8127492/181770612-c6ebe5c4-3fe2-4685-b71c-434bad05a46e.png" width="48%">

I made this map in [QGIS](https://www.qgis.org/en/site/), but unfortunately I have not been able to recreate it yet in Python:

![Heatmap](https://user-images.githubusercontent.com/8127492/181775946-dbf1fee3-e7b2-4831-92f8-db9cbd5286c1.jpg)

Slightly glitched animation from [gpx_animation.py](gpx_animation.py):

https://user-images.githubusercontent.com/8127492/181772542-597dbe69-ddbe-4ad3-a5ea-a93bb909671e.mp4

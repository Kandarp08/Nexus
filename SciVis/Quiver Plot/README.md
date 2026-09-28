# Wind Quiver Plot Visualization

This project generates a GIF animation of wind data visualizations for selected dates using quiver plots in Matplotlib. Each frame in the GIF includes two side-by-side plots: one with vectors of varying lengths based on wind speed, and one with normalized vectors of the same length.

## Project Overview

- **Data Source:** NetCDF files containing wind speed and direction data for each selected date.
- **Visualization:** Quiver plots showing wind direction and speed.
- **Output:** A GIF animation that displays side-by-side plots for each selected date.

## Features

1. **Filtered Data:** The `filter_data` function applies a moving average filter for smooth transitions in the data.
2. **Date-Specific Frames:** The `date_list` contains the dates to visualize.
3. **Quiver Plot Configurations:**
   - Left Plot: Displays wind vectors of different lengths based on wind speed.
   - Right Plot: Displays wind vectors normalized to the same length.
4. **GIF Creation:** Frames are saved as individual images and then compiled into an animated GIF.

## Requirements

- Python 3.x
- Libraries:
  - `matplotlib`
  - `netCDF4`
  - `numpy`
  - `Pillow`

Install the necessary packages using:
```bash
pip install matplotlib netCDF4 numpy pillow
```

## Usage
1. **Run the code**:
Run the Python script to generate the GIF. The script will:

- Process each specified date.
- Generate two side-by-side quiver plots for each date.
- Save each plot as a frame and compile them into an animated GIF.

2. **Output**:
- The GIF will be saved as `wind_animation.gif` in the 'Quiver Plot' project directory.

## Code Explaination
- **Date Iteration and Data Extraction**: Each date is iterated to retrieve corresponding wind speed and direction data.
- **Vector Sampling**: Wind vectors are sampled to avoid overly dense plots and improve readability.
- **Quiver Plotting**:  Creates two plots:
    - Left Plot: Varying vector lengths based on wind speed.
    - Right Plot: Same vector length with contours of wind speed.
- **GIF Creation**: Uses `Pillow` to compile the frames into a GIF animation.
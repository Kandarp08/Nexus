This Python script analyzes and visualizes fire weather data stored in a NetCDF file named extracted_data.nc. The script leverages libraries like NumPy, Matplotlib, xarray, and netCDF4 to achieve the following:

Data Exploration: Extracts relevant variables representing fire weather conditions like burning index (bi), relative humidity (rmin, rmax), temperature (tmmx, tmmn), and precipitation (pr).
Data Normalization: Applies various normalization techniques (global and local) to ensure color maps effectively represent data variations across different spatial locations.
Dual Color Map Visualization: Creates dual color map visualizations displaying two fire weather variables simultaneously. Both global (normalizing across all data points) and local (normalizing for each day) normalization options are available.
Logarithmic Continuous Color Maps: Generates visualizations with logarithmic color scales for variables with positive values that span several orders of magnitude (e.g., reference evapotranspiration).
Discrete Color Maps: Creates visualizations with discrete color bins for variables with a limited range of distinct categories.
Animation: Generates animations showcasing the temporal evolution of fire weather variables using dual color maps with local normalization.
Script Functionality

The script provides several functions:

plot_global_dual_color_maps(ds, var_name1, var_name2, day, cmap1='viridis', cmap2='plasma'): Creates a dual color map visualization with global normalization for a specified day, variables, and colormaps.
plot_dual_color_maps(ds, var_name1, var_name2, day, folder_path='plots', cmap1='viridis', cmap2='plasma'): Generates a dual color map visualization with local normalization, saving the plot to a specified folder.
plot_single_log_continuous_color_map(ds, var_name, day, folder_path='plots', cmap='viridis'): Creates a visualization using a logarithmic color map for a single variable and day, saving it to a folder.
plot_single_discrete_color_map(ds, var_name, day, folder_path='plots', cmap='viridis', num_bins=10): Generates a visualization with a discrete color map for a single variable and day, specifying the number of color bins.
animate_color_maps(ds, var_name1, var_name2, cmap1='viridis', cmap2='plasma', start_day=0, end_day=None, interval=200): Creates an animation using dual color maps with local normalization for a specified variable pair, animation range (days), and interval.
animate_with_global_color_maps(ds, var_name1, var_name2, cmap1='viridis', cmap2='plasma', start_day=0, end_day=None, interval=200): Similar to animate_color_maps but employs global normalization.
Running the Script

Prerequisites: Ensure you have Python 3.x, NumPy, Pandas, Matplotlib, NetCDF4, and xarray installed. You can install them using pip install numpy pandas matplotlib netCDF4 xarray.
Place the Script and Data Together: Put the script (color_map.py) in the same directory as your NetCDF file (extracted_data.nc).
Run the Script: Execute the script from the command line using python3 color_map.py.
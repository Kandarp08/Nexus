
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
import netCDF4 as nc
import xarray as xr
import os

# Extracting the sampled Dates and also mapping var to their fulforms.


ds=nc.Dataset('extracted_data.nc')
var_to_name = {"bi": "Burning index", "rmin": "Min Relative Humidity", "rmax": "Max Relative Humidity", "pet": "Daily grass reference evapotranspiration", 
               "etr": "Daily alfalfa reference evapotranspiration", "pr": "Precipitation amount", "fm1000": "1000-hour dead fuel moisture", 
               "fm100": "100-hour dead fuel moisture", "sph": "Specific humididy", "srad": "surface_downwelling_shortwave_flux_in_air",
               "th": "wind_from_direction", "tmmn": "Min temperature", "tmmx": "Max temperature", "vpd": "mean_vapor_pressure_deficit",
               "vs": "wind_speed"}


# Function for plotting dual color maps with global maxima minima normalization

Days = {
    0: "10/11/2023", 1: "20/11/2023", 2: "30/11/2023",
    3: "10/12/2023", 4: "20/12/2023", 5: "30/12/2023",
    6: "10/01/2024", 7: "20/01/2024", 8: "30/01/2024"
}
def plot_global_dual_color_maps(ds, var_name1, var_name2, day, cmap1='viridis', cmap2='plasma'):
    # Extract data for the specified variables and day
    data1 = ds.variables[var_name1][day, :, :]
    data2 = ds.variables[var_name2][day, :, :]
    
    # Get min and max values for normalization
    vmin1, vmax1 = np.nanmin(data1), np.nanmax(data1)
    vmin2, vmax2 = np.nanmin(data2), np.nanmax(data2)
    
    # Extract latitude and longitude
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]
    
    # Create normalization objects
    norm1 = mcolors.Normalize(vmin=vmin1, vmax=vmax1)
    norm2 = mcolors.Normalize(vmin=vmin2, vmax=vmax2)
    
    # Set up the figure and axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Plot for the first variable
    c1 = ax1.pcolormesh(lons, lats, data1, cmap=cmap1, norm=norm1, shading='auto')
    cbar1 = fig.colorbar(ScalarMappable(norm=norm1, cmap=cmap1), ax=ax1, orientation='vertical', shrink=0.8, pad=0.02)
    cbar1.set_label(var_name1, rotation=270, labelpad=15)
    ax1.set_title(f'{var_to_name[var_name1]} on Day {Days[day]}')
    ax1.set_xlabel('Longitude')
    ax1.set_ylabel('Latitude')
    
    # Plot for the second variable
    c2 = ax2.pcolormesh(lons, lats, data2, cmap=cmap2, norm=norm2, shading='auto')
    cbar2 = fig.colorbar(ScalarMappable(norm=norm2, cmap=cmap2), ax=ax2, orientation='vertical', shrink=0.8, pad=0.02)
    cbar2.set_label(var_name2, rotation=270, labelpad=15)
    ax2.set_title(f'{var_to_name[var_name2]} on Day {Days[day]}')
    ax2.set_xlabel('Longitude')
    ax2.set_ylabel('Latitude')
    
    plt.tight_layout()
    plt.show()




# Function for plotting dual color maps with local normalization

Days = {
    0: "10/11/2023", 1: "20/11/2023", 2: "30/11/2023",
    3: "10/12/2023", 4: "20/12/2023", 5: "30/12/2023",
    6: "10/01/2024", 7: "20/01/2024", 8: "30/01/2024"
}
Units={'tmmx':'K','tmmn':'K',"bi":"NFDRS fire danger index","fm100":"%","fm1000":"%","pet":"mm","etr":"mm","pr":"mm/daily total"
       ,"vpd":"kPa","rmax":"%","rmin":"%","sph":"Mass Fraction"}
def plot_dual_color_maps(ds, var_name1, var_name2, day, folder_path='plots', cmap1='viridis', cmap2='plasma'):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Extract data for the specified variables and day
    data1 = ds.variables[var_name1][day, :, :]
    data2 = ds.variables[var_name2][day, :, :]

    # Local normalization for each dataset
    vmin1, vmax1 = np.nanmin(data1), np.nanmax(data1)
    vmin2, vmax2 = np.nanmin(data2), np.nanmax(data2)

    # Extract latitude and longitude
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]

    # Create normalization objects for local scaling
    norm1 = mcolors.Normalize(vmin=vmin1, vmax=vmax1)
    norm2 = mcolors.Normalize(vmin=vmin2, vmax=vmax2)

    # Set up the figure and axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Plot for the first variable
    c1 = ax1.pcolormesh(lons, lats, data1, cmap=cmap1, norm=norm1, shading='auto')
    cbar1 = fig.colorbar(ScalarMappable(norm=norm1, cmap=cmap1), ax=ax1)
    unit1 = Units.get(var_name1, '')  # Get the unit from the Units dictionary
    cbar1.set_label(f'{var_to_name[var_name1]} ({unit1})', rotation=270, labelpad=15)
    ax1.set_title(f'{var_to_name[var_name1]} on {Days.get(day, "Unknown Date")}')
    ax1.set_xlabel('Longitude')
    ax1.set_ylabel('Latitude')

    # Plot for the second variable
    c2 = ax2.pcolormesh(lons, lats, data2, cmap=cmap2, norm=norm2, shading='auto')
    cbar2 = fig.colorbar(ScalarMappable(norm=norm2, cmap=cmap2), ax=ax2)
    unit2 = Units.get(var_name2, '')  # Get the unit from the Units dictionary
    cbar2.set_label(f'{var_to_name[var_name2]} ({unit2})', rotation=270, labelpad=15)
    ax2.set_title(f'{var_to_name[var_name2]} on {Days.get(day, "Unknown Date")}')
    ax2.set_xlabel('Longitude')
    ax2.set_ylabel('Latitude')

    plt.tight_layout()

    # Save the plot to the specified folder
    file_name = f"{var_name1}_{var_name2}_Day_{day}.png"
    file_path = os.path.join(folder_path, file_name)
    plt.savefig(file_path, dpi=300)
    
    # plt.show()




# Function for plotting color maps using logarithmic normalization


def plot_single_log_continuous_color_map(ds, var_name, day, folder_path='plots', cmap='viridis'):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Extract data for the specified variable and day
    data = ds.variables[var_name][day, :, :]
    
    # Mask out non-positive values (since log scale cannot handle non-positive data)
    data = np.ma.masked_less_equal(data, 0)

    # Extract latitude and longitude
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]

    # Create a normalization object for continuous logarithmic scaling
    norm = mcolors.LogNorm(vmin=np.nanmin(data), vmax=np.nanmax(data))

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot for the variable using continuous and logarithmic color map
    c = ax.pcolormesh(lons, lats, data, cmap=cmap, norm=norm, shading='auto')
    cbar = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), ax=ax)
    cbar.set_label(var_name, rotation=270, labelpad=15)
    cbar.ax.set_yticklabels([f'{tick:.2e}' for tick in cbar.get_ticks()])  # Format tick labels in scientific notation

    ax.set_title(f'{var_to_name[var_name]} on {Days.get(day, "Unknown Date")}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.tight_layout()

    # Save the plot to the specified folder
    file_name = f"{var_name}_Day_{day}_log_continuous.png"
    file_path = os.path.join(folder_path, file_name)
    plt.savefig(file_path, dpi=300)
    
    plt.show()



# Function for plotting color map with discrete color scheme


def plot_single_discrete_color_map(ds, var_name, day, folder_path='plots', cmap='viridis', num_bins=10):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Extract data for the specified variable and day
    data = ds.variables[var_name][day, :, :]

    # Define linear bins for the color scale
    linear_bins = np.linspace(np.nanmin(data), np.nanmax(data), num_bins)

    # Extract latitude and longitude
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]

    # Create a normalization object for discrete scaling
    norm = mcolors.BoundaryNorm(linear_bins, cmap.N, extend='both')

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot for the variable using a discrete color map
    c = ax.pcolormesh(lons, lats, data, cmap=cmap, norm=norm, shading='auto')
    cbar = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), ax=ax, ticks=linear_bins)
    cbar.set_label(var_name, rotation=270, labelpad=15)
    cbar.ax.set_yticklabels([f'{tick:.2f}' for tick in linear_bins])  # Format tick labels with 2 decimal places

    ax.set_title(f'{var_to_name[var_name]} on {Days.get(day, "Unknown Date")}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.tight_layout()

    # Save the plot to the specified folder
    file_name = f"{var_name}_Day_{day}_discrete.png"
    file_path = os.path.join(folder_path, file_name)
    plt.savefig(file_path, dpi=300)
    
    # plt.show()


plot_single_log_continuous_color_map(ds,'tmmx',day=0)


for i in range(9):
    plot_dual_color_maps(ds,var_name1='tmmx',var_name2='bi',day=i)


for i in range(9):
    plot_dual_color_maps(ds,var_name1='tmmx',var_name2='tmmn',day=i)


plot_dual_color_maps(ds,var_name1="pr",var_name2="pet",day=8)

# Function for creating gijs with global normalization

# Dictionary of days for labeling
Days = {
    0: "10/11/2023", 1: "20/11/2023", 2: "30/11/2023",
    3: "10/12/2023", 4: "20/12/2023", 5: "30/12/2023",
    6: "10/01/2024", 7: "20/01/2024", 8: "30/01/2024"
}

    # Animates two separate color maps for two different variables over multiple time steps using local normalization.
def animate_with_global_color_maps(ds, var_name1, var_name2, cmap1='viridis', cmap2='plasma', start_day=0, end_day=None, interval=200):

    # Extract latitude and longitude data
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]
    
    # Determine the range of time steps
    end_day = end_day or ds.variables[var_name1].shape[0]
    time_steps = range(start_day, end_day)
    
    # Normalize based on the data range for all time steps
    vmin1 = np.nanmin(ds.variables[var_name1][:])
    vmax1 = np.nanmax(ds.variables[var_name1][:])
    norm1 = mcolors.Normalize(vmin=vmin1, vmax=vmax1)
    
    vmin2 = np.nanmin(ds.variables[var_name2][:])
    vmax2 = np.nanmax(ds.variables[var_name2][:])
    norm2 = mcolors.Normalize(vmin=vmin2, vmax=vmax2)

    # Create the figure and two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Initial plots with first time step data
    color_map1 = ax1.pcolormesh(lons, lats, ds.variables[var_name1][start_day], cmap=cmap1, norm=norm1, shading='auto')
    color_map2 = ax2.pcolormesh(lons, lats, ds.variables[var_name2][start_day], cmap=cmap2, norm=norm2, shading='auto')

    # Set titles and labels
    ax1.set_title(f'Color Map for {var_to_name[var_name1]}')
    ax1.set_xlabel('Longitude')
    ax1.set_ylabel('Latitude')
    
    ax2.set_title(f'Color Map for {var_to_name[var_name2]}')
    ax2.set_xlabel('Longitude')
    ax2.set_ylabel('Latitude')

    # Add color bars for each plot
    cbar1 = fig.colorbar(ScalarMappable(norm=norm1, cmap=cmap1), ax=ax1, orientation='vertical', shrink=0.8, pad=0.02)
    cbar1.set_label(var_name1, rotation=270, labelpad=15)
    
    cbar2 = fig.colorbar(ScalarMappable(norm=norm2, cmap=cmap2), ax=ax2, orientation='vertical', shrink=0.8, pad=0.02)
    cbar2.set_label(var_name2, rotation=270, labelpad=15)

    # Update function for animation
    def update(day):
        # Update data for each subplot
        color_map1.set_array(ds.variables[var_name1][day].ravel())
        color_map2.set_array(ds.variables[var_name2][day].ravel())
        
        # Use the Days dictionary to show the date in the title
        fig.suptitle(f"Date: {Days.get(day, 'Unknown Date')}", fontsize=16)

    # Create animation
    ani = FuncAnimation(fig, update, frames=time_steps, interval=interval, repeat=True)

    plt.tight_layout()
    # plt.show()
    return ani



# Function for creating gijs with local normalization


# Dictionary of days for labeling
Days = {
    0: "10/11/2023", 1: "20/11/2023", 2: "30/11/2023",
    3: "10/12/2023", 4: "20/12/2023", 5: "30/12/2023",
    6: "10/01/2024", 7: "20/01/2024", 8: "30/01/2024"
}

    #Animates two separate color maps for two different variables over multiple time steps using local normalization.
def animate_color_maps(ds, var_name1, var_name2, cmap1='viridis', cmap2='plasma', start_day=0, end_day=None, interval=200):
    # Extract latitude and longitude data
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]
    
    # Determine the range of time steps
    end_day = end_day or ds.variables[var_name1].shape[0]
    time_steps = range(start_day, end_day)

    # Create the figure and two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Initial plots (with arbitrary data)
    color_map1 = ax1.pcolormesh(lons, lats, ds.variables[var_name1][start_day], cmap=cmap1, shading='auto')
    color_map2 = ax2.pcolormesh(lons, lats, ds.variables[var_name2][start_day], cmap=cmap2, shading='auto')

    # Set titles and labels
    ax1.set_title(f'Color Map for {var_to_name[var_name1]}')
    ax1.set_xlabel('Longitude')
    ax1.set_ylabel('Latitude')
    
    ax2.set_title(f'Color Map for {var_to_name[var_name2]}')
    ax2.set_xlabel('Longitude')
    ax2.set_ylabel('Latitude')

    # Add initial color bars (will be updated in `update`)
    cbar1 = fig.colorbar(ScalarMappable(cmap=cmap1), ax=ax1, orientation='vertical', shrink=0.8, pad=0.02)
    cbar1.set_label(var_name1, rotation=270, labelpad=15)
    
    cbar2 = fig.colorbar(ScalarMappable(cmap=cmap2), ax=ax2, orientation='vertical', shrink=0.8, pad=0.02)
    cbar2.set_label(var_name2, rotation=270, labelpad=15)

    # Update function for animation
    def update(day):
        # Extract data for the current day
        data1 = ds.variables[var_name1][day]
        data2 = ds.variables[var_name2][day]
        
        # Create local normalization for each timestep
        norm1 = mcolors.Normalize(vmin=np.nanmin(data1), vmax=np.nanmax(data1))
        norm2 = mcolors.Normalize(vmin=np.nanmin(data2), vmax=np.nanmax(data2))

        # Update the plots with new data and normalization
        color_map1.set_array(data1.ravel())
        color_map1.set_norm(norm1)
        
        color_map2.set_array(data2.ravel())
        color_map2.set_norm(norm2)
        
        # Update color bars to reflect local normalization
        cbar1.mappable.set_norm(norm1)
        cbar2.mappable.set_norm(norm2)

        # Update the title with the current day
        fig.suptitle(f"Date: {Days.get(day, 'Unknown Date')}", fontsize=16)

    # Create animation
    ani = FuncAnimation(fig, update, frames=time_steps, interval=interval, repeat=True)

    plt.tight_layout()
    # plt.show()
    return ani



ani=animate_color_maps(ds,var_name1='tmmx',var_name2='bi',start_day=0,end_day=9,interval=200)
ani.save('tmmx_bi.gif')


plot_dual_color_maps(ds,var_name1='bi',var_name2='fm100',day=0)


plot_dual_color_maps(ds,var_name1='tmmx',var_name2='fm100',day=0)


ani=animate_color_maps(ds,var_name1='tmmx',var_name2='fm100',start_day=0,end_day=9,interval=200)
ani.save('tmmx_fm100.gif')


plot_dual_color_maps(ds,var_name1='rmax',var_name2='pet',day=0)


ani=animate_color_maps(ds,var_name1='rmax',var_name2='pet',start_day=0,end_day=9,interval=200)
ani.save("pet_rmax.gif")


ani=animate_color_maps(ds,var_name1='pet',var_name2='tmmx',start_day=0,end_day=9,interval=200)
ani.save("pet_tmmx.gif")

ani=animate_color_maps(ds,var_name1='etr',var_name2='tmmx',start_day=0,end_day=9,interval=200)
ani.save("etr_tmmx.gif")



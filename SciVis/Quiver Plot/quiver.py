import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np
from datetime import date
from PIL import Image


# List of dates to generate frames for
date_list = [(2023, 11, 15), (2023, 12, 16), (2023, 12, 20), (2023, 12, 25), (2024, 1, 9), (2024, 1, 13)]

# Initialize list to store frames
frames = []

# Iterate over the list of dates
for year, month, day in date_list:

    vs = nc.Dataset("./data/vs_" + str(year) + ".nc")
    th = nc.Dataset("./data/th_" + str(year) + ".nc")
    days_btwn = date(year, month, day) - date(year, 1, 1)
    days_btwn = days_btwn.days

    # Extract and preprocess data
    wind_speed = vs["wind_speed"][days_btwn, :, :]
    wind_dir = th["wind_from_direction"][days_btwn, :, :]
    lon = vs["lon"][:]
    lat = vs["lat"][:]

    
    # Calculate u and v wind components
    wind_u = wind_speed * np.cos(np.deg2rad(wind_dir))
    wind_v = wind_speed * np.sin(np.deg2rad(wind_dir))

    # Sampling for better visualization
    sample_interval = 25
    wind_u_sampled = wind_u[::sample_interval, ::sample_interval]
    wind_v_sampled = wind_v[::sample_interval, ::sample_interval]
    wind_speed_sampled = wind_speed[::sample_interval, ::sample_interval]
    lon_sampled = lon[::sample_interval]
    lat_sampled = lat[::sample_interval]

    # Create figure and axes for side-by-side plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(32, 8))

    # Plot 1: Different lengths based on magnitude
    magnitude = wind_speed_sampled
    q1 = ax1.quiver(lon_sampled, lat_sampled, wind_u_sampled, wind_v_sampled, 
                    magnitude, cmap="viridis", scale=150, width=0.003, headwidth=3)
    fig.colorbar(q1, ax=ax1, label="Wind Speed (m/s)")
    ax1.set_title(f"Different Lengths ({year}-{month:02d}-{day:02d})", fontsize=14)
    ax1.set_xlabel("Longitude", fontsize=12)
    ax1.set_ylabel("Latitude", fontsize=12)

    # Plot 2: Same lengths for all vectors
    normalized_wind_u = wind_u_sampled / magnitude
    normalized_wind_v = wind_v_sampled / magnitude

    levels = 20
    c2 = ax2.contourf(lon_sampled, lat_sampled, wind_speed_sampled, levels)
    ax2.quiver(lon_sampled, lat_sampled, normalized_wind_u, normalized_wind_v, 
                    cmap="viridis", scale=50)
    fig.colorbar(c2, ax=ax2, label="Wind Speed (m/s)")
    ax2.set_title(f"Same Lengths ({year}-{month:02d}-{day:02d})", fontsize=14)
    ax2.set_xlabel("Longitude", fontsize=12)
    ax2.set_ylabel("Latitude", fontsize=12)

    plt.tight_layout()

    # Save plot as image
    frame_path = f"./frames/frame_{year}_{month:02d}_{day:02d}.png"
    plt.savefig(frame_path)
    frames.append(Image.open(frame_path))
    plt.close(fig)

# Create a GIF
gif_path = "./wind_animation.gif"
frames[0].save(gif_path, format="GIF", append_images=frames[1:], save_all=True, duration=500, loop=0)
print(f"GIF saved to {gif_path}")

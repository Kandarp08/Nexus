import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import netCDF4 as nc

# Opening the dataset and initializing relevant variables such as latitudes, longitudes, 
# and days

ds = nc.Dataset("../extracted_data.nc")

lat = ds["lat"][:]
lon = ds["lon"][:]
day = ds["day"][:]

# Dates corresponding to the data samples
dates = ["10th Nov 2023", "20th Nov 2023", "30th Nov 2023", "10th Dec 2023", "20th Dec 2023", "30th Dec 2023", 
         "10th Jan 2024", "20th Jan 2024", "30th Jan 2024"]

# We now plot contour plots for several combinations of variables. 
# A GIF is created using 9 data samples, and stored in the GIFs folder. 
# The code saves an image for each plot that is generated. 
# However, only those images are stored in the Images folder that are used in the report. Rest of the images are deleted.

# Code Overview:
# 1. The animate function is used to plot the contour maps at different instances of time.
# 2. Figures are saved for each plot (Most of the figures are later deleted)
# 3. Colorbar is initialized in the beginning, and not changed throughout the GIF.

# PRECIPITATION AMOUNT AND SPECIFIC HUMIDITY

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()
    
    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    pr = ds["pr"][i]
    sph = ds["sph"][i]

    contour_pr = ax.contourf(lon, lat, pr, cmap="viridis_r")
    ax.contour(contour_pr, levels=contour_pr.levels[:], colors="k", linewidths=0.4)

    contour_sph = ax.contour(lon, lat, sph, cmap="gray")
    ax.clabel(contour_sph, inline=True, colors="red")

    fig.savefig(f"./Images/pr_sph_{i}.png")

contour_pr = ax.contourf(lon, lat, ds["pr"][0], cmap="viridis_r")
ax.contour(contour_pr, levels=contour_pr.levels[:], colors="k", linewidths=0.4)

cbar = plt.colorbar(contour_pr, ax=ax)
cbar.set_label("Precipitation amount (mm)")

contour_sph = ax.contourf(lon, lat, ds["sph"][0], cmap="gray")
ax.clabel(contour_sph, inline=True, colors="red")

cbar = plt.colorbar(contour_sph, ax=ax)
cbar.set_label("Specific humidity (Mass fraction)")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/pr_sph.gif")

# AVERAGE TEMPERATURE AND AVERAGE RELATIVE HUMIDITY

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()

    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    tmin = ds["tmmn"][i]
    tmax = ds["tmmx"][i]
    rhmin = ds["rmin"][i]
    rhmax = ds["rmax"][i]

    # Calculate average temperature and average relative humidity
    tavg = (tmin + tmax) / 2 - 273.15 
    ravg = (rhmin + rhmax) / 2

    contour_tmp = ax.contourf(lon, lat, tavg, cmap="Wistia")
    ax.contour(contour_tmp, levels=contour_tmp.levels[:], colors="k", linewidths=0.4)

    contour_r = ax.contour(lon, lat, ravg, cmap="cool", linewidths=0.8)
    ax.clabel(contour_r, inline=True, colors="black")
    
    fig.savefig(f"./Images/rh_tmp_{i}.png")
    
contour_tmp = ax.contourf(lon, lat, (ds["tmmn"][0] + ds["tmmx"][0]) / 2 - 273.15, cmap="Wistia")
ax.contour(contour_tmp, levels=contour_tmp.levels[:], colors="k", linewidths=0.4)

contour_r = ax.contourf(lon, lat, (ds["rmin"][0] + ds["rmax"][0]) / 2, cmap="cool")
ax.clabel(contour_r, inline=True, colors="black")

cbar = plt.colorbar(contour_tmp, ax=ax)
cbar.set_label("Average Temperature (\u2103)")

cbar = plt.colorbar(contour_r, ax=ax)
cbar.set_label("Average Relative Humidity (%)")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/rh_tmp.gif")

# BURNING INDEX AND DEAD FUEL MOISTURE (100-HOUR)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()

    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    bi = ds["bi"][i]
    dfm = ds["fm100"][i]

    contour_bi = ax.contourf(lon, lat, bi, cmap="Oranges")
    ax.contour(contour_bi, levels=contour_bi.levels[:], colors="k", linewidths=0.4)

    contour_dfm = ax.contour(lon, lat, dfm, cmap="Greens", linewidths=0.8)
    ax.clabel(contour_dfm, inline=True, colors="black")

    fig.savefig(f"./Images/bi_dfm100_{i}.png")

contour_bi = ax.contourf(lon, lat, ds["bi"][0], cmap="Oranges")
ax.contour(contour_bi, levels=contour_bi.levels[:], colors="k", linewidths=0.4)

contour_dfm = ax.contourf(lon, lat, ds["fm100"][0], cmap="Greens")
ax.clabel(contour_dfm, inline=True, colors="black")

cbar = plt.colorbar(contour_bi, ax=ax)
cbar.set_label("Burning Index (NFDRS fire danger index)")

cbar = plt.colorbar(contour_dfm, ax=ax)
cbar.set_label("Dead Fuel Moisture (100-hour)")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/bi_dfm100.gif")

# BURNING INDEX AND DEAD FUEL MOISTURE (1000-HOUR)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()

    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    bi = ds["bi"][i]
    dfm = ds["fm1000"][i]

    contour_bi = ax.contourf(lon, lat, bi, cmap="Oranges")
    ax.contour(contour_bi, levels=contour_bi.levels[:], colors="k", linewidths=0.4)

    contour_dfm = ax.contour(lon, lat, dfm, cmap="Greens", linewidths=0.8)
    ax.clabel(contour_dfm, inline=True, colors="black")

    fig.savefig(f"./Images/bi_dfm1000_{i}.png")

contour_bi = ax.contourf(lon, lat, ds["bi"][0], cmap="Oranges")
ax.contour(contour_bi, levels=contour_bi.levels[:], colors="k", linewidths=0.4)

contour_dfm = ax.contourf(lon, lat, ds["fm1000"][0], cmap="Greens")
ax.clabel(contour_dfm, inline=True, colors="black")

cbar = plt.colorbar(contour_bi, ax=ax)
cbar.set_label("Burning Index (NFDRS fire danger index)")

cbar = plt.colorbar(contour_dfm, ax=ax)
cbar.set_label("Dead Fuel Moisture (1000-hour)")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/bi_dfm1000.gif")

# MEAN VAPOR PRESSURE DEFICIT, AVERAGE TEMPERATURE, AND AVERAGE RELATIVE HUMIDITY

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()

    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    vpd = ds["vpd"][i]
    tmin = ds["tmmn"][i]
    tmax = ds["tmmx"][i]
    rmin = ds["rmin"][i]
    rmax = ds["rmax"][i]

    tavg = (tmin + tmax) / 2 - 273.15
    ravg = (rmin + rmax) / 2
    ratio = tavg / ravg

    contour_vpd = ax.contourf(lon, lat, vpd, cmap="viridis_r")
    ax.contour(contour_vpd, levels=contour_vpd.levels[:], colors="k", linewidths=0.4)

    contour_ratio = ax.contour(lon, lat, ratio, cmap="Reds", linewidths=0.7)
    ax.clabel(contour_ratio, inline=True, colors="black")

    fig.savefig(f"./Images/vpd_temp_rh_{i}.png")
        
contour_vpd = ax.contourf(lon, lat, ds["vpd"][0], cmap="viridis_r")
ax.contour(contour_vpd, levels=contour_vpd.levels[:], colors="k", linewidths=0.4)
    
tavg = (ds["tmmn"][0] + ds["tmmx"][0]) / 2 - 273.15
ravg = (ds["rmin"][0] + ds["rmax"][0]) / 2
ratio = tavg / ravg

contour_ratio = ax.contourf(lon, lat, ratio, cmap="Reds")
ax.clabel(contour_ratio, inline=True, colors="black")

cbar = plt.colorbar(contour_vpd, ax=ax)
cbar.set_label("Mean Vapor Pressure Deficit (kPa)")

cbar = plt.colorbar(contour_ratio, ax=ax)
cbar.set_label("Temperature (\u2103) / Relative Humidity")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/vpd_temp_rh.gif")

# DEAD FUEL MOISTURE (1000-HOUR) AND AVERAGE TEMPERATURE

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()

    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    dfm = ds["fm1000"][i]
    tavg = (ds["tmmn"][i] + ds["tmmx"][i]) / 2 - 273.15

    contour_dfm = ax.contourf(lon, lat, dfm, cmap="Greens")
    ax.contour(contour_dfm, levels=contour_dfm.levels[:], colors="k", linewidths=0.4)

    contour_temp = ax.contour(lon, lat, tavg, cmap="Oranges", linewidths=0.7)
    ax.clabel(contour_temp, inline=True, colors="red")

    fig.savefig(f"./Images/dfm1000_temp_{i}.png")
        
tavg = (ds["tmmn"][0] + ds["tmmx"][0]) / 2 - 273.15

contour_dfm = ax.contourf(lon, lat, ds["fm1000"][0], cmap="Greens")
contour_temp = ax.contourf(lon, lat, tavg, cmap="Oranges")

cbar = plt.colorbar(contour_dfm, ax=ax)
cbar.set_label("Dead Fuel Moisture (1000-hour)")

cbar = plt.colorbar(contour_temp, ax=ax)
cbar.set_label("Average Temperature (\u2103)")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/dfm1000_temp.gif")

# DEAD FUEL MOISTURE (1000-HOUR) AND AVERAGE RELATIVE HUMIDITY

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()

    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    dfm = ds["fm1000"][i]
    ravg = (ds["rmin"][i] + ds["rmax"][i]) / 2

    contour_dfm = ax.contourf(lon, lat, dfm, cmap="Greens")
    ax.contour(contour_dfm, levels=contour_dfm.levels[:], colors="k", linewidths=0.4)

    contour_r = ax.contour(lon, lat, ravg, cmap="cool", linewidths=0.7)
    ax.clabel(contour_r, inline=True, colors="red")

    fig.savefig(f"./Images/dfm1000_rh_{i}.png")
        
ravg = (ds["rmin"][0] + ds["rmax"][0]) / 2

contour_dfm = ax.contourf(lon, lat, ds["fm1000"][0], cmap="Greens")
contour_temp = ax.contourf(lon, lat, tavg, cmap="cool")

cbar = plt.colorbar(contour_dfm, ax=ax)
cbar.set_label("Dead Fuel Moisture (1000-hour)")

cbar = plt.colorbar(contour_temp, ax=ax)
cbar.set_label("Relative Humidity (%)")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/dfm1000_rh.gif")

# DEAD FUEL MOISTURE (1000-HOUR) AND PRECIPITATION AMOUNT

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()

    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    dfm = ds["fm1000"][i]
    pr = ds["pr"][i]

    contour_dfm = ax.contourf(lon, lat, dfm, cmap="Greens")
    ax.contour(contour_dfm, levels=contour_dfm.levels[:], colors="k", linewidths=0.4)

    contour_pr = ax.contour(lon, lat, pr, cmap="Reds_r")
    ax.clabel(contour_pr, inline=True, colors="yellow")

    fig.savefig(f"./Images/dfm1000_pr_{i}.png")
        
contour_dfm = ax.contourf(lon, lat, ds["fm1000"][0], cmap="Greens")
contour_pr = ax.contourf(lon, lat, ds["pr"][0], cmap="Reds_r")

cbar = plt.colorbar(contour_dfm, ax=ax)
cbar.set_label("Dead Fuel Moisture (1000-hour)")

cbar = plt.colorbar(contour_pr, ax=ax)
cbar.set_label("Precipitation amount (mm)")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/dfm1000_pr.gif")

# DEAD FUEL MOISTURE (1000-HOUR) AND SURFACE DOWNWARD SHORTWAVE RADIATION

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

def animate(i):

    ax.clear()

    ax.set_title(dates[i])
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    dfm = ds["fm1000"][i]
    srad = ds["srad"][i]

    contour_dfm = ax.contourf(lon, lat, dfm, cmap="Greens")
    ax.contour(contour_dfm, levels=contour_dfm.levels[:], colors="k", linewidths=0.4)

    contour_srad = ax.contour(lon, lat, srad, cmap="Wistia_r")
    ax.clabel(contour_srad, inline=True, colors="red")

    fig.savefig(f"./Images/dfm1000_srad_{i}.png")
        
contour_dfm = ax.contourf(lon, lat, ds["fm1000"][0], cmap="Greens")
contour_srad = ax.contourf(lon, lat, ds["srad"][0], cmap="Wistia_r")

cbar = plt.colorbar(contour_dfm, ax=ax)
cbar.set_label("Dead Fuel Moisture (1000-hour)")

cbar = plt.colorbar(contour_srad, ax=ax)
cbar.set_label("Surface downward shortwave radiation (W/m\u00b2)")

anim = FuncAnimation(fig, animate, frames=9)
anim.save("./GIFs/dfm1000_srad.gif")


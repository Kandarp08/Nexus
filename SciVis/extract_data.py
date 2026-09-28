# Importing libraries

import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr
import os

# Initialize dimensions for xarray dataset

ds = nc.Dataset("./Dataset/bi_2023.nc")

lat = ds["lat"][:]
lon = ds["lon"][:]

# Day numbers for which data is sampled
days = [45238, 45248, 45258, 45268, 45278, 45288, 45299, 45309, 45319]
req_days = ["2023_313", "2023_323", "2023_333", "2023_343", "2023_353", "2023_363", "2024_9", "2024_19", "2024_29"]

ds.close()

# Get data for each of the sampled days, for each variable

file_list = os.listdir("./Dataset")

var_to_name = {"bi": "burning_index_g", "rmin": "relative_humidity", "rmax": "relative_humidity", "pet": "potential_evapotranspiration", 
               "etr": "potential_evapotranspiration", "pr": "precipitation_amount", "fm1000": "dead_fuel_moisture_1000hr", 
               "fm100": "dead_fuel_moisture_100hr", "sph": "specific_humidity", "srad": "surface_downwelling_shortwave_flux_in_air",
               "th": "wind_from_direction", "tmmn": "air_temperature", "tmmx": "air_temperature", "vpd": "mean_vapor_pressure_deficit",
               "vs": "wind_speed"}

d = {} # Dictionary to store the sampled data

for file in file_list:

    for day in req_days:

        file_year = file[-7:-3]
        day_year = day[:4]
        day_ind = int(day[5:])

        if file_year != day_year:
            continue

        var_name = file[0:-8]

        ds = nc.Dataset(f"./Dataset/{file}") # Open dataset

        # Extract data for a given variable, on a given day
        ar = xr.DataArray(
            data = ds[var_to_name[var_name]][day_ind][:],
            dims = ["lat", "lon"],
            coords = dict(
                lat = (lat),
                lon = (lon),
            )
        )
        
        # Append to dictionary

        if var_name not in d:            
            d[var_name] = [ar]

        else:
            d[var_name].append(ar)

        ds.close()

# Store the data in a new file, named "extracted_data.nc"

lat = np.array(np.ma.getdata(lat))
lon = np.array(np.ma.getdata(lon))
days = np.array(days)

merged = []

for item in d:

    ar = xr.DataArray(
        data = d[item],
        dims = ["day", "lat", "lon"],
        coords = dict(
            lat = (lat),
            lon = (lon),
            day = (days),
        ),
        name=item,
    )
    
    merged.append(ar)

merged = xr.combine_by_coords(merged)

merged.to_netcdf("extracted_data.nc") # Store the file
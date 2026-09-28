<h1>Scientific Visualization</h1>

The period chosen for scientific visualizations is November 2023 - January 2024.

<h2>Folder Structure</h2>

<ol>
    <li>
        Dataset folder contains all the netcdf files that are used for visualizations. Since these files consume a lot of space, the Dataset folder has been kept empty. The files used can be downloaded from https://www.northwestknowledge.net/metdata/data/. 
    </li>
    <li>
        The implementation of different visualization tasks can be found in the respective folders.
    </li>
</ol>

<h2>Extracting Required Data</h2>

The samples used for visualizations are: 10 November 2023, 20 November 2023, 30 November 2023, ..., 30 January 2024. The rationale behind this choice is explained in the report.

To extract the data from the original files for these 9 samples, the file extract_data.py is used. Run it before generating any contour or color plot. The extracted data is stored in the file extracted_data.nc. This file is used for all contour plots and color plots, and not the original files in the Dataset folder.

Prerequisites: Ensure you have Python 3.x, NumPy, Pandas, Matplotlib, NetCDF4, and xarray installed. You can install them using "pip install numpy pandas matplotlib netCDF4 xarray". 

Place the Script and Data: Put the script (extract_data.py) in the directory outside Dataset. Run the Script: Execute the script from the command line using python3 extract_data.py.
from flask import Blueprint, Flask, render_template, send_from_directory
import os
main = Blueprint('main', __name__)

@main.route('/')
def image_extraction():
    return render_template('image_extraction.html')
@main.route('/static/rasters/<municipality>/<year>.tif')
def download_file(municipality, year):
    # Define the path to your rasters directory
    raster_dir = os.path.join(main.root_path, 'static', 'rasters', municipality)
    
    # Define the filename for the requested raster
    filename = f'{year}.tif'
    file_path = os.path.join(raster_dir, filename)

    # Check if the file exists, and return it for download
    if os.path.exists(file_path):
        return send_from_directory(raster_dir, filename, as_attachment=True)
    else:
        return "File not found", 404
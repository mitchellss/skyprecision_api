# Use official ubuntu 18.04 image
FROM ubuntu:18.04

# Adding backend directory to make absolute filepaths consistent across services
WORKDIR '/app'

# Install prequistes for dependencies
RUN apt-get update &&\
    apt-get install -y python3-pip

# GDAL dependencies
RUN apt-get install -y libgdal-dev

# Some monkey-ass commands to get gdal to build. Just don't ask.
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install python package requirements
COPY requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt

# Install monkey-ass-gdal
RUN pip3 install GDAL==`gdal-config --version`

# Copy the rest of the files
COPY . .

# Make port 8000 available for the app
EXPOSE 8000

# Run the backend on 0.0.0.0:8000
CMD python3 manage.py runserver 0.0.0.0:8000
# Use a lightweight base image
FROM python:3.9-slim
RUN pip install psutil

# Copy the Python script to the container
COPY ram_eater.py /ram_eater.py

# Run the Python script on startup
CMD ["python3", "/ram_eater.py"]


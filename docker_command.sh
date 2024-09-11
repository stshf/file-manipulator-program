docker build -t file-manipulator-python3 .
docker run -v $(pwd)/output:/app/output file-manipulator-python3
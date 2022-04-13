echo "Running Uvicorn ASGI in localhost:5000"
uvicorn main:app --port 5000 --host 127.0.0.1 --reload
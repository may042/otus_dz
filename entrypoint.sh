echo "Starting pipeline"
python3 src/pipeline.py -d '\r'

echo "Starting Flask server"
flask run --host=0.0.0.0 --port=5000
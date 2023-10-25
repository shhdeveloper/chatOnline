# import json
# import requests

# # Define your string data and file path
# data = "Your string data"
# file_path = "cyclic_data.json"

# # Save the string cyclically to a JSON file
# try:
#     with open(file_path, 'r') as file:
#         cyclic_data = json.load(file)
# except (FileNotFoundError, json.JSONDecodeError):
#     cyclic_data = []

# cyclic_data.append(data)

# with open(file_path, 'w') as file:
#     json.dump(cyclic_data, file)

# # Load the cyclic data from the file
# with open(file_path, 'r') as file:
#     cyclic_data = json.load(file)

# # Define the URL of your web service
# url = "https://gorgeous-lime-seagull.cyclic.app/api/data"  # Replace with your actual URL

# # Send a POST request with JSON data
# data_to_send = {
#     "cyclic_data": cyclic_data
# }

# response = requests.post(url, json=data_to_send)

# # Check the response
# if response.status_code == 200:
#     print("Data sent successfully")

#     # Retrieve the list of saved data from the response
#     response_data = response.json()
#     saved_data = response_data.get("saved_data", [])
#     print("List of saved data:", saved_data)
# else:
#     print(f"Error: {response.status_code}")





# from flask import Flask, render_template
# from flask_socketio import SocketIO, send

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!123'
# socketio = SocketIO(app, cors_allowed_origins="*")

# @socketio.on('message')
# def handle_message(message):
#     print("Received message:", message)
#     if message != "User connected!":
#         send(message, broadcast=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == "__main__":
#     socketio.run(app, host="localhost", port=5000, debug=True, allow_unsafe_werkzeug=True)

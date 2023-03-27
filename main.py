# import requests
# import base64
# import json
# from secrets import *

# # Step 1 - Authorization 
# url = "https://accounts.spotify.com/api/token"
# headers = {}
# data = {}

# # Encode as Base64
# message = f"{clientId}:{clientSecret}"
# messageBytes = message.encode('ascii')
# base64Bytes = base64.b64encode(messageBytes)
# base64Message = base64Bytes.decode('ascii')


# headers['Authorization'] = f"Basic {base64Message}"
# data['grant_type'] = "client_credentials"

# r = requests.post(url, headers=headers, data=data)

# token = r.json()['access_token']

# # Step 2 - Use Access Token to call playlist endpoint

# playlistId = "myPlaylistId"
# playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
# headers = {
#     "Authorization": "Bearer " + token
# }

# res = requests.get(url=playlistUrl, headers=headers)

# print(json.dumps(res.json(), indent=2))

# ==================


import requests
from urllib.parse import urlencode
import base64
import webbrowser

client_id = "3014ba0ea7e240fa9d36d3e519a5d73f"
client_secret = "90af86f50bd5409ab12d830673d3f2ea"

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:7777/callback",
    "scope": "user-library-read"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

# code = "insert your authorization code here"

# encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

# token_headers = {
#     "Authorization": "Basic " + encoded_credentials,
#     "Content-Type": "application/x-www-form-urlencoded"
# }

# token_data = {
#     "grant_type": "authorization_code",
#     "code": code,
#     "redirect_uri": "http://localhost:7777/callback"
# }
# r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

# token = r.json()["access_token"]

# print(token)

# user_headers = {
#     "Authorization": "Bearer " + token,
#     "Content-Type": "application/json"
# }

# user_params = {
#     "limit": 50
# }

# user_tracks_response = requests.get("https://api.spotify.com/v1/me/tracks", params=user_params, headers=user_headers)

# print(user_tracks_response.json())


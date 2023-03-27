
import requests
import logging
import secret_env as secret

# ========================================

class SpotifyAPI():
    def __init__(self, url='https://accounts.spotify.com/api/token'):
        print('Welcome to the Spotify API')
        self.AUTH_URL=  url 
        self.access_token = self.get_Access_Token()        
        self.BASE_URL = 'https://api.spotify.com/v1/'


# POST
    def get_Access_Token(self):
        try:
            auth_response= requests.post(self.AUTH_URL, {
                'grant_type': 'client_credentials',
                'client_id':secret.CLIENT_ID,
                'client_secret': secret.CLIENT_SECRET,
            })
        except Exception as err:
            print(err)
            logging.info(f'[!Error]:', {err})


        # convert the response to JSON
        auth_response_data = auth_response.json()
        # print(auth_response_data)
        # save the access token
        access_token = auth_response_data['access_token']

        print(access_token)
        return access_token



    def headers(self):
        headers = {
            'Authorization': 'Bearer {token}'.format(token=self.access_token)
        }
        return headers

# actual GET request with proper header

    def get_track_info(self, track_id='6y0igZArWVi6Iz0rj35c1Y'):
        try:
            r = requests.get(self.BASE_URL + 'audio-features/' + track_id, headers=self.headers())
            r= r.json()
            print(r)
            return r
        except Exception as err:
            print(err)
            logging.info(f'[!Error]:', {err})    

    def get_artist_info(self, artist_id='36QJpDe2go2KgaRleHCDTp'):
        try:
            r = requests.get(self.BASE_URL + 'artists/' + artist_id + '/albums', 
                    headers=self.headers(), 
                    params={'include_groups': 'album', 'limit': 50})
            d = r.json()
            # print(d)

            for album in d['items']:
                print(album['name'], ' --- ', album['release_date'])
        except Exception as err:
            print(err)
            logging.info(f'[!Error]:', {err})
        # return d

    def main(self):
        self.get_Access_Token()
        self.get_track_info()
        self.get_artist_info()
        

obj = SpotifyAPI()
obj.main()

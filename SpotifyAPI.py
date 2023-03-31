
import requests
import logging
import secret_env as secret
from pprint import pprint

# ========================================

class SpotifyAPI():
    def __init__(self, url='https://api.spotify.com/v1/'):
        # print("\n=============================================")
        self.AUTH_URL=  'https://accounts.spotify.com/api/token'
        self.access_token = self.get_Access_Token()     
        # self.access_token = self.check_access_token_expiry()    
        self.BASE_URL = url


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
        # print("\n=============================================\n")
        # print('Access Token',access_token)
        # print("\n=============================================\n\n")
        return access_token

    # def check_access_token_expiry(self):
    #     if access_token:
    #         return 
    #     else:
    #         self.get_Access_Token()


    def headers(self):
        headers = {
            'Authorization': 'Bearer {token}'.format(token=self.access_token)
        }
        # print('header', headers)
        return headers

# actual GET request with proper header

    def get_track_info(self, track_id='11dFghVXANMlKmJXsNCbNl'):
        try:
            r = requests.get(self.BASE_URL + 'tracks/' + track_id, headers=self.headers())
            d= r.json()
            print("=============== get_track_info for ", track_id, "==============================\n")
            
            print('name: ' ,d['album']['name'])
            print('release_date: ' ,d['album']['release_date'])
            n= len(d['album']['artists'])
            for x in range(n):
                print('Artist: ', d['album']['artists'][x]['name'])
            print('duration_ms: ' ,d['duration_ms'])
            print('Link: ' ,d['album']['href'])
            # print("\n=============================================\n\n")
            return r
        except Exception as err:
            print(err)
            logging.info(f'[!Error]:', {err})    


    # not working-- {'error': {'status': 401, 'message': 'Missing token'}}
    # def get_user_saved_albums(self):
    #     try:
    #         r = requests.get(self.BASE_URL + 'me/albums/', 
    #                 headers=self.headers())
    #                 # params={'limit':10, 'offset':5, 'market':'ES'})
    #         r= r.json()
    #         print("\n===========USER'S SAVED ALBUMS==================================\n\n")
    #         print(r)
    #         # print("\n=============================================\n\n")
    #         # return r
    #     except Exception as err:
    #         print(err)
    #         logging.info(f'[!Error]:', {err})    

    # {'error': {'status': 401, 'message': 'Unauthorized.'}}---- /me related queries getting error
    # def curr_user_profile(self):
    #     try:
    #         r = requests.get(self.BASE_URL + 'me/', 
    #                 headers=self.headers())
    #                 # params={'limit':10, 'offset':5, 'market':'ES'})
    #         r= r.json()
    #         print("\n===========curr_user_profile==================================\n\n")
    #         print(r)
    #         # print("\n=============================================\n\n")
    #         # return r
    #     except Exception as err:
    #         print(err)
    #         logging.info(f'[!Error]:', {err})    


    def search_for_item(self, query='duaa', category='track' ):
        try:
            r = requests.get(self.BASE_URL + 'search/', 
                    headers=self.headers(),
                    params={'q':query, 'type':category  ,'limit':10, 'offset':5, 'market':'ES'})
            d= r.json()
            print("\n===========showing results for ",query, "==================================\n\n")
            # print(type(d['tracks']['items']))
            # pprint(d['tracks']['items'][0])
            # print(d['tracks']['items'][0].keys())
            print('link: ', d['tracks']['items'][0]['href'])
            print('name: ', d['tracks']['items'][0]['name'])
            print('Type: ', d['tracks']['items'][0]['type'])
            n= len(d['tracks']['items'][0]['artists'])
            for x in range(n):
                print('Artist: ', d['tracks']['items'][0]['artists'][x]['name'])
            print('duration: ', d['tracks']['items'][0]['duration_ms'], 'millisec')
            # print(d)
            # return 

            # print("\n=============================================\n\n")
            # return r
        except Exception as err:
            print(err)
            logging.info(f'[!Error]:', {err})    

    def get_album(self, album_id= '4aawyAB9vmqN3uQ7FjRGTy'):
        try:
            r = requests.get(self.BASE_URL + 'albums/'+ album_id, 
                    headers=self.headers())
                    # params={'limit':10, 'offset':5, 'market':'ES'})
            d= r.json()
            print("\n====SHOWING DETAILS FOR ALBUM ID: ",album_id, "==================================\n")
            # pprint(r)
            # print(type(d))
            # print(d.keys())
            # pprint(d[0])
            print('name', '-----', d['name'])
            print('id', '-----',d['id'])
            print('Link', '-----',d['href'])
            print('release_date', '-----',d['release_date'])
            print('album_type', '-----',d['album_type'])
            print('genres', '-----',d['genres'])
            print('total_tracks', '-----',d['total_tracks'])

            # for x,y in d.items():
            #     print(x, '----', y)
            # print(d.keys())
            # break
            print("\n=============================================\n\n")
            # return r
        except Exception as err:
            print(err)
            logging.info(f'[!Error]:', {err})    


    def get_artist_info(self, artist_id='36QJpDe2go2KgaRleHCDTp'):
        try:
            r = requests.get(self.BASE_URL + 'artists/' + artist_id + '/albums', 
                    headers=self.headers(), 
                    params={'include_groups': 'album', 'limit': 50})
            d = r.json()
            # pprint(d)
            # print(d.keys())
            # print(d['items'].keys())
            # pprint(d['items'][0])
            # print(type(d['items']))
            print("\n===========Showing Album Name & Release date for artist id", artist_id, "===========\n")
            for album in d['items']:
                print(album['name'], ' --- ', album['release_date'])
        except Exception as err:
            print(err)
            logging.info(f'[!Error]:', {err})
        # return d

if __name__ == "__main__":
    print('Welcome to the Spotify API')
    obj = SpotifyAPI()
    obj.get_Access_Token()
    obj.get_track_info()
    obj.search_for_item()
    obj.get_album()
    obj.get_artist_info()

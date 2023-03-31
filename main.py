import SpotifyAPI as sapi
api= sapi.SpotifyAPI()

print("Welcome to Spotify API")
print("Enter '1' for search: ")
print("Enter '2' to get any track info: ")
print("Enter '3' to get album: ")
print("Enter '4' to get any artist info: ")
response= int(input("ENTER YOUR RESPONSE:"))

if response==1:
    cat= input("Enter category: ")
    que= input("Enter query: ")
    if cat != "" and que != "":
        api.search_for_item( category=cat, query=que)
    else:
        api.search_for_item()
    
elif response==2:
    cat= input("Enter track id: ")
    if cat != "" :
        api.get_track_info(track_id=cat)
    else:
        api.get_track_info()

elif response==3:
    cat= input("Enter album id: ")
    if cat != "" :
        api.get_album(album_id=cat)
    else:
        api.get_album()

elif response==4:
    cat= input("Enter artist id: ")
    
    if cat != "" :
        api.get_artist_info(artist_id=cat)
    else:
        api.get_artist_info()
    

else:
    print("Enter a valid option")







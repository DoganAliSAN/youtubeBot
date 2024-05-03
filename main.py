from support import Support
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
scopes = ["https://www.googleapis.com/auth/youtube.upload","https://www.googleapis.com/auth/youtube.force-ssl","https://www.googleapis.com/auth/youtube.readonly"]
sup = Support("keys.ini")
youtube_key = sup.read_config("KEYS", "youtube_data_v3_key")
oauth2_secret = sup.read_config("KEYS", "oauth2_client_secret")
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file("client.json",scopes)
credentials = flow.run_console()
client = build("youtube", "v3", developerKey=youtube_key)
client_oauth = build("youtube", "v3", credentials=credentials)
channelinfo = client_oauth.channels().list(
  part="contentDetails",
  id="UCvEwBdLSUT1YVQPxB4SEc1w"
).execute()

print(client.playlistItems().list(
  part="snippet",
  playlistId=channelinfo["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"],
  maxResults = 25
).execute())
# videoinfo = client_oauth.videos().insert(
#    part="snippet,status",
#    body={"snippet":{"title":"This is my test video","categoryId":"22","description":"This is a test video for my code"},"status":{"privacyStatus":"public"}},
#    media_body = MediaFileUpload("youtubetestvideo.mov")).execute()
# comment = client_oauth.commentThreads().insert(
#     part="snippet",
#     body={
#           "snippet": {
#             "topLevelComment": {
#               "snippet": {
#                 "textOriginal": "This is a software test"
#               }
#             },
#             "videoId": "Ok36t5CCERc"
#           }
#         }
#     ).execute()
# print("Comment id test 1:",comment["id"])
# comment_reply = client_oauth.comments().insert(
#   part="snippet",
#   body={
#     "snippet":{
#       "parentId":comment["id"],
#       "textOriginal":"This is a software reply"
#       }
#   }
# ).execute()
#client_oauth.comments().delete(id="Ugy-rnSOzBDwfxS2-YN4AaABAg").execute()

# print(client.commentThreads().list(
#     part="snippet",
#     videoId="Ok36t5CCERc", #videoinfo["id"],
#     maxResults=100
# ).execute())
#print(client.channels().list(part="statistics",id="UCeUHlEwQOX8FNqcuVyM83_w").execute())
""" print(client_oauth.videos().insert(
    part="snippet,status",
    body={"snippet":{"title":"This is my test video","categoryId":"22","description":"This is a test video for my code"},"status":{"privacyStatus":"private"}},
    media_body = MediaFileUpload("youtubetestvideo.mov")).execute()) # to use this function youtube requires a QAuth3 access token instead of v3 data key
 """

# print(client_oauth.videos().delete(id="4eyd1DxCpP0").execute())

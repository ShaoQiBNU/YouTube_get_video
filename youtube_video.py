# -*- coding: utf-8 -*-
# function: get video url from youtube based on search query

from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyDhkgPCy2hncXO48_MJq3gyA0MFwMV4Wv4"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # more parameters setting can be found in https://developers.google.com/youtube/v3/docs/search/list
  search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order=order,
    part="id,snippet",
    videoDuration='short',
    maxResults=max_results,
    location=location,
    locationRadius=location_radius
  ).execute()

  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result)
  try:
      nexttok = search_response["nextPageToken"]
      return(nexttok, videos)
  except Exception as e:
      nexttok = "last_page"
      return(nexttok, videos)


def geo_query(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet, recordingDetails, statistics'

    ).execute()

    return video_response
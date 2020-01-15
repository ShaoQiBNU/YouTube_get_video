# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    ## please see the link: https://developers.google.com/youtube/v3/docs to get more ways to use this API
    ## search query
    # API only allow maxResults in range [0, 50]
    request = youtube.search().list(
        q='cat',
        type="video",
        part="id,snippet",
        maxResults=50
    )

    ## videoId
    # API only allow maxResults in range [0, 50]
    request = youtube.videos().list(
        part="snippet, contentDetails, recordingDetails, localizations, statistics",
        id="Ks-_Mh1QhMc,c0KYU2j0TM4,eIho2S0ZahI"
    )

    response = request.execute()
    print(response)

    ## get video info
    videos = []
    for search_result in response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    print(videos)


if __name__ == "__main__":
    main()

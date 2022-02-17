#this is all about threading
import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')





# async example:
import aiohttp
import asyncio
import requests
import time

from key import key

start_time = time.time()

channel_id = 'UC-QDfvrRIDB6F0bIO4I4HkQ'

url = f'https://www.googleapis.com/youtube/v3/channels?id={channel_id}&key={key}&part=contentDetails'
r = requests.get(url)
results = r.json()['items']

playlist_id = results[0]['contentDetails']['relatedPlaylists']['uploads']

url = f'https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist_id}&key={key}&part=contentDetails&maxResults=50'

video_ids = []
while True:
    r = requests.get(url)
    results = r.json()
    if 'nextPageToken' in results:
        nextPageToken = results['nextPageToken']
    else:
        nextPageToken = None

    if 'items' in results:
        for item in results['items']:
            videoId = item['contentDetails']['videoId']
            video_ids.append(videoId)

    if nextPageToken:
        url = f'https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist_id}&pageToken={nextPageToken}&key={key}&part=contentDetails&maxResults=50'
    else:
        break



'''
view_counts = []
for video_id in video_ids:
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={key}&part=statistics'
    r = requests.get(url)
    results = r.json()['items']
    viewCount = results[0]['statistics']['viewCount']
    view_counts.append(int(viewCount))
print('Number of videos:', len(view_counts))
print('Average number of views:', sum(view_counts) / len(view_counts))
'''

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for video_id in video_ids:
            task = asyncio.ensure_future(get_video_data(session, video_id))
            tasks.append(task)

        view_counts = await asyncio.gather(*tasks)

    print('Number of videos:', len(view_counts))
    print('Average number of views:', sum(view_counts) / len(view_counts))

async def get_video_data(session, video_id):
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={key}&part=statistics'

    async with session.get(url) as response:
        result_data = await response.json()
        results = result_data['items']
        viewCount = results[0]['statistics']['viewCount']
        return int(viewCount)

asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))
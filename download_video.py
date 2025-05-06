import urllib.request

def callback(chunkid, chunk_size, total_size):
    percent = int(100 * chunkid * chunk_size / total_size)
    print(str(percent) + '%')

urllib.request.urlretrieve('https://wbrbr.org/publications/LipschitzPruning/videos/video.mp4', 'LipschitzPruningVideo.mp4', reporthook=callback)

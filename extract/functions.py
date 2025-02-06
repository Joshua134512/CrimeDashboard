from extract.extraction import Extractor
from config import settings
from os import path,curdir

ROOT = path.abspath(curdir)

def download_file(city = None, url = None, file = None):
    if url:
        url = url
    elif city:
        url = settings.data[city]["url"]
    if file:
        filepath = file
    else: 
        ext = 'data/' + city + '.csv'
        filepath = path.join(ROOT, ext)
    with Extractor(url) as extract:
        contents = extract.download_csv()
    with open(filepath, 'w') as writer:
        writer.write(contents)
    return

def download_files():
    download_option = settings.options.download
    if download_option in ['all','new']:
        sources = settings.data
        for key in sources:
            ext = 'data/' + key + '.csv'
            file = path.join(ROOT, ext)
            if download_option == 'all':
                print(f"Downloading {key} data file")
                url = settings.data[key]["url"]
                download_file(None, url, file)
            elif download_option == 'new':
                if path.exists(file):
                    print(f"{key} data file already downloaded: Skipping")
                else:
                    print(f"Downloading {key} data file")
                    url = settings.data[key]["url"]
                    download_file(None, url, file)
        print("Downloads complete")

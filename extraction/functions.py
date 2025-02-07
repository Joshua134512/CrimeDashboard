from extraction.extractor import Extractor
from config import settings
from os import path,curdir,makedirs

ROOT = path.abspath(curdir)

def download_file(url: str, filepath: str, **_):
    with Extractor(url) as extract:
        contents = extract.download_csv()
    with open(filepath, 'w') as writer:
        writer.write(contents)
    return

def download_files(**kwargs):
    download_option = kwargs.get('download_option') or 'all'
    source = kwargs.get('source') or 'data'
    files = settings[source]
    for key in files:
        file = key + '.csv'
        folderpath = path.join(ROOT, source)
        if not path.exists(folderpath):
            makedirs(folderpath)
        filepath = path.join(folderpath, file)
        if download_option == 'all':
            print(f"Downloading {key} data file")
            url = settings.data[key]["url"]
            download_file(url, filepath)
        elif download_option == 'new':
            if path.exists(file):
                print(f"{key} data file already downloaded: Skipping")
            else:
                print(f"Downloading {key} data file")
                url = settings.data[key]["url"]
                download_file(None, url, file)
    print("Downloads complete")

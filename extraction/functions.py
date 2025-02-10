from extraction.Extractor import Extractor
from config import settings
from os import path,curdir,makedirs

ROOT = path.abspath(curdir)

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def download_file(url: str, filepath: str, **_):
    with Extractor(url) as extract:
        contents = extract.download_csv()
    with open(filepath, 'w') as writer:
        writer.write(contents)
    return

def download_files(url, folder, **_):
    api_key = settings.fbi.key
    folderpath = path.join(ROOT, "data", folder)
    if not path.exists(folderpath):
        makedirs(folderpath)
    for state in STATES:
        print(f"Downloading {state} {folder} data")
        url = url.format(state = state, api_key = api_key)
        file = f"{state}.csv"
        download_file(url, path.join(folderpath, file))
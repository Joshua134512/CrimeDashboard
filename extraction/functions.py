from config import settings
from os import path,curdir,makedirs
from connectors.Extractor import Extractor

ROOT = path.abspath(curdir)

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def download_file(url: str, filepath: str, **_):
    with Extractor(url) as e:
        data = e.get_file()
    with open(filepath, 'wb') as writer:
        writer.write(data)
    return

def download_files(url: str, folder, **kwargs):
    kwargs['api_key']  = settings.fbi.key
    folderpath = path.join(ROOT, "data", "working", folder)
    if not path.exists(folderpath):
        makedirs(folderpath)
    for state in STATES:
        print(f"Downloading {state} {folder} data")
        kwargs['state'] = state
        stateurl = url.format(**kwargs)
        file = f"{state}.json"
        download_file(stateurl, path.join(folderpath, file))


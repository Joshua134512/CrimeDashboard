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

def download_files(url, folder, **_):
    api_key = settings.fbi.key
    folderpath = path.join(ROOT, "data", folder)
    if not path.exists(folderpath):
        makedirs(folderpath)
    for state in STATES:
        print(f"Downloading {state} {folder} data")
        url = url.format(state = state, api_key = api_key)
        file = f"{state}.json"
        download_file(url, path.join(folderpath, file))

def file_to_table(filepath, table, database = "test.db", **_):
    filepath = 'https://api.usa.gov/crime/fbi/cde/shr/state/IA?type=counts&from=01-2024&to=12-2024&API_KEY=t3R5zKm1TXbzF8aq9x3NUmUhRxBqOMk2dwP7fomd'
    with Extractor(filepath) as e:
        e.to_sql(table, database)
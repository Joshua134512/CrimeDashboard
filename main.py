from extract.extraction import Extractor
from config import settings

def main(update = True):
    if update == True:
        sources = settings.data
        for key in sources:
            with Extractor(key, None) as ext:
                ext.writeToFile()
    return

if __name__ == '__main__':
    main()
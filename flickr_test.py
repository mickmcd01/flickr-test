import sys
import argparse
import flickrapi


def sort_func(photo):
    return int(photo['views'])


def process_album(flickr, album):
    sets = flickr.photosets.getList()
    photosets = sets['photosets']['photoset']
    for set in photosets:
        if set['title']['_content'].lower() == album.lower():
            photoset = flickr.photosets.getPhotos(photoset_id=set['id'], extras='views', per_page=200)
            photos = photoset['photoset']['photo']
            photos = sorted(photos, key=sort_func)
            for photo in photos:
                print 'Views: %d, Title/ID: %s %s' % (int(photo['views']), photo['title'], photo['id'])
            print 'Total number of photos in the album %d' % len(photos)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyfile', help='Path to keyfile (defaults to ./flickr_keys.txt)')
    parser.add_argument('--album', help='The album to process')
    args = parser.parse_args()

    if not args.album:
        print 'The album name must be specified'
        sys.exit()

    if args.keyfile:
        keyfile = args.keyfile
    else:
        keyfile = './flickr_keys.txt'

    with open(keyfile) as f:
        key_info = f.readlines()

    api_key = key_info[0].strip()
    api_secret = key_info[1].strip()

    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    flickr.authenticate_via_browser(perms='read')

    process_album(flickr, args.album)

if __name__ == "__main__":
    main()

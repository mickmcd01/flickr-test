import sys
import argparse
import flickrapi
import settings


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
            total_views = 0
            for photo in photos:
                print 'Views: %d, Title/ID: %s %s' % (int(photo['views']), photo['title'], photo['id'])
                total_views += int(photo['views'])
            print 'Total number of photos in the album %d' % len(photos)
            print 'Total number of views for pictures in the album %d' % total_views
            break
    else:
        print 'Album "%s" was not found.' % album


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--album', help='The album to process')
    args = parser.parse_args()

    if not args.album:
        print 'The album name must be specified'
        sys.exit()

    flickr = flickrapi.FlickrAPI(settings.flickr_api_key, settings.flickr_secret, format='parsed-json')
    flickr.authenticate_via_browser(perms='read')

    process_album(flickr, args.album)

if __name__ == "__main__":
    main()

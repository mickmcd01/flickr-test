import flickrapi

with open('./flickr_keys.txt') as f:
    key_info = f.readlines()

api_key = key_info[0].strip()
api_secret = key_info[1].strip()

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
flickr.authenticate_via_browser(perms='read')

sets = flickr.photosets.getList()
print sets
title = sets['photosets']['photoset'][0]['title']['_content']
print title
title = sets['photosets']['photoset'][1]['title']['_content']
print title
photosets = sets['photosets']
print len(photosets)
photosets = sets['photosets']['photoset']
print len(photosets)

for entry in photosets:
    print entry['title']
for entry in photosets:
    print entry['title'], entry['photos'], entry['id']

id = sets['photosets']['photoset'][1]['id']
print id
x = flickr.photosets.getInfo(photoset_id=id)
print x

photos = flickr.photosets.getPhotos(photoset_id=id, extras='views', per_page=3)
print photos
for photo in photos['photoset']['photo']:
    print photo['title'], photo['views'], photo['id']

details = flickr.photos.getInfo(photo_id=photos['photoset']['photo'][2]['id'])
print details

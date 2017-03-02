# flickr-test

usage: flickr_test.py [-h] [--keyfile KEYFILE] [--album ALBUM]

optional arguments:
  -h, --help         show this help message and exit
  --keyfile KEYFILE  Path to keyfile (defaults to ./flickr_keys.txt)
  --album ALBUM      The album to process

keyfile is a file containing 2 lines: the first line is the API key, the second line is the secret. 
if keyfile argument is not present, the file flickr_keys.txt in the current directory is used.

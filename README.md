# fast5purge
Purge a fast5 file or directory of fast5 files from potentially sensitive information:
all of the information in data in UniqueGlobalKey/context_tags and UniqueGlobalKey/tracking_id will be erased.

WARNING:  
Currently modifies fast5 file IN PLACE. You cannot get your original data data back if you do not have a copy.  
I hope to fix this sooner or later, pull requests are very much welcome


```
usage: fast5purge.py [-h] [-d DIR] [-f FILE] [-r]

Remove all sensible content from a fast5

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     directory in which fast5 files have to be purged
  -f FILE, --file FILE  single fast5 file to purge
  -r, --recursive       recursively go through directory
```

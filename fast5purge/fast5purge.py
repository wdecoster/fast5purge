from ont_fast5_api.fast5_file import Fast5File
from argparse import ArgumentParser
import sys
import glob


def main():
    args = get_args()
    if args.file:
        purge(args.file)
    else:
        for filename in glob.iglob(args.dir + '**/*.txt', recursive=args.recursive):
            purge(filename)


def purge(fn):
    f = Fast5File(fn, "r+")
    f.set_tracking_id({"sample_id": "", "ip_address": ""})
    f.add_context_tags({"filename": "", "user_filename_input": ""})
    f.close()


def get_args():
    parser = ArgumentParser(description="Remove sensible content from a fast5 file or directory")
    parser.add_argument("-d", "--dir", help="directory in which fast5 files have to be purged")
    parser.add_argument("-f", "--file", help="single fast5 file to purge")
    parser.add_argument("-r", "--recursive",
                        help="recursively go through directory",
                        action="store_true")
    args = parser.parse_args()
    if not args.dir and not args.file:
        sys.exit("ARGUMENT ERROR: Exactly one of --dir or --file is required")
    if args.dir and args.file:
        sys.exit("ARGUMENT ERROR: Exactly one of --dir or --file is required")
    if args.recursive and args.file:
        sys.exit("ARGUMENT ERROR: -r/--recursive is only applicable when selecting a directory")
    return args


if __name__ == '__main__':
    main()

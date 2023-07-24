import argparse
import aggregator

def parse_arguments():
    parser = argparse.ArgumentParser(description='A simple RSS aggregator.')
    parser.add_argument('--limit', type=int, help='The maximum number of entries to show from each feed.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    entries = aggregator.fetch_entries(aggregator.FEED_URLS, args.limit)
    for entry in entries:
        print(entry)

if __name__ == '__main__':
    main()

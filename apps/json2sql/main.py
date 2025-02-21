import argparse
import json


def parse_json_file(filename: str):
    with open(filename) as json_file:
        return json.load(json_file)

def parse_args():
    parser = argparse.ArgumentParser(
        prog='Json2Sql',
        description='read a JSON file and add data to SQLite database',
        epilog='Text at the bottom of help'
    )
    parser.add_argument('json_file',)
    parser.add_argument('sql_file',)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    parse_json_file(args.json_file)

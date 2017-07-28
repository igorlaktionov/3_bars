import json
import argparse
import math


def load_data(file_path):
    with open(file_path, 'r') as handler:
        return json.load(handler)


def get_biggest_bar(json_data):
    biggest_bar = max(json_data, key=lambda item: item['SeatsCount'])
    return biggest_bar['Name']


def get_smallest_bar(json_data):
    biggest_bar = min(json_data, key=lambda item: item['SeatsCount'])
    return biggest_bar['Name']


def get_distance(bar_coordinates, your_coordinates):
    return math.hypot(bar_coordinates[0] - your_coordinates[0], bar_coordinates[1] - your_coordinates[1])


def get_closest_bar(json_data, longitude, latitude):
    closest_bar = min(json_data, key=lambda item: get_distance(item['geoData']['coordinates'], (longitude, latitude)))
    return closest_bar['Name']


def parser_input_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('-filepath', '-f', dest='file_path', required=True, type=str, help='-filepath=/path/to/file')
    parser.add_argument('--biggest', dest='biggest', action='store_true', help='print biggest bar')
    parser.add_argument('--smallest', dest='smallest', action='store_true', help='print smallest bar')
    parser.add_argument('--closest', dest='closest', action='store_true', help='print closest bar')
    parser.add_argument('-latitude', dest='latitude', type=float, help='-latitude=12.33')
    parser.add_argument('-longitude', dest='longitude', type=float, help='-longitude=66.33')
    return parser.parse_args()


def print_bars(args, json_data):
    if args.biggest:
        print('Biggest bar: ', get_biggest_bar(json_data))
    if args.smallest:
        print('Smallest bar: ', get_smallest_bar(json_data))
    if args.closest:
        if not args.latitude or not args.longitude:
            print('Please write latitude and longitude: -latitude=12 -longitude=13')
        else:
            print('Closest bar: ', get_closest_bar(json_data, args.longitude, args.latitude))


if __name__ == '__main__':
    try:
        args = parser_input_data()
        print_bars(args, load_data(args.file_path))
    except OSError as error:
        print(error)
    except UnicodeDecodeError as error:
        print("Please use the encoding UTF8: %s" % error)
    except ValueError as error:
        print('Invalid json: %s' % error)
    except KeyError as error:
        print('Invalid json key: %s' % error)

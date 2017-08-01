import json
import argparse
import math


def load_data(file_path):
    json_data = None
    try:
        with open(file_path, 'r') as handler:
            json_data = json.load(handler)
    except OSError as error:
        print(error)
    except UnicodeDecodeError as error:
        print("Please use the encoding UTF8: %s" % error)
    except ValueError as error:
        print('Invalid json: %s' % error)
    finally:
        return json_data


def get_biggest_bar(json_data):
    biggest_bar = max(json_data, key=lambda item: item['SeatsCount'])
    return 'Biggest bar: %s' % biggest_bar['Name']


def get_smallest_bar(json_data):
    smallest_bar = min(json_data, key=lambda item: item['SeatsCount'])
    return 'Smallest bar: %s' % smallest_bar['Name']


def get_distance(bar_coordinates, your_coordinates):
    return math.hypot(bar_coordinates[0] - your_coordinates[0], bar_coordinates[1] - your_coordinates[1])


def get_closest_bar(json_data, longitude, latitude):
    closest_bar = min(json_data, key=lambda item: get_distance(item['geoData']['coordinates'], (longitude, latitude)))
    return 'Closest bar: %s' % closest_bar['Name']


def parser_input_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('-filepath', '-f', dest='file_path', required=True, type=str, help='-filepath=/path/to/file')
    parser.add_argument('--biggest', dest='biggest', action='store_true', help='print biggest bar')
    parser.add_argument('--smallest', dest='smallest', action='store_true', help='print smallest bar')
    parser.add_argument('--closest', dest='closest', action='store_true', help='print closest bar')
    parser.add_argument('-latitude', dest='latitude', type=float, help='-latitude=12.33')
    parser.add_argument('-longitude', dest='longitude', type=float, help='-longitude=66.33')
    return parser.parse_args()


def get_bars(json_data, args):
    bars = []
    try:
        if args.biggest:
            bars.append(get_biggest_bar(json_data))
        if args.smallest:
            bars.append(get_smallest_bar(json_data))
        if args.closest:
            bars.append(get_closest_bar(json_data, args.longitude, args.latitude))
    except KeyError as error:
        print('Invalid json key: %s' % error)
    finally:
        return bars


def print_bars(bars):
    if bars:
        for bar in bars:
            print(bar)


def validate_arguments(args):
    if args.closest and (not args.longitude or not args.latitude):
        print('Please write latitude and longitude: -latitude=12 -longitude=13')
        return False
    else:
        return True


if __name__ == '__main__':
    args = parser_input_data()
    json_data = load_data(args.file_path)
    if json_data and validate_arguments(args):
        print_bars(get_bars(json_data, args))

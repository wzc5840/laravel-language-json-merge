import sys
import argparse
import json


def do_merge(json_path_from, json_path_to, out_put_path, language):
    output_dic = {}
    with open(json_path_from, 'r') as load_from:
        load_from_dict = json.load(load_from)
        with open(json_path_to, 'r') as load_to:
            load_to_dict = json.load(load_to)
            # for key_from in load_from_dict:
            #     print('key_from = ' + key_from)
            #     print('key_from = ' + load_from_dict[key_from])
            for key_to in load_to_dict:
                print('key_from = ' + key_to)
                print('key_from = ' + load_to_dict[key_to])


def run(json_path_from, json_path_to, out_put_path, language):
    '''
    コマンド実行
    '''

    print('=============START=============')

    try:
        print('json_path_from = ' + json_path_from)
        print('json_path_to = ' + json_path_to)
        print('out_put_path = ' + out_put_path)
        print('language = ' + language)
        do_merge(json_path_from, json_path_to, out_put_path, language)
    except Exception as e:
        print('merge language json cause expection!!')
        print(e)
    print('==============END==============')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--perform',
        action='store_true',
        help='Perform and run commands',
        required=True)
    parser.add_argument(
        '--json_path_from', help='Merge from', required=True)
    parser.add_argument(
        '--json_path_to', help='Merge to', required=True)
    parser.add_argument(
        '--out_put_path', help='Output to', required=True)
    parser.add_argument(
        '--language', help='Language', required=True)
    args = parser.parse_args()
    print('Command quit!')
    run(json_path_from=args.json_path_from,
        json_path_to=args.json_path_to,
        out_put_path=args.out_put_path,
        out_put_path=args.language)


if __name__ == '__main__':
    sys.exit(main())

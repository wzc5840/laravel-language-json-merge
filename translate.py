import sys
import argparse
import json
import time
from googletrans import Translator


def do_translate(json_path_from, src_language, dest_language):
    output_dic = {}
    with open(json_path_from, 'r') as load_from:
        load_from_dict = json.load(load_from)
        translator = Translator()  
        for key_from in load_from_dict:
            result = translator.translate(
                load_from_dict[key_from], dest=dest_language, src=src_language)
            print('[ ' + src_language + ' ]: ' + load_from_dict[key_from] + '-----> [ ' + dest_language + ' ]: ' + result.text)
            output_dic[key_from] = result.text
            time.sleep(0.5)
        print('result = ')
        print(output_dic)
        with open('output.json', 'w+') as f:
            json.dump(output_dic, f)


def run(json_path_from, src_language, dest_language):
    print('=============START=============')
    try:
        print('json_path_from = ' + json_path_from)
        print('src_language = ' + src_language)
        print('dest_language = ' + dest_language)
        do_translate(json_path_from, src_language, dest_language)
        # lan = detect("你好.")
        # print('lan = ' + lan)
    except Exception as e:
        print('translate json cause expection!!')
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
        '--src_language', help='Source language', required=True)
    parser.add_argument(
        '--dest_language', help='Destination language', required=True)
    args = parser.parse_args()
    print('Command quit!')
    run(json_path_from=args.json_path_from,
        src_language=args.src_language, dest_language=args.dest_language)


if __name__ == '__main__':
    sys.exit(main())

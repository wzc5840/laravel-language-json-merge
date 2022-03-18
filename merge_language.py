import sys
import argparse


def run(json_path_from, json_path_to, out_put_path):
    '''
    コマンド実行
    '''

    print('=============START=============')

    try:
        print('json_path_from = ' + json_path_from)
        print('json_path_to = ' + json_path_to)
        print('out_put_path = ' + out_put_path)
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
        '--out_put_path', help='Merge to', required=True)
    args = parser.parse_args()
    print('Command quit!')
    run(json_path_from=args.json_path_from,
        json_path_to=args.json_path_to,
        out_put_path=args.out_put_path)


if __name__ == '__main__':
    sys.exit(main())

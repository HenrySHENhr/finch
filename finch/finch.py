import sys


def run_cli(arguments=None):
    if arguments is None:
        arguments = sys.argv[1:]
    print('main', arguments)

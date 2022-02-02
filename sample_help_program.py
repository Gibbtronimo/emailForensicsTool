#!/usr/bin/python3
from socket import *
from threading import *
import argparse

def main():
    parser=argparse.ArgumentParser(
    description='''My Description. And what a lovely description it is. ''',
    epilog="""All is well that ends well.""")
    parser.add_argument('--foo', type=int, default=42, help='FOO!')
    parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
    args=parser.parse_args()

main()

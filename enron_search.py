#!/usr/bin/python3
import argparse
import sys

def main():
    try:
        parser=argparse.ArgumentParser(
        usage='enron_search term [term ...]',
        description='Welcome to Forensics Email Analyzer',
        epilog="This program was coded by Tri Nguyen and Ryan Salinas!!")

        #-t for target
        parser.add_argument('search',help='Enter keyword(s) to search in dataset')
        args=parser.parse_args()

        search = str(args.search).split(" ")
        
        for key in search:
            print(key)

        if len(sys.argv)==1:
             parser.print_help()
             parser.exit()


    except KeyboardInterrupt:
        print(Style.RESET_ALL, end ="")
        print("\nExiting the program, goodbye!")
        sys.exit(0)

if (__name__ == "__main__"):
    main()

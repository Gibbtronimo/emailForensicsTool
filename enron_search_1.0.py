#!/usr/bin/python3
import argparse
import sys
import os
import mailbox
import time
from collections import OrderedDict
from email.parser import BytesParser
from email.policy import default


def main():
    try:
        parser=argparse.ArgumentParser(
        usage='enron_search term [term ...]',
        description='Welcome to Forensics Email Analyzer',
        epilog="This program was coded by Tri Nguyen and Ryan Salinas!!")

        
        parser.add_argument('search', nargs='+', help='Enter keyword(s) to search in dataset')
        args=parser.parse_args()

        search_str = str(' '.join(args.search)).split(" ")
        
        for i in range(len(search_str)):
            search_str[i] = search_str[i].lower()
        
        search_clean = list(OrderedDict.fromkeys(search_str))
        
        for search in search_clean:
            print (search)
        
        rootDir='/home/kali/Documents/Digital_Forensics/Enron2mbox/enron'
        for (root,dirs,files) in os.walk(rootDir, topdown=True):
            inbox=files
            mymail = mailbox.mbox(inbox, factory=BytesParser(policy=default).parse)
            for _, message in enumerate(mymail):
                date = message['date']
                print("date:",date)
                to = message['to']
                sender = message['from']
                subject = message['subject']
                messageID = message['Message-ID']
                received = message['received']
                deliveredTo = message['Delivered-To']
                if(messageID == None): continue

                print("Date        :", date)
                print("From        :", sender)
                print("To:         :", to)
                print('Delivered-To:', deliveredTo)
                print("Subject     :", subject)
                print("Message-ID  :", messageID)
            #     print('Received    :', received)

                print("**************************************")





        # if no argument are given, print help screen and exit
        if len(sys.argv)==1:
             parser.print_help()
             parser.exit()

    except KeyboardInterrupt:
        print(Style.RESET_ALL, end ="")
        print("\nExiting the program, goodbye!")
        sys.exit(0)

if (__name__ == "__main__"):
    main()

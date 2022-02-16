#!/usr/bin/python3
import argparse
import sys
import os
import mailbox
import re
from collections import OrderedDict
from email.parser import BytesParser
from email.policy import default

count=0; #global variable to count the total occurence of search strings

# Function print out the header and date of emails that matches all the terms given by the user 
def print_result(self, inboxName):
    global count
    print("INBOX:", inboxName)
    print("-------------------------")
    for message in self:
        print("%d. <%s>, %s" %(count,message['from'], message['date']))
        count+=1;
    print("-------------------------\n")


# Function read parse the mbox and return the body of each email
def read_email_payload(self):
        message = self
        if message.is_multipart():
            content = ''.join(part.get_payload(decode=True) for part in message.get_payload())
        else:
            content = message.get_payload(decode=True)
        return content


def main():
    try:
        #help menu for the program
        parser=argparse.ArgumentParser(
        usage='enron_search term [term ...]', #usage option
        description='Welcome to Forensics Email Analyzer',
        epilog="This program was coded by Tri Nguyen and Ryan Salinas!!")

        
        parser.add_argument('search', nargs='+', help='Enter keyword(s) to search in dataset')
        args=parser.parse_args()

        #tokenize the input given by the user using space delimeter
        search_str = str(' '.join(args.search)).split(" ") 
        


        for i in range(len(search_str)):
            search_str[i] = search_str[i].lower()
        
        search_clean = list(OrderedDict.fromkeys(search_str))
       
       
        rootDir='.' #root directory where all the enron mbox files are located
        for search in search_clean:
            for (root,dirs,files) in os.walk(rootDir, topdown=False):
                for inbox in files:
                    mbox = mailbox.mbox(inbox,create=False)
                    for i, message in enumerate(mbox):
                        message = str(read_email_payload(message))
                        if(len(re.findall('\\b'+search+'\\b', message)) > 0 ):
                           print_result(mbox, inbox)

        global count
        print("result found:",count) #print the total results

        # if no argument are given, print help screen and exit
        if (len(sys.argv)==1):
            parser.print_help()
            parser.exit()

    #if user press CtrlC, print message and exit the program
    except KeyboardInterrupt:
        print("\nExiting the program, goodbye!")
        sys.exit(0)

if (__name__ == "__main__"):
    main()
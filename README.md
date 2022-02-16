Email Forensics Tool
----------------------
Developed by team members:
Tri Nguyen   - A04233345
Ryan Salinas - A04065275

DESCRIPTION
For each email with a message body in the Enron Dataset that matches all the terms given by the user, the program captures and output the sender email and the date the email was sent. the program will dislay the number results and display the total number of results found when the search is completed.

Note that the program ignores any duplicate terms, term order, and is not case sensitive.

For example:
  hide Hide the EVIDENCE
  HIDE THE EVIDENCE
  EVIDENCE hide the
  hide the evidence

All these inputs above  will produce the exact same result.

USAGE
1. Download the Enron email data set from https://www.cs.cmu.edu/~enron/. Be sure to get the May 7, 2015 version (the file will be named enron_mail_2015057.tar.gz).
2. Go to https://github.com/lintool/Enron2mbox and follow the instructions to convert the data to the mbox format.
3. Please make sure that the python program is in the same directory as enron dataset in Mbox format (AKA the Enron directory)
4. Execute the program using the following command: python3 enron_search [INPUT] 



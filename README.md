# Bloom-Filter
This is the implementation of a simple Bloom Filter written in Python.

The program takes two input .csv files.

One file contains a "Data Base" of text in email format. The other contains a list of emails that the user wishes to search for
in the "Data Base" file.

The program outputs a results.csv file which contains all the emails to be searched for and the result of whether they were found
in the "Data Base" file or not.

To run the code, please do the following:
1. Make sure you have all files in the same directory. Two csv files and one py file.
2. Delete the results.csv file or rename it for later comparison.
3. Open your IDE terminal, ensure the directory is correct.
4. Enter the command "python Bloom_Filter.py DB_emails.csv Emails_forSearch.csv" (without the quotation marks).
5. The program will print "Finished!" to show completion and will create the results.csv file in the same directory.

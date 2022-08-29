import sys
import math
import mmh3
import pandas as pd


# This method reads and returns the data in the first csv file.
def readDB_Items(db_email):
    try:
        read_file = pd.read_csv(db_email)

    except FileNotFoundError:
        print("File not found.")

    else:
        return read_file


# This method reads and returns the data in the second csv file.
def readRequests(req_email):
    try:
        read_file = pd.read_csv(req_email)

    except FileNotFoundError:
        print("File not found.")

    else:
        return read_file


# This method uses the data in the first file to construct a Bloom Filter.
# It calculates the hash value of the given parameter and, once the hash
# has been calculated, it is used as an index value to change the zero-bit
# to a one-bit in that specific position.
def BloomFilter(DBItems):

    for seed in range(k):
        Hash_value = mmh3.hash(DBItems, seed) % m
        bit_vector[Hash_value] = 1


# This method uses the data in the second file and compares it to the data in the first file,
# according to our bit_vector array. It essentially does the same process as the BloomFilter()
# method, but instead of changing the value in the index derived from the hash value it sees
# the element in the given index is a 1. If so, the "result" variable will equal
# "Probably in the DB", else it equals "Not in the DB". It returns a list that contains the
# elements of the second csv file and the results of each search.
def SearchInDB(Wanted_Emails):

    result = ""
    for seed in range(k):
        search_req = mmh3.hash(Wanted_Emails, seed) % m
        if bit_vector[search_req] == 1:
            result = "Probably in the DB"
        else:
            result = "Not in the DB"
    return [Wanted_Emails, " " + result]


if __name__ == "__main__":

    # reads the two files inputted by the user and stores them in variables.
    # If there are less than 2 files it will return an error message.
    bloom_items = readDB_Items(sys.argv[1])
    check_items = readRequests(sys.argv[2])

    # n represents the quantity of items in the first file.
    n = len(bloom_items)
    # probability of false positives
    p = 0.0000001
    # represents the length of bit_vector array
    m = math.ceil((n * math.log(p)) / math.log(1 / pow(2, math.log(2))))
    # number of hashes to be done according to other parameters
    k = round((m / n) * math.log(2))

    # This array has nothing but bits. I will be used as our Bloom Filter.
    bit_vector = [0] * m

    # These are the labels of the columns that will be displayed in our "results.csv"
    col_names = ["Emails", " Result"]
    data = pd.DataFrame(columns=col_names)

    # Iterates over the items in the first csv file and calls the BloomFilter() method.
    for i in range(len(bloom_items)):
        BloomFilter(bloom_items['Email'][i])

    # Iterates over the items in the second csv file and calls the SearchInDB() method. The output of this method is
    # later stored in the "data" variable.
    for j in range(len(check_items)):
        data.loc[len(data.index)] = SearchInDB(check_items['Email'][j])

    # Stores the path where the output file will reside
    sys.argv[1] = 'results.csv'
    results = sys.argv[1]
    # Stores the data in the output file
    # NOTE: Results file may not appear immediately
    data.to_csv(results, index=False)

    # print(bit_vector)
    # If there is no error, this message shall be displayed to show completion.
    print("Finished!")

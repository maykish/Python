#!/usr/bin/env python3

# This script downloads a movie database file from the web and parses its contents, extracting the first column of data and then sorting it out alphabetically. In the end, names.txt is created with the names of all people from the database, and sorted_names.txt, with a sorted list for use in more programming projects.  

from typing import List
import requests
import gzip

def download_dataset(filename: str):
    print("Fetching data from IMDb...", end=" ")

    url = "https://datasets.imdbws.com/name.basics.tsv.gz"
    response = requests.get(url, allow_redirects=True)
    with open(filename, "wb") as f:
        f.write(response.content)

    print("Done!")

def fetch_names_from_file(filename: str) -> List[str]:
    print("Parsing data from the file...", end=" ")

    f = gzip.open("IMDb.tsv.gz", "r")  # Decompress
    header = f.readline().decode("utf-8")
    name_index = header.split("\t").index("primaryName")

    names = []

    for line in f:
        names.append(line.decode("utf-8").split("\t")[name_index])

    print("Done!")

    return names

def sort_names(names):
    print("Sorting names... ", end=" ")

    sorted_names = sorted(names)

    print("Done!")

    return sorted_names

def write_to_files(names, sorted_names):
    with open("names.txt", "w") as out:
        out.write("\n".join(names))

    with open("sorted_names.txt", "w") as out:
       out.write("\n".join(sorted_names))

    print("Successfully created names.txt and sorted_names.txt")

local_file = "IMDb.tsv.gz"
download_dataset(local_file)
names = fetch_names_from_file(local_file)
sorted_names = sort_names(names)
write_to_files(names, sorted_names)

#!/usr/bin/python3
"""
Records all tasks that are owned by the queried employee and return
the info in a csv file
"""
import requests
import sys
import csv

if __name__ == "__main__":
    id_ = sys.argv[1]
    url_u = "https://jsonplaceholder.typicode.com/users"
    usr_res = requests.get(url_u, params={"id": id_})
    usr_data = usr_res.json()[0]

    url_t = "https://jsonplaceholder.typicode.com/todos"
    tod_res = requests.get(url_t, params={"userId": id_})
    todo_data = tod_res.json()

    with open("{}.csv".format(id_), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [id_, usr_data["username"], t.get("completed"), t.get("title")]
            ) for t in todo_data]

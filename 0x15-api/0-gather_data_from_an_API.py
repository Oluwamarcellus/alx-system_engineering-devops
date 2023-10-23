#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID
"""
import requests
import sys

if __name__ == "__main__":
    id_ = int(sys.argv[1])
    url_u = "https://jsonplaceholder.typicode.com/users"
    usr_res = requests.get(url_u, params={"id": id_})
    usr_data = usr_res.json()[0]

    url_t = "https://jsonplaceholder.typicode.com/todos"
    tod_res = requests.get(url_t, params={"userId": id_})
    todo_data = tod_res.json()

    todo_done = 0
    for i in todo_data:
        if i["completed"]:
            todo_done += 1

    user_info = "Employee {} is done with tasks({}/{}):".format(
        usr_data["name"],
        todo_done,
        len(todo_data)
    )

    print(user_info)
    for i in todo_data:
        if i["completed"]:
            print("\t {}".format(i["title"]))

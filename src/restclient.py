'''
REST API test
'''


import requests
import os
from datetime import datetime
import deco



@deco.synchronized
def getusers():
    for i in range(1, 11):
        getuser(i)


@deco.concurrent
def getuser(id):
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id)).json()
    print('{} {} {} {}'.format(os.getpid(), response["id"], response["name"], response["company"]["name"]))
    # print(response)


if __name__ == "__main__":
    starttime = datetime.now()
    getusers()
    print("time taken:", datetime.now() - starttime)

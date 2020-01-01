from urllib.request import *
from urllib.error import *
import socket
import os

def get(jie,nian,school,id):
    try:
        a = urlopen("http://211.153.82.232/cmisfolder/photos/%s/%s/%s/%s.JPG" % (jie,nian,school,id))
        if not os.path.exists("picture/"):
            os.mkdir("picture/")
        with open("picture/"+id+".JPG", "wb") as f:
            f.write(a.read())
    except HTTPError as e:
        print(str(e)+" "+id+".JPG")

    try:
        a = urlopen("http://211.153.82.232/cmisfolder/photos/%s/%s/%s/%s.jpg" % (jie,nian,school,id))
        if not os.path.exists("picture/"):
            os.mkdir("picture/")
        with open("picture/"+id+".jpg", "wb") as f:
            f.write(a.read())
    except HTTPError as e:
        print(str(e)+" "+id+".jpg ")

if __name__ == "__main__":
    get("2012003","2021","01124006","09068048");
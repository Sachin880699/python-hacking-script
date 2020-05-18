import urllib.request
from urllib.error import HTTPError
import urllib.request as urllib2
import urllib.request as urllib2
import requests
import re
import datetime


# get url
url = input('Enter a URL (include `http://`): ')
# connect to the url
website = requests.get(url)
# read html
html = website.text
# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
# output links
for link in links:
    data = link[0]
    with open("log.txt","a") as f:
        f.write(data)
        f.write("\n")
with open('log.txt', "r") as ifile:
    for line in ifile:
        try:
            import urllib.request as urllib2
            from six.moves import urllib
            print(urllib.request.urlopen(line).getcode())
        except HTTPError as err:
            if err.code== 404:
                error = "404 page not found error"
                print(error)
                date_and_time = datetime.datetime.now()
                date_and_time = str(date_and_time)
                with open('error.txt','a') as f:
                    f.write(date_and_time)
                    f.write("\n")
                    f.write(error)
                    f.write("\n")
                    f.write("=========================================================================================================")
                    f.close()
            if err.code==403:
                error = "403 forbidden error"
                print(error)
                date_and_time = datetime.datetime.now()
                date_and_time = str(date_and_time)
                with open('error.txt','a') as f:
                    f.write(date_and_time)
                    f.write("\n")
                    f.write(error)
                    f.write("\n")
                    f.write("=========================================================================================================")
                    f.close()
            if err.code ==401:
                error = "Unauthorized error"
                print(error)
                date_and_time = datetime.datetime.now()
                date_and_time = str(date_and_time)
                with open('error.txt','a') as f:
                    f.write(date_and_time)
                    f.write("\n")
                    f.write(error)
                    f.write("\n")
                    f.write("=========================================================================================================")
                    f.close()
            if err.code==500:
                error = "Internal Server Error"
                print(error)
                date_and_time = datetime.datetime.now()
                date_and_time = str(date_and_time)
                with open('error.txt','a') as f:
                    f.write(date_and_time)
                    f.write("\n")
                    f.write(error)
                    f.write("\n")
                    f.write("=========================================================================================================")
                    f.close()
            if err.code==504:
                error = "Gateway timeout"
                print(error)
                date_and_time = datetime.datetime.now()
                date_and_time = str(date_and_time)
                with open('error.txt','a') as f:
                    f.write(date_and_time)
                    f.write("\n")
                    f.write(error)
                    f.write("\n")
                    f.write("=========================================================================================================")
                    f.close()
            if err.code==503:
                error = "Service Unavailable"
                print(error)
                date_and_time = datetime.datetime.now()
                date_and_time = str(date_and_time)
                with open('error.txt','a') as f:
                    f.write(date_and_time)
                    f.write("\n")
                    f.write(error)
                    f.write("\n")
                    f.write("=========================================================================================================")
                    f.close()
            else:
                error = "unknown error"
                print(error)
                date_and_time = datetime.datetime.now()
                date_and_time = str(date_and_time)
                with open('error.txt','a') as f:
                    f.write(date_and_time)
                    f.write("\n")
                    f.write(error)
                    f.write("\n")
                    f.write("=========================================================================================================")
                    f.close()

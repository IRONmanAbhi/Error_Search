import sys
import subprocess
from subprocess import Popen, PIPE
import requests
import webbrowser


def execute_return(cmd):
    args = cmd.split()
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out, err


def make_request(erorr):
    res = requests.get("https://api.stackexchange.com/" +
                       "/2.3/search?order=desc&sort=activity&tagged=python&intitle={}&site=stackoverflow".format(erorr))
    return res.json()


def get_urls(json_dict):
    url_list = []
    count = 0
    for i in json_dict["items"]:
        if i["is_answered"]:
            url_list.append(i["link"])
        count += 1
        if count == 4:
            break

    for i in url_list:
        webbrowser.open(i)


if __name__ == "__main__":
    file_name = sys.argv[1]
    print(file_name)
    subprocess.run(["python", file_name])
    op, err = execute_return("python {0}".format(file_name))
    error_message = err.decode("utf-8").strip().split("\r\n")[-1]
    if error_message:
        filter_err = error_message.split(":")
        json1 = make_request(filter_err[0])
        json2 = make_request(filter_err[1])
        json3 = make_request(filter_err[2])
        json4 = make_request(filter_err[3])
        json = make_request(error_message)
        get_urls(json4)
        get_urls(json3)
        get_urls(json1)
        get_urls(json2)
        get_urls(json)

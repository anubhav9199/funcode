import json
import time


def write_in_file(username, password, question, answer):
    data_to_dump = {}
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    date = "%s:%s:%s" % (curr.tm_mday, curr.tm_mon, curr.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    data_to_dump[username] = {
        "createdAtDate": date,
        "createdAtTs": time_write,
        "username": username,
        "password": password,
    }
    data_to_dump[username][question] = answer

    try:
        with open("use_dbs.json", "a", encoding='utf-8') as file:
            file.write(json.dumps(data_to_dump))
    except Exception as e:
        raise e


def read_from_file():
    try:
        data_file = open("use_dbs.json", "r", encoding='utf-8')
        return json.loads(data_file.read())
    except Exception as e:
        raise e


def write_login_logs(username, activity):
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    date = "%s:%s:%s" % (curr.tm_mday, curr.tm_mon, curr.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    with open("log_dbs.txt", "a", encoding='utf-8') as file:
        file.write("Date: %s\nTime: %s\nUsername: %s\nActvity: %s" %
                (date, time_write, username, activity))
        file.write("\n--------------------\n")

import datetime
import json

import requests
from config import tibbr_config


def login():
    form = {
        "params[login]": tibbr_config["domain_id"],
        "params[password]": tibbr_config["password"],
        "params[session_manager]": "cookie",
    }
    result = requests.post("https://mb.oocl.com/tibbr/web/login", data=form, verify=False)
    return result.headers['X-CSRF-Token'], result.cookies


def post(token, cookies):
    json_data = {
        "format": "json",
        "message": {
            "rich_content": ' @Corporate.ISD.ZHA.ISDC_ZHA_IT_Academy.2018_Class @%s @%s @%s ' % (
                tibbr_config['leader'], tibbr_config['tutor'], tibbr_config['teacher']) + build_weekly_report(calculate_week_and_date(),
                                                                                     build_report_with_md()),
            "temp_files": "",
            "private_message": "true",
            "msg_type": "plain"
        },
        "tibbr-subject_name": "",
        "subject_name": ",Corporate.ISD.ZHA.ISDC_ZHA_IT_Academy.2018_Class,%s,%s,%s" % (
            tibbr_config['leader'], tibbr_config['tutor'], tibbr_config['teacher']),
        "allow_subject_announcement": "false",
        "authenticity_token": token,
        "access_token": "undefined"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    result = requests.post("https://mb.oocl.com/a/messages", data=json.dumps(json_data), verify=False, cookies=cookies,
                           headers=headers)
    return result.status_code


def build_weekly_report(date, contents):
    msg = '<p></p><p><b><u><b><u><b><u>' \
          '[ITA] Weekly Report on Week No.%s (%s to %s)' \
          '</u></b></u></b><br>1. Key learning, skills and experience acquired</u></b></p>' \
          '<ul>%s</ul>' \
          '<u><b>2. Problem / Confusing / Difficulties</b></u>' \
          '<br><ul>%s</ul>' \
          '<u><b>3. Other Comments / Suggestion</b></u>' \
          '<br><ul>%s</ul><br><p></p></div>'
    week, from_date, to_date = date
    key_learning_content, problem_content, other_content = contents
    return msg % (week, from_date, to_date, key_learning_content, problem_content, other_content)


def format_content(contents):
    if (len(contents) == 0):
        return '<li>No update.</li>'
    return str.join("", ['<li>' + content + '</li>' for content in contents])


def build_report_with_md():
    f = open('report.md', 'r')
    file_content = f.read().split("##")[1:]
    contents = []
    for index in range(len(file_content)):
        contents.append(format_content(get_content_from_each_subtitle(file_content, index)))
    return contents


def get_content_from_each_subtitle(content, index):
    key_learning_content = [content[3:] for content in content[index].split("\n")[1:] if content != ""]
    return key_learning_content


def calculate_week_and_date():
    today = datetime.datetime.now()
    days_of_week = int(today.strftime("%w"))
    from_date = (today + datetime.timedelta(days=-days_of_week + 1))
    to_date = (from_date + datetime.timedelta(days=4))
    return [today.strftime("%W"), from_date.strftime("%Y/%m/%d"), to_date.strftime("%Y/%m/%d")]


if __name__ == "__main__":
    token, cookies = login()
    if post(token, cookies) == 201:
        print("""
            *******************
            *  post success!  *
            *******************
        """)
    else:
        print("""
            *****************
            *  post faild!  *
            *****************
        """)

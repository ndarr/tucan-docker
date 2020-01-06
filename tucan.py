#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import mechanize
from lxml import html

class Grade:
    def __init__(self):
        self.id = ""
        self.subject = ""
        self.date = ""
        self.result_no = ""
        self.result_str = ""

    def __init__(self, array):
        self.from_array(array)

    def from_array(self, array):
        self.id = array[0].split()[0]
        self.subject = " ".join(array[0].split()[1:])
        self.date = array[1]
        self.result_no = array[2]
        self.result_str = array[3]

def parse_grades(grades):
    grades_parsed = []
    for grade in grades:
        grade_parsed = Grade(array=grade)
        grades_parsed.append(grade_parsed)
    return grades_parsed



def get_grades(username, password):
    br = mechanize.Browser()
    br.open("https://www.tucan.tu-darmstadt.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=EXTERNALPAGES&ARGUMENTS"
            "=-N000000000000001,-N000344,-Awelcome")
    br.select_form(nr=0)
    br.form["usrname"] = username
    br.form["pass"] = password
    br.submit()

    br.follow_link(text_regex=u"^Prüfungen$")
    br.follow_link(text_regex=u"^Semesterergebnisse$")
    br.follow_link(text_regex=u"^Prüfungsergebnisse$")

    tree = html.fromstring(br.response().read())
    tbody = tree.xpath("//table[@class='nb list']/tbody")[0]

    grades = [[" ".join(unicode(td.text).strip().split())
               for td in tr.findall("td")][:-1]
              for tr in tbody.findall("tr")]

    return parse_grades(grades)

#!/usr/bin/env python
# new_minutes.py

from datetime import datetime
import os

TEMPLATE = """\
---
layout:     minutes
title:      {title}
date:       {date}
sequence:   "{sequence}"
status:     draft
permalink:  /register/minutes/{sequence}/
---

"""

if __name__ == "__main__":

    title = raw_input("Meeting Title:\n")

    datestamp = datetime.today().strftime("%Y-%m-%d")

    seq = len([name for name in os.listdir('minutes') if os.path.isfile('minutes/' + name)])
    seq = "%03d" % (seq + 1)

    file_name = datestamp + "-minutes-" + seq + ".markdown"

    with open("minutes/" + file_name, "w+") as file:
        file.write(TEMPLATE.format(title=title, date=datestamp, sequence=seq))

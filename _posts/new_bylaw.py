#!/usr/bin/env python
# new_bylaw.py

from datetime import datetime
import os

TEMPLATE = """\
---
layout:     bylaw
title:      {title}
date:       {date}
sequence:   "{sequence}"
status:     draft
permalink:  /register/bylaw/{sequence}/
---

Be it enacted as a bylaw of the Pubgem Foundation as follows:

## Article 1: Something

0. **Blah**. Here is a statement.

"""

if __name__ == "__main__":

    title = raw_input("Title:\n")

    datestamp = datetime.today().strftime("%Y-%m-%d")

    seq = len([name for name in os.listdir('bylaws') if os.path.isfile('bylaws/' + name)])
    seq = "%03d" % seq

    file_name = datestamp + "-bylaw-" + seq + ".markdown"

    with open("bylaws/" + file_name, "w+") as file:
        file.write(TEMPLATE.format(title=title, date=datestamp, sequence=seq))

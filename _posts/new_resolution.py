#!/usr/bin/env python
# new_resolution.py

from datetime import datetime
import os

TEMPLATE = """\
---
layout:     resolution
title:      {title}
date:       {date}
sequence:   "{sequence}"
act:        False
status:     draft
permalink:  /register/resolution/{sequence}/
---

- whereas; and

Therefore be it resolved:

1. First
2. Second

"""

if __name__ == "__main__":

    title = raw_input("Title:\n")

    datestamp = datetime.today().strftime("%Y-%m-%d")

    seq = len([name for name in os.listdir('resolutions') if os.path.isfile('resolutions/' + name)])
    seq = "%03d" % (seq + 1)

    file_name = datestamp + "-resolution-" + seq + ".markdown"

    with open("resolutions/" + file_name, "w+") as file:
        file.write(TEMPLATE.format(title=title, date=datestamp, sequence=seq))

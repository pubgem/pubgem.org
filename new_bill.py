#!/usr/bin/env python
# new_bill.py

from datetime import datetime
import os

TEMPLATE = """\
---
layout:     bill
title:      {title}
date:       {date}
sequence:   "{sequence}"
enacted:    False
status:     draft
permalink:  /register/bill/{sequence}/
---

## Preamble

- whereas; and

Therefore be it enacted as a bylaw of the Pubgem Foundation as follows:

## Article 1: Something

0. **Blah**. Here is a statement.

"""

if __name__ == "__main__":

    title = raw_input("Title:\n")

    datestamp = datetime.today().strftime("%Y-%m-%d")

    seq = len([name for name in os.listdir('bills') if os.path.isfile('bills/' + name)])
    seq = "%03d" % (seq)

    file_name = "bill-" + seq + ".markdown"

    with open("_bills/" + file_name, "w+") as file:
        file.write(TEMPLATE.format(title=title, date=datestamp, sequence=seq))

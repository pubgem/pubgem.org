#!/usr/bin/env python
# new_minutes.py

from datetime import datetime
import os

TEMPLATE = """\
---
layout:     minutes
title:      Monthly Meeting
date:       {date}
sequence:   "{sequence}"
status:     draft
permalink:  /register/minutes/{sequence}/
---

## Call to order

A monthly meeting of the Pubgem Foundation was held at LOCATION on {date}.

## Attendees

- 

## Reports

- Secretary reported the previous meeting's minutes through the Pubgem Foundation \
Register. Secretary moves to accept last meeting's minutes.  The motion is CARRIED/AMENDED.

## Unfinished Business

- 

## New Business

- 

## Announcements

- 

## Adjournment

The next meeting shall be held at LOCATION on DATE.

The meeting was called to close at TIME.

"""

if __name__ == "__main__":

    title = raw_input("Meeting Title:\n")

    datestamp = datetime.today().strftime("%Y-%m-%d")

    seq = len([name for name in os.listdir('minutes') if os.path.isfile('minutes/' + name)])
    seq = "%03d" % (seq)

    file_name = "minutes-" + seq + ".markdown"

    with open("_minutes/" + file_name, "w+") as file:
        file.write(TEMPLATE.format(title=title, date=datestamp, sequence=seq))

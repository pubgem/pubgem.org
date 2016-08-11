---
layout:     post
title:      May Hackathon Results
date:       2016-05-30
tags:       hackathon, sprint, toronto
---

The development team convened a one-day hackathon on Monday May 30, 2016 in Toronto.  We focused on RSS aggregation, the production server, and the Front Page in [the architecture](http://project.pubgem.org/design/pubgem_Architecture.pdf).

## RSS Aggregation

### Motivation

Publishers typically use RSS to provide notifications about new publications.  Pubgem needs to have the latest citation information in order to maximize relevance.  Thus, the *RSS Aggregator* is a process that constantly monitors RSS sources for updates, and when it finds new things, it will send them through the Pubgem processing pipeline.

### Results

The [RSS Aggregator Daemon](https://github.com/pubgem/rss-aggregator) is a stand-alone project on github.  It maintains a list of RSS sources.  The daemon process runs constantly in the background, and every 15 minutes or so, a systemd trigger launches the refresh procedure.  Any entries are logged to a database in order to eliminate duplicates.

## Production Server

### Motivation

Pubgem needs a permanent server so that long-running daemon processes can be hosted.  There will also be web hosting needs that depend upon application server processes.  In order to develop for this environment, it will be necessary to have development environments within which to perform testing.

### Results

A [system environment](https://github.com/pubgem/env-omnibus) was created using Vagrant.  There is currently only one system environment called the omnibus environment because it is suitable for any kind of server instance.  It is possible that in the future we will need application servers, database servers, load balancers, etc.  In that case, the omnibus environment will need to be specialized for different purposes.

## Front Page

### Motivation

In order for a project like Pubgem to be successful, it is necessary to create user-oriented applications that make it easy to interface with the Pubgem database.  The *front page* will be a facility enabling users to subscribe to various publication sources - such as journals - in order to configure a personalized "front page" with all the latest publications from those sources.  The aim is for the Pubgem Front Page to become part of the daily routine for many academics.

### Results

The Front Page is a list of articles that have been indexed by Pubgem so far.  There are currently about 20 journal sources.  The Front Page has been implemented as part of the RSS Aggregator.  It works as a proof-of-concept, but it will need to be split apart in the near future because the system architecture specifies a separation between these components.

## Hackathon Conclusions

This was an extremely productive day.  Everything necessary for a minimum viable product "Front Page" is in place.  This is good enough to demonstrate some of the functionality that Pubgem will bring to the field, but it's just the beginning.

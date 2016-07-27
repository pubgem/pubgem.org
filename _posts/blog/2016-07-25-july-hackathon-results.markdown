---
layout:     post
title:      July Hackathon Results
date:       2016-07-25
tags:       hackathon, sprint, toronto
---

The development team convened another one-day hackathon on Monday July 25, 2016 in Toronto.  This time, we focused on the BibTeX pipeline in [the architecture](http://project.pubgem.org/design/pubgem_Architecture.pdf).

## RSS Citation Parsing

### Motivation

As new articles are collected from sources like *Journal Publishers*, we will require the ability to parse certain fields (particularly the authors' field) on the basis of inconsistencies in the ways different publishers construct their RSS feeds.

### Result

There is now support for a robust *adapter pattern* that will permit custom parsers to be built for any publisher.  This parsing pattern is a critical filter along the citation pipeline. The next steps here are to write specific parsers for the various publishers and then to send the results down the pipeline to the Curation Daemon.

## BibTeX Curation Daemon

### Motivation

Filtered citations are produced by the *RSS Aggregator*, which must then be stored as plain BibTeX citations in [the public BibTeX git repository](https://github.com/pubgem/bib).  The curator will have several methods for improving the quality of the data in the *BibTeX git repository*, but the first need will be to eliminate duplicate citations.  The curator will also implement our first major curation directive, which is to separate publishers and journals into individual BibTeX files.

### Result

There is now a curation daemon that is capable of receiving raw BibTeX and determining whether and how to incorporate that citation within the repository.  The curation daemon works under specific conditions, but it has not been placed into production yet.  To see the daemon in action, look at the *testing* branch of [the BibTeX repository](https://github.com/pubgem/bib/tree/testing).

## Hackathon Conclusions

This was some critical infrastructure work that will form the foundation for all that is to come.

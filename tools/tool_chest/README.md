# About

This directory contains tools to download, parse, and output the categories
 and tools of XebiaLabs' DevOps Tool Chest.

# Usage

Run `make` to download the necessary tools and build a JSON file to be placed
 into the \_data directory for Jekyll. This file is then used to parse and
 build content for the */tools/* part of the Wiki.

# Slugify

Included in the venv is the tool `./tool_chest.venv/bin/slufigy` which can be
 used to generate slugified strings. These are used to create the names of
 files or directories in the wiki (so this might be relocated in the future).

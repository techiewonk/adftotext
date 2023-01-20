# adftotxt
#### Parse Atlassian Document Format to Simple Texts

**adftotxt** is a simple parser that converts JSON Formatted Atlassian Documents into Simple texts for storing in Google Sheets as reports.

## Features
- Parse top level (doc), mid level (paragraph, orderedLists, etc), child nodes (text, listItem)
- Parse marks
- Parse Links

## Installation
Dillinger requires [Python>=3.6](https://nodejs.org/) and [pip](https://pip.pypa.io/en/stable/) to run.
`pip install adftotxt`

## Usage
```
from adftotxt import adftotxt
adf = { } #ADF from JIRA
print(adftotxt.startParsing(adf [, debug=True][, bulletDecor='#']))
```

And of course **adftotxt** itself is open source.

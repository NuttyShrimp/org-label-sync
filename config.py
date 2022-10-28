token='PASTE-YOUR-GH-TOKEN-HERE'
org = 'ZeusWPI'
# deletes labels that are not tlisted in newLabels array
shouldDeleteUnknown = False
projects = [
    "ZeusWPI",
    "Haldis",
    "zinc",
    "ZOUT",
    "zeus.ugent.be",
    "Tap",
    "Tab",
    "Gandalf"
]

newLabels = [
    {
        "name": "hacktoberfest-accepted",
        "color": "819A05",
        "description": "",
    },
    {
        "name": "bug",
        "color": "fc2929",
        "description": " Something isn't working",
    },
    {
        "name": "enhancement",
        "color": "84b6eb",
        "description": "",
    },
    {
        "name": "feature",
        "color": "bfd4f2",
        "description": "New feature or request",
    },
    {
        "name": "level: easy",
        "color": "0D624A",
        "description": "Small/easy issue fixable in an evening",
    },
    {
        "name": "level: medium",
        "color": "FA6C31",
        "description": "",
    },
    {
        "name": "level: hard",
        "color": "B60205",
        "description": "",
    },
    {
        "name": "first-good-issue",
        "color": "7057ff",
        "description": "Good for newcomers",
    },
    {
        "name": "chore",
        "color": "D9C95E",
        "description": "",
    },
    {
        "name": "wontfix",
        "color": "939A95",
        "description": "Will not be worked on",
    }
]


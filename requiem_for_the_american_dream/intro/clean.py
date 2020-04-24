"""
Data Syntax
{
  name: "root",
  children: [
    {
      name: "leafA",
      value: 3
    },
    {
      name: "nodeB",
      children: [
        {
          name: "leafBA",
          value: 5
        },
        {
          name: "leafBB",
          value: 1
        }
      ]
    }
  ]
}
"""

import csv
import json

data = []
with open('./sources/distribution_of_wealth_over_time/dfa-networth-levels.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# One quarter sample
print(json.dumps(data[0], indent=4))
print(json.dumps(data[1], indent=4))
print(json.dumps(data[2], indent=4))
print(json.dumps(data[3], indent=4))

testJson = {
    "name": "networth",
    "children": [
        {
            "name": data[0]["Category"],
            "children": [
                {
                    "name": "Assets",
                    "size": data[0]["Assets"]
                },
                {
                    "name": "Liabilities",
                    "size": data[0]["Liabilities"]
                }
            ]
        },
        {
            "name": data[1]["Category"],
            "children": [
                {
                    "name": "Assets",
                    "size": data[1]["Assets"]
                },
                {
                    "name": "Liabilities",
                    "size": data[1]["Liabilities"]
                }
            ]
        },
        {
            "name": data[2]["Category"],
            "children": [
                {
                    "name": "Assets",
                    "size": data[2]["Assets"]
                },
                {
                    "name": "Liabilities",
                    "size": data[2]["Liabilities"]
                }
            ]
        },
        {
            "name": data[3]["Category"],
            "children": [
                {
                    "name": "Assets",
                    "size": data[3]["Assets"]
                },
                {
                    "name": "Liabilities",
                    "size": data[3]["Liabilities"]
                }
            ]
        }
    ]
}

print(testJson)
print(json.dumps(testJson, indent=4))

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(testJson, f, ensure_ascii=False, indent=4)

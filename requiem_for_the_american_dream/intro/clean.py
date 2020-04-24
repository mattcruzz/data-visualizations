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
                    "children": [
                        {
                            "name": "Real estate",
                            "size": data[0]["Real estate"]
                        },
                        {
                            "name": "Consumer durables",
                            "size": data[0]["Consumer durables"]
                        },
                        {
                            "name": "Corporate equities and mutual fund shares",
                            "size": data[0]["Corporate equities and mutual fund shares"]
                        },
                        {
                            "name": "Pension entitlements",
                            "size": data[0]["Pension entitlements"]
                        },
                        {
                            "name": "Private businesses",
                            "size": data[0]["Private businesses"]
                        },
                        {
                            "name": "Other assets",
                            "size": data[0]["Other assets"]
                        }
                    ]
                },
                {
                    "name": "Liabilities",
                    "children": [
                        {
                            "name": "Home mortgages",
                            "size": data[0]["Home mortgages"]
                        },
                        {
                            "name": "Consumer credit",
                            "size": data[0]["Consumer credit"]
                        },
                        {
                            "name": "Other liabilities",
                            "size": data[0]["Other liabilities"]
                        }
                    ]
                }
            ]
        },
        {
            "name": data[1]["Category"],
            "children": [
                {
                    "name": "Assets",
                    "children": [
                        {
                            "name": "Real estate",
                            "size": data[1]["Real estate"]
                        },
                        {
                            "name": "Consumer durables",
                            "size": data[1]["Consumer durables"]
                        },
                        {
                            "name": "Corporate equities and mutual fund shares",
                            "size": data[1]["Corporate equities and mutual fund shares"]
                        },
                        {
                            "name": "Pension entitlements",
                            "size": data[1]["Pension entitlements"]
                        },
                        {
                            "name": "Private businesses",
                            "size": data[1]["Private businesses"]
                        },
                        {
                            "name": "Other assets",
                            "size": data[1]["Other assets"]
                        }
                    ]
                },
                {
                    "name": "Liabilities",
                    "children": [
                        {
                            "name": "Home mortgages",
                            "size": data[1]["Home mortgages"]
                        },
                        {
                            "name": "Consumer credit",
                            "size": data[1]["Consumer credit"]
                        },
                        {
                            "name": "Other liabilities",
                            "size": data[1]["Other liabilities"]
                        }
                    ]
                }
            ]
        },
        {
            "name": data[2]["Category"],
            "children": [
                {
                    "name": "Assets",
                    "children": [
                        {
                            "name": "Real estate",
                            "size": data[2]["Real estate"]
                        },
                        {
                            "name": "Consumer durables",
                            "size": data[2]["Consumer durables"]
                        },
                        {
                            "name": "Corporate equities and mutual fund shares",
                            "size": data[2]["Corporate equities and mutual fund shares"]
                        },
                        {
                            "name": "Pension entitlements",
                            "size": data[2]["Pension entitlements"]
                        },
                        {
                            "name": "Private businesses",
                            "size": data[2]["Private businesses"]
                        },
                        {
                            "name": "Other assets",
                            "size": data[2]["Other assets"]
                        }
                    ]
                },
                {
                    "name": "Liabilities",
                    "children": [
                        {
                            "name": "Home mortgages",
                            "size": data[2]["Home mortgages"]
                        },
                        {
                            "name": "Consumer credit",
                            "size": data[2]["Consumer credit"]
                        },
                        {
                            "name": "Other liabilities",
                            "size": data[2]["Other liabilities"]
                        }
                    ]
                }
            ]
        },
        {
            "name": data[3]["Category"],
            "children": [
                {
                    "name": "Assets",
                    "children": [
                        {
                            "name": "Real estate",
                            "size": data[3]["Real estate"]
                        },
                        {
                            "name": "Consumer durables",
                            "size": data[3]["Consumer durables"]
                        },
                        {
                            "name": "Corporate equities and mutual fund shares",
                            "size": data[3]["Corporate equities and mutual fund shares"]
                        },
                        {
                            "name": "Pension entitlements",
                            "size": data[3]["Pension entitlements"]
                        },
                        {
                            "name": "Private businesses",
                            "size": data[3]["Private businesses"]
                        },
                        {
                            "name": "Other assets",
                            "size": data[3]["Other assets"]
                        }
                    ]
                },
                {
                    "name": "Liabilities",
                    "children": [
                        {
                            "name": "Home mortgages",
                            "size": data[3]["Home mortgages"]
                        },
                        {
                            "name": "Consumer credit",
                            "size": data[3]["Consumer credit"]
                        },
                        {
                            "name": "Other liabilities",
                            "size": data[3]["Other liabilities"]
                        }
                    ]
                }
            ]
        }
    ]
}

print(testJson)
print(json.dumps(testJson, indent=4))

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(testJson, f, ensure_ascii=False, indent=4)

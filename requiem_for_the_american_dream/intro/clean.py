import csv
import json

data = []
with open('./sources/distribution_of_wealth_over_time/dfa-networth-levels.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)


for i in range(0, len(data), 4):
    quarter_json = {
        "name": "Net Worth",
        "children": [
            {
                "name": data[i]["Category"],
                "children": [
                    {
                        "name": "Assets",
                        "children": [
                            {
                                "name": "Real estate",
                                "size": int(data[i]["Real estate"])
                            },
                            {
                                "name": "Consumer durables",
                                "size": int(data[i]["Consumer durables"])
                            },
                            {
                                "name": "Corporate equities and mutual fund shares",
                                "size": int(data[i]["Corporate equities and mutual fund shares"])
                            },
                            {
                                "name": "Pension entitlements",
                                "size": int(data[i]["Pension entitlements"])
                            },
                            {
                                "name": "Private businesses",
                                "size": int(data[i]["Private businesses"])
                            },
                            {
                                "name": "Other assets",
                                "size": int(data[i]["Other assets"])
                            }
                        ]
                    },
                    {
                        "name": "Liabilities",
                        "children": [
                            {
                                "name": "Home mortgages",
                                "size": int(data[i]["Home mortgages"])
                            },
                            {
                                "name": "Consumer credit",
                                "size": int(data[i]["Consumer credit"])
                            },
                            {
                                "name": "Other liabilities",
                                "size": int(data[i]["Other liabilities"])
                            }
                        ]
                    }
                ]
            },
            {
                "name": data[i+1]["Category"],
                "children": [
                    {
                        "name": "Assets",
                        "children": [
                            {
                                "name": "Real estate",
                                "size": int(data[i+1]["Real estate"])
                            },
                            {
                                "name": "Consumer durables",
                                "size": int(data[i+1]["Consumer durables"])
                            },
                            {
                                "name": "Corporate equities and mutual fund shares",
                                "size": int(data[i+1]["Corporate equities and mutual fund shares"])
                            },
                            {
                                "name": "Pension entitlements",
                                "size": int(data[i+1]["Pension entitlements"])
                            },
                            {
                                "name": "Private businesses",
                                "size": int(data[i+1]["Private businesses"])
                            },
                            {
                                "name": "Other assets",
                                "size": int(data[i+1]["Other assets"])
                            }
                        ]
                    },
                    {
                        "name": "Liabilities",
                        "children": [
                            {
                                "name": "Home mortgages",
                                "size": int(data[i+1]["Home mortgages"])
                            },
                            {
                                "name": "Consumer credit",
                                "size": int(data[i+1]["Consumer credit"])
                            },
                            {
                                "name": "Other liabilities",
                                "size": int(data[i+1]["Other liabilities"])
                            }
                        ]
                    }
                ]
            },
            {
                "name": data[i+2]["Category"],
                "children": [
                    {
                        "name": "Assets",
                        "children": [
                            {
                                "name": "Real estate",
                                "size": int(data[i+2]["Real estate"])
                            },
                            {
                                "name": "Consumer durables",
                                "size": int(data[i+2]["Consumer durables"])
                            },
                            {
                                "name": "Corporate equities and mutual fund shares",
                                "size": int(data[i+2]["Corporate equities and mutual fund shares"])
                            },
                            {
                                "name": "Pension entitlements",
                                "size": int(data[i+2]["Pension entitlements"])
                            },
                            {
                                "name": "Private businesses",
                                "size": int(data[i+2]["Private businesses"])
                            },
                            {
                                "name": "Other assets",
                                "size": int(data[i+2]["Other assets"])
                            }
                        ]
                    },
                    {
                        "name": "Liabilities",
                        "children": [
                            {
                                "name": "Home mortgages",
                                "size": int(data[i+2]["Home mortgages"])
                            },
                            {
                                "name": "Consumer credit",
                                "size": int(data[i+2]["Consumer credit"])
                            },
                            {
                                "name": "Other liabilities",
                                "size": int(data[i+2]["Other liabilities"])
                            }
                        ]
                    }
                ]
            },
            {
                "name": data[i+3]["Category"],
                "children": [
                    {
                        "name": "Assets",
                        "children": [
                            {
                                "name": "Real estate",
                                "size": int(data[i+3]["Real estate"])
                            },
                            {
                                "name": "Consumer durables",
                                "size": int(data[i+3]["Consumer durables"])
                            },
                            {
                                "name": "Corporate equities and mutual fund shares",
                                "size": int(data[i+3]["Corporate equities and mutual fund shares"])
                            },
                            {
                                "name": "Pension entitlements",
                                "size": int(data[i+3]["Pension entitlements"])
                            },
                            {
                                "name": "Private businesses",
                                "size": int(data[i+3]["Private businesses"])
                            },
                            {
                                "name": "Other assets",
                                "size": int(data[i+3]["Other assets"])
                            }
                        ]
                    },
                    {
                        "name": "Liabilities",
                        "children": [
                            {
                                "name": "Home mortgages",
                                "size": int(data[i+3]["Home mortgages"])
                            },
                            {
                                "name": "Consumer credit",
                                "size": int(data[i+3]["Consumer credit"])
                            },
                            {
                                "name": "Other liabilities",
                                "size": int(data[i+3]["Other liabilities"])
                            }
                        ]
                    }
                ]
            }
        ]
    }
    filename = data[i]["Date"].replace(":", "_") + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(quarter_json, f, ensure_ascii=False, indent=4)

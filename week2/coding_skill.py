import json


def read_json():
    with open('data.json', 'r') as f:
        data = json.load(f)

    return data


def coding_skill():
    d = read_json()
    languages = {}
    for x in range(0, len(d['people'])):
        for y in range(0, len(d['people'][x]['skills'])):
            if d['people'][x]['skills'][y]['name'] in languages:
                if languages[d['people'][x]['skills'][y]['name']][2] < d['people'][x]['skills'][y]['level']:
                    languages[d['people'][x]['skills'][y]['name']] = [
                        d['people'][x]['first_name'],
                        d['people'][x]['last_name'],
                        d['people'][x]['skills'][y]['level']
                    ]
                else:
                    continue
            else:
                languages[d['people'][x]['skills'][y]['name']] = [
                    d['people'][x]['first_name'],
                    d['people'][x]['last_name'],
                    d['people'][x]['skills'][y]['level']
                ]

    return languages


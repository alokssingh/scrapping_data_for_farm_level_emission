import json


def serialize_to_json(data, filename):
    json_object = json.dumps(data, indent=4)
    # print(json_object)
    with open(filename, "w") as outfile:
        outfile.write(json_object)

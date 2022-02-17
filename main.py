import json


def read_downloaded_json(path):
    with open(path) as json_file:
        map_data = json.load(json_file)

    print(f"reading in map name: {map_data['name']}\nwith elements:")
    for element in map_data["elements"]:
        print(element["attributes"]["label"])

    return map_data


def update_element(map_data: dict, label: str, field: str, value):
    for element in map_data["elements"]:
        if element["attributes"]["label"] == label:
            element["attributes"][field] = value
            print(element["attributes"])
    return map_data


def save_map(map_data, path):
    with open(path, "w") as outfile:
        json.dump(map_data, outfile)


if __name__ == "__main__":
    load_path = "kumu-tristandowning-samra-1.json"
    map_data = read_downloaded_json(load_path)
    map_data = update_element(map_data, "Element-1", "field-1", "value-1")
    save_path = "kumu-tristandowning-samra-1_modified.json"
    save_map(map_data, save_path)
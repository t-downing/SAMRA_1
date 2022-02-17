import json


def read_downloaded_json(path):
    with open(path) as json_file:
        map_data = json.load(json_file)
    print(f"reading in map name: {map_data['name']}\nwith elements:")
    for element in map_data["elements"]:
        print(element["attributes"]["label"])

    return map_data


def update_element(map_data: dict, label: str, field: str, value):
    # check validity of field

    if field not in [ex_field["name"] for ex_field in map_data["attributes"]]:
        print("field not valid, map will not update")
        # return map_data
    else:
        print("field valid")
    # find element
    for element in map_data["elements"]:
        if element["attributes"]["label"] == label:
            element["attributes"][field] = value
            print(element["attributes"])
    return map_data


def save_map(map_data, path):
    json_object = json.dumps(map_data, indent=4)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(map_data, f, ensure_ascii=False, indent=2)

    # with open(path, "w") as outfile:
    #     json.dump(map_data, outfile)


if __name__ == "__main__":
    load_path = "kumu-tristandowning-samra-1_2.json"
    map_data = read_downloaded_json(load_path)
    map_data = update_element(map_data, "Element-1", "kumu-created-field-1", "value-1-2")
    map_data = update_element(map_data, "Element-2", "kumu-created-field-1", "value-2")
    map_data = update_element(map_data, "Element-2", "label", "Element-2-2")
    save_path = "kumu-tristandowning-samra-1_modified_2.json"
    save_map(map_data, save_path)
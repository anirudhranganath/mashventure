import csv


def write_list_of_dict_to_csv(file_path, list_of_dict, columns):
    with open(file_path, 'wb') as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(list_of_dict)

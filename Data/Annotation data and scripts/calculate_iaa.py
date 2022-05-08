# Author: Thijs Brekhof

import json

from sklearn.metrics import cohen_kappa_score


def get_id(data):
    return data.get('id')


def main():
    # Opening file 1
    with open('pilot_annot_thijs.json', encoding='utf8') as json_file1:
        data1 = json.load(json_file1)

    # Opening file 2
    with open('pilot_annot_nils.json', encoding='utf8') as json_file2:
        data2 = json.load(json_file2)

    # sorting the data (by default the order is weird for some reason)
    data1.sort(key=get_id)
    data2.sort(key=get_id)

    # Getting annotations from annotator 1
    label_list_1 = []
    for i in range(1, 478):

        if i == data1[0].get('id'):
            label_list_1.append(data1[0]["annotations"][0]["result"][0]["value"]['choices'][0])
            del data1[0]
        else:
            label_list_1.append("multiple")

    # Getting annotations from annotator 2
    label_list_2 = []
    for i in range(1, 478):

        if i == data2[0].get('id'):
            try:
                label_list_2.append(data2[0]["annotations"][0]["result"][0]["value"]['choices'][0])
                del data2[0]
            except IndexError:
                label_list_2.append("multiple")
                del data2[0]
        else:
            label_list_2.append("multiple")

    #  Calculating IAA
    print(cohen_kappa_score(label_list_1, label_list_2))


if __name__ == "__main__":
    main()

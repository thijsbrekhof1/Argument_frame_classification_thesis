import json
import sklearn
from sklearn.metrics import cohen_kappa_score


def main():
    # Opening file 1
    with open('pilot_annot_thijs.json', encoding='utf8') as json_file1:
        data1 = json.load(json_file1)

    # Opening file 2
    with open('pilot_annot_thijs.json', encoding='utf8') as json_file2:
        data2 = json.load(json_file2)

    # Getting annotations from annotator 1
    label_list_1 = []
    for count, line in enumerate(data1):
        label_list_1.append(line["annotations"][0]["result"][0]["value"]['choices'][0])

    # Getting annotations from annotator 2
    label_list_2 = []
    for count, line in enumerate(data2):
        label_list_2.append(line["annotations"][0]["result"][0]["value"]['choices'][0])

    # Calculating IAA
    print(cohen_kappa_score(label_list_1, label_list_2))


if __name__ == "__main__":
    main()

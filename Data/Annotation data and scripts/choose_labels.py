import json
import random


def get_id(data):
    return data.get('id')


def main():
    # Opening file 1
    with open('pilot_annot_thijs.json', encoding='utf8') as json_file1:
        data1 = json.load(json_file1)

    # Opening file 2
    with open('pilot_annot_nils.json', encoding='utf8') as json_file2:
        data2 = json.load(json_file2)
    # Opening file 3
    with open('all_annot_thijs.json', encoding='utf8') as json_file3:
        data3 = json.load(json_file3)

    # Opening file 4
    with open('all_annot_thijs.json', encoding='utf8') as json_file4:
        data4 = json.load(json_file4)

    # sorting the data (by default the order is weird for some reason)
    data1.sort(key=get_id)
    data2.sort(key=get_id)
    data3.sort(key=get_id)
    data4.sort(key=get_id)

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

    label_list_3 = []
    for i in range(1, 1434):
        if i == data3[0].get('id'):

            label_list_3.append(data3[0]["annotations"][0]["result"][0]["value"]['choices'][0])
            del data3[0]
        else:
            label_list_3.append("multiple")
    label_dict = {}
    for count, label in enumerate(label_list_3):
        try:
            if label == label_list_1[count]:
                pass
        except IndexError:
            if label in label_dict.keys():
                label_dict[label] += 1
            else:
                label_dict[label] = 1

    # print(label_dict)
    # print(dict(sorted(label_dict.items(), key=lambda x: x[1], reverse=True)))
    # count = 0
    # for i in label_dict.values():
    #     count += i
    # print(count)

    # Choosing what label to pick between annotator 1 and annotator 2's labels
    final_labels = []
    for count, label in enumerate(label_list_1):
        # print(label, "---", label_list_2[count])
        if label == label_list_2[count]:
            final_labels.append(label)
        elif label == "Other" and label_list_2[count] != "Other":
            final_labels.append(label_list_2[count])
        elif label != "Other" and label_list_2[count] == "Other":
            final_labels.append(label)
        else:
            count1 = label_dict[label]
            count2 = label_dict[label_list_2[count]]
            if count1 < count2:
                final_labels.append(label)
                label_dict[label] += 1
            elif count1 > count2:
                final_labels.append(label_list_2[count])
                label_dict[label_list_2[count]] += 1
            elif count1 == count2:
                random_chance = random.choice([0, 1])
                if random_chance == 0:
                    final_labels.append(label)
                    label_dict[label] += 1
                elif random_chance == 1:
                    final_labels.append(label_list_2[count])
                    label_dict[label_list_2[count]] += 1
    print(len(final_labels))


main()

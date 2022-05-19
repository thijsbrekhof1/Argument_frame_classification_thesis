import random
import pandas as pd
import numpy as np

def get_id(data):
    return data.get('id')


def check_distribution(labels):
    label_dict = {}
    for count, label in enumerate(labels):
        if label in label_dict.keys():
            label_dict[label] += 1
        else:
            label_dict[label] = 1

    return label_dict, dict(sorted(label_dict.items(), key=lambda x: x[1], reverse=True))

def main():
    df_thijs = pd.read_csv("all_annot_thijs.csv")
    df_nils = pd.read_csv("all_annot_nils.csv")

    # Sorting and removing pilot annotations for thijs
    df_thijs = df_thijs.sort_values('id')
    # Getting the pilot annot for thijs
    pilot_annot_thijs = df_thijs[df_thijs.id < 478]
    pilot_annot_thijs = pilot_annot_thijs.where(pd.notnull(pilot_annot_thijs), None)
    thijs_pilot_labels = pilot_annot_thijs['topic'].tolist()
    # all other annots for thijs
    df_thijs = df_thijs[df_thijs.id > 477]
    df_thijs = df_thijs[df_thijs.id < 1434]
    # Sorting and removing pilot annotations for nils
    df_nils = df_nils.sort_values('id')
    # Getting the pilot annot for nils
    pilot_annot_nils = df_nils[df_nils.id < 478]
    pilot_annot_nils = pilot_annot_nils.where(pd.notnull(pilot_annot_nils), None)
    nils_pilot_labels = pilot_annot_nils['topic'].tolist()
    # all other annots for nils
    df_nils = df_nils[df_nils.id > 477]

    # merging both dfs
    merged_df = df_thijs.append(df_nils)
    merged_df = merged_df.where(pd.notnull(merged_df), None)
    # Checking distribution of labels
    all_labels = merged_df['topic'].tolist()
    label_dict, sorted_labels = check_distribution(all_labels)
    print(sorted_labels)
    print(len(all_labels))

    # Choosing what label to pick between annotator 1 and annotator 2's labels
    pilot_labels_total = []
    for count, label in enumerate(thijs_pilot_labels):
        try:
            if label == nils_pilot_labels[count]:
                pilot_labels_total.append(label)
            elif label == "Other" and nils_pilot_labels[count] != "Other":
                pilot_labels_total.append(nils_pilot_labels[count])
            elif label != "Other" and nils_pilot_labels[count] == "Other":
                pilot_labels_total.append(label)
            else:
                count1 = label_dict[label]
                count2 = label_dict[nils_pilot_labels[count]]
                if count1 < count2:
                    pilot_labels_total.append(label)
                    label_dict[label] += 1
                elif count1 > count2:
                    pilot_labels_total.append(nils_pilot_labels[count])
                    label_dict[nils_pilot_labels[count]] += 1
                elif count1 == count2:
                    random_chance = random.choice([0, 1])
                    if random_chance == 0:
                        pilot_labels_total.append(label)
                        label_dict[label] += 1
                    elif random_chance == 1:
                        pilot_labels_total.append(nils_pilot_labels[count])
                        label_dict[nils_pilot_labels[count]] += 1
        except IndexError:
            label2 = None
            if label == label2:
                pilot_labels_total.append(label)
            elif label == "Other" and label2 != "Other":
                pilot_labels_total.append(label2)
            elif label != "Other" and label2 == "Other":
                pilot_labels_total.append(label)
            else:
                count1 = label_dict[label]
                count2 = label_dict[label2]
                if count1 < count2:
                    pilot_labels_total.append(label)
                    label_dict[label] += 1
                elif count1 > count2:
                    pilot_labels_total.append(label2)
                    label_dict[label2] += 1
                elif count1 == count2:
                    random_chance = random.choice([0, 1])
                    if random_chance == 0:
                        pilot_labels_total.append(label)
                        label_dict[label] += 1
                    elif random_chance == 1:
                        pilot_labels_total.append(label2)
                        label_dict[label2] += 1


    # Assigning the labels to a df
    pilot_annot_thijs.drop('topic', axis=1, inplace=True)
    pilot_annot_thijs['topic'] = pilot_labels_total

    final_df = pilot_annot_thijs.append(merged_df)
    final_df = final_df[final_df.topic.notnull()]
    final_df = final_df[final_df.topic != "Irrelevant"]
    # Checking distribution of final labels
    final_labels = final_df['topic'].tolist()
    label_dict, sorted_labels = check_distribution(final_labels)
    print(sorted_labels)
    print(len(final_labels))


    final_df.to_csv("all annotations.csv")


main()

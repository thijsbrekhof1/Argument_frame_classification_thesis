import random
import pandas as pd


def get_id(data):
    return data.get('id')


def main():
    df_thijs = pd.read_csv("all_annot_thijs.csv")
    df_nils = pd.read_csv("all_annot_thijs.csv")

    # Sorting and removing pilot annotations for thijs
    df_thijs = df_thijs.sort_values('id')
    # Getting the pilot annot for thijs
    pilot_annot_thijs = df_thijs[df_thijs.id < 478]
    thijs_pilot_labels = pilot_annot_thijs['topic'].tolist()
    # all other annots for thijs
    df_thijs = df_thijs[df_thijs.id > 477]

    # Sorting and removing pilot annotations for nils
    df_nils = df_nils.sort_values('id')
    # Getting the pilot annot for nils
    pilot_annot_nils = df_nils[df_nils.id < 478]
    nils_pilot_labels = pilot_annot_nils['topic'].tolist()
    # all other annots for nils
    df_nils = df_nils[df_nils.id > 477]

    # merging both dfs
    merged_df = df_thijs.merge(df_nils)
    all_labels = merged_df['topic'].tolist()

    label_dict = {}
    for count, label in enumerate(all_labels):
        if label in label_dict.keys():
            label_dict[label] += 1
        else:
            label_dict[label] = 1

    # This code is for checking the distribution of labels
    print(label_dict)
    print(dict(sorted(label_dict.items(), key=lambda x: x[1], reverse=True)))
    count = 0
    for i in label_dict.values():
        count += i
    print(count)

    # Choosing what label to pick between annotator 1 and annotator 2's labels
    final_labels = []
    for count, label in enumerate(thijs_pilot_labels):
        if label == nils_pilot_labels[count]:
            final_labels.append(label)
        elif label == "Other" and nils_pilot_labels[count] != "Other":
            final_labels.append(nils_pilot_labels[count])
        elif label != "Other" and nils_pilot_labels[count] == "Other":
            final_labels.append(label)
        else:
            count1 = label_dict[label]
            count2 = label_dict[nils_pilot_labels[count]]
            if count1 < count2:
                final_labels.append(label)
                label_dict[label] += 1
            elif count1 > count2:
                final_labels.append(nils_pilot_labels[count])
                label_dict[nils_pilot_labels[count]] += 1
            elif count1 == count2:
                random_chance = random.choice([0, 1])
                if random_chance == 0:
                    final_labels.append(label)
                    label_dict[label] += 1
                elif random_chance == 1:
                    final_labels.append(nils_pilot_labels[count])
                    label_dict[nils_pilot_labels[count]] += 1

    print(len(final_labels))

    # Assigning the labels to a df
    pilot_annot_thijs.drop('topic', axis=1, inplace=True)
    pilot_annot_thijs['topic'] = final_labels

    final_df = pilot_annot_thijs.append(merged_df)

    final_df.to_csv("all annotations.csv")

main()

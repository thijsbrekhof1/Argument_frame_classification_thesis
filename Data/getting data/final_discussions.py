import csv
import jsonlines


with open("filtered_threads - Possible topics.csv", encoding="utf8") as discussions:
    reader = csv.reader(discussions)

    post_list = []
    for row in reader:
        if row[11] == "possible_topic":

            post_list.append(row[7])
final_discussions = []
with jsonlines.open('filtered_threads2.jsonl') as reader:
    for post in reader:
        if post["id"] in post_list:
            final_discussions.append(post)

with jsonlines.open('filtered_threads_final.jsonl', mode='w') as writer:
    writer.write_all(final_discussions)

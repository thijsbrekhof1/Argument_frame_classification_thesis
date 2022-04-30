import pandas as pd

df = pd.read_json(path_or_buf='threads.jsonl', lines=True, nrows=10000)

for i in df["comments"]:
    if i[0]["body"] != "[deleted]":

        print(i[0]["level"])


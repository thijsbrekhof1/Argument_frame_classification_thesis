import csv
import pandas as pd


l = []
with open("frame annotation v5.csv", encoding="utf8") as frames_csv:
    reader = csv.reader(frames_csv)

    for row in reader:
        if row[0] != "":
            l.append([row[0]])

df = pd.DataFrame(l)

df.to_csv("frame annotation v6.csv")

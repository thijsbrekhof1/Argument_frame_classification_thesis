import csv
import pandas as pd

l = []
with open("All temporary states of frames be4 clustering/frame annotation v4.csv", encoding="utf8") as frames_csv:
    reader = csv.reader(frames_csv)

    for row in reader:
        if row[3] == "":

            if row[4] != "":
                l.append(row[4])
            else:
                l.append(row[1])

df = pd.DataFrame(l[1:])

df.to_csv("final_frames.csv")

# Author: Thijs Brekhof
import csv


def get_frames():
    with open("Webis-argument-framing.csv", encoding="utf8") as frames_csv:
        reader = csv.reader(frames_csv)

        all_frames = set()

        for row in reader:
            all_frames.add(row[2])
        # for frame in all_frames:
        #     print(frame)
        return all_frames


def main():
    frames = get_frames()
    with open("all_frames.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(frames)


if __name__ == "__main__":
    main()

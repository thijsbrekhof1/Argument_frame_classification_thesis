import jsonlines
from langdetect import detect

with jsonlines.open('filtered_threads2.jsonl') as reader:
    for discussion in reader:
        for i in discussion:
            if i == "comments":
                for ii in discussion[i]:
                    # print(ii['body'])
                    lang = detect(ii['body'])
                    if lang != "en":
                        print(lang)
            else:
                pass
                # print("{0}:\t-\t{1}".format(i, discussion[i]))

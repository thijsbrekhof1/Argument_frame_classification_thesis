#!/usr/bin/python3
# File Name: 
# Author: S. Wijnen S3153281

import sys
import json
import csv


def main():
    with open('filtered_threads_final.json', encoding='utf8') as json_file:
        data = json.load(json_file)

    with open('comments_for_anno.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        header = ['thread_id', 'comment_text', 'comment_id', 'thread_title']
        writer.writerow(header)

        for thread in data:
            thread_title, thread_score, thread_created_utc, thread_author, thread_url, thread_id = thread['title'], \
                                                                                                   thread['score'], \
                                                                                                   thread[
                                                                                                       'created_utc'], \
                                                                                                   thread['author'], \
                                                                                                   thread['url'], \
                                                                                                   thread['id']
            thread_comments = thread['comments']

            for comment in thread_comments:
                comment_body, comment_author, comment_controversiality, comment_score, comment_created_utc, comment_id = \
                comment['body'], comment['author'], comment['controversiality'], comment['score'], comment[
                    'created_utc'], comment['id']

                row = [thread_id, comment_body, comment_id, thread_title]
                writer.writerow(row)


if __name__ == "__main__":
    main()

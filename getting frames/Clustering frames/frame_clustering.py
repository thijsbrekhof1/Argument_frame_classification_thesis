import csv
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import pandas as pd


def freq(lst):
    d = {}
    for i in lst:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    return d


def get_embeddings(frames):
    # model = SentenceTransformer('all-MiniLM-L6-v2')
    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
    embeddings = model.encode(frames)

    return embeddings


def get_frames():
    frame_l = []

    with open("All temporary states of frames be4 clustering/final_frames.csv", encoding="utf8") as frames:
        reader = csv.reader(frames)

        for row in reader:
            frame_l.append(row[1])

    return frame_l[1:]


def calculate_WSS(points, kmax):
    sse = []
    for k in range(1, kmax + 1):
        kmeans = KMeans(n_clusters=k).fit(points)
        centroids = kmeans.cluster_centers_
        pred_clusters = kmeans.predict(points)
        curr_sse = 0

        # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
        for i in range(len(points)):
            curr_center = centroids[pred_clusters[i]]
            curr_sse += (points[i, 0] - curr_center[0]) ** 2 + (points[i, 1] - curr_center[1]) ** 2

        sse.append(curr_sse)
    return sse


def main():
    frames = get_frames()
    # To check embedding per frame, uncomment the prints
    # for sentence, embedding in zip(frames, embeddings):
    #     print("Sentence:", sentence)
    #     print("Embedding:", embedding)
    #     print("")

    embeddings = get_embeddings(frames)
    # Checking best number of clusters
    # max_k = 20
    # wss = calculate_WSS(embeddings, max_k)
    #
    # fig, ax = plt.subplots()
    #
    # ax.plot(wss)
    # plt.xticks(range(0, max_k+1))
    # plt.show()

    # sil = []
    # for k in range(2, max_k + 1):
    #     kmeans = KMeans(n_clusters=k).fit(embeddings)
    #     labels = kmeans.labels_
    #     sil.append(silhouette_score(embeddings, labels, metric='euclidean'))
    #
    # fig, ax = plt.subplots()
    #
    # ax.plot(sil)
    # plt.xticks(range(0, max_k+1))
    # plt.show()

    # # Implementing K-Means
    cluster_dict = {}
    num_clusters = 100
    # Define kmeans model
    clustering_model = KMeans(n_clusters=num_clusters, random_state=123)
    # Fit the embedding with kmeans clustering.
    clustering_model.fit(embeddings)
    # Get the cluster id assigned to each news headline.
    cluster_assignment = clustering_model.labels_

    clustered_sentences = [[] for i in range(num_clusters)]
    for sentence_id, cluster_id in enumerate(cluster_assignment):
        clustered_sentences[cluster_id].append(frames[sentence_id])

    for i, cluster in enumerate(clustered_sentences):
        cluster_dict["Cluster", i] = cluster
        # print("Cluster ", i + 1)
        # print(cluster)
        # print("")

    df = pd.DataFrame(columns=["Cluster", "Frames"])
    for key in cluster_dict.keys():
        df = df.append({"Cluster": key, "Frames": cluster_dict[key]}, ignore_index=True)

    df.to_csv("100_clusters.csv")

main()

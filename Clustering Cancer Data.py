import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import math

K = 2 # number of clusters

def dataAsLists():
    path = "cancer.csv.txt"
    df = pd.read_csv(path, index_col=0)
    K = 2  # number of clusters
    lines = []
    with open('cancer.csv.txt', 'r') as da:
        lines = da.readlines()
        lines = [x.strip() for x in lines]
    length = len(lines)
    n = 0
    list2 = []

    for m in range(length):
        a = lines[n]  # holds a string
        a = a.split(',')
        list1 = list(a)
        if a != "":
            del list1[0]
            n += 1  # number of rows
            delimiter = ','  # empty string
            a = delimiter.join(list1)
            list2.append(a)

    return list2


def clusterAnalysis():
    length = 78
    n = 78
    list_of_samples = []
    myList = dataAsLists()
    for m in range(length):
        list_of_samples.append(myList[m])

    new_list = myList

    c1 = []
    c2 = []
    clusters = [c1, c2]

    while new_list:
        a = np.random.randint(0, n)
        random_sample = new_list[a]  # store random sample in list
        c1.append(random_sample)
        del new_list[a]
        n -= 1
        a = np.random.randint(0, n)
        random_sample = new_list[a]  # store random sample in list
        c2.append(random_sample)
        del new_list[a]
        n -= 1

    clust_list1 = c1
    for i in range(len(clust_list1)):
        d = clust_list1[i].split(",")
        for m in range(len(d)):
            d[m] = float(d[m])
        clust_list1[i] = d
    centroid1 = np.mean(clust_list1, axis=0)  # calculate centroid of cluster 1

    clust_list2 = c2
    for i in range(len(clust_list2)):
        d = clust_list2[i].split(",")
        for m in range(len(d)):
            d[m] = float(d[m])  # convert the strings to floats
        clust_list2[i] = d
    centroid2 = np.mean(clust_list2, axis=0)  # calculate centroid of cluster 2

    distance_list_c1 = []
    distance_list_c2 = []

    for i in range(length):  # Change samples values from strings to floats
        d = list_of_samples[i].split(",")
        for m in range(len(d)):
            d[m] = float(d[m])
        list_of_samples[i] = d

    centroid_old1 = np.zeros((K, length))
    centroid_old2 = np.zeros((K, length))
    a = 0
    new_clust_list1 = []
    new_clust_list2 = []
    old_clust_list1 = clust_list1.copy()
    old_clust_list2 = clust_list2.copy()

    while old_clust_list1 != new_clust_list1 and old_clust_list2 != new_clust_list2:
        a += 1
        temp1 = []
        temp2 = []
        for m in range(length):  # assinging samples to clusters
            distance_c1 = Euclidean(centroid1, list_of_samples[m])
            distance_list_c1.append(distance_c1)
            distance_c2 = Euclidean(centroid2, list_of_samples[m])
            distance_list_c2.append(distance_c2)
            if distance_list_c1[m] < distance_list_c2[m]:  # if distance from clust1 is less than clust2
                temp1.append(list_of_samples[m])  # assign sample to cluster1
            else:
                temp2.append(list_of_samples[m])  # assign sample to cluster2
        new_clust_list1 = temp1
        new_clust_list2 = temp2
        distance_list_c1 = []
        distance_list_c2 = []
        centroid1 = np.mean(new_clust_list1, axis=0)  # recompute each clusters centroid values
        centroid2 = np.mean(new_clust_list2, axis=0)
        if old_clust_list1 == new_clust_list1 and old_clust_list2 == new_clust_list2:
            break
        else:
            old_clust_list1 = new_clust_list1.copy()
            old_clust_list2 = new_clust_list2.copy()
            new_clust_list1 = []
            new_clust_list2 = []

    return new_clust_list1, new_clust_list2, list_of_samples


def Euclidean(vector1, vector2):
    dist = [(a - b) ** 2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    return dist


def plotting():
    # Plotting
    lists = clusterAnalysis()
    new_data = lists[0] + lists[1]
    mp.imshow(lists[2], cmap='RdBu')  # original dataset plot
    mp.title('original data plot')
    mp.colorbar()
    mp.show()

    mp.imshow(new_data, cmap='RdBu')  # clustered dataset plot
    mp.title('clustered data plot')
    mp.colorbar()
    mp.show()


plotting()

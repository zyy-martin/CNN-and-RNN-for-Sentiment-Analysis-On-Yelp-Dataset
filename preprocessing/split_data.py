import csv
import random
import numpy


data = []
data_vali = []
ratings = [0,0,0,0,0]
#
# with open('restaurant_review.csv', 'rt') as f:
#     reader = csv.reader(f, delimiter=',')
#     i = 0
#     for row in reader:
#         if i == 0:
#             header.append(row)
#             i += 1
#             continue
#         data.append(row)
# random.shuffle(data)
# data = header + data
#
#
# with open('review_100k_train.csv', 'wt') as f:
#     writer = csv.writer(f, delimiter=',')
#     for i in range(100000):
#         writer.writerow(data[i])
#
#
# with open('review_20k_valid.csv', 'wt') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(data[0])
#     for i in range(100000, 120000):
#         writer.writerow(data[i])
#
#
# with open('review_20k_test.csv', 'wt') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(data[0])
#     for i in range(120000, 140000):
#         writer.writerow(data[i])

#
# with open('review_100k_train.csv','rt') as f:
#     reader = csv.reader(f, delimiter=',')
#     i = 0
#     for row in reader:
#         if i == 0:
#             i += 1
#             header=row
#             continue
#         rating = int(row[3])-1
#         if ratings[rating] >= 2000:
#             continue
#         else:
#             ratings[int(row[3])-1] += 1
#             data.append(row)



with open('review_20k_valid.csv','rt') as f:
    reader = csv.reader(f, delimiter=',')
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            header=row
            continue
        rating = int(row[3])-1
        if ratings[rating] >= 800:
            continue
        else:
            ratings[int(row[3])-1] += 1
            data_vali.append(row)


print(len(data_vali))

# with open('balanced_10k_train.csv','wt') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(header)
#     for i in range(10000):
#         writer.writerow(data[i])
#
with open('balanced_4k_vali.csv','wt') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)
    for i in range(4000):
        writer.writerow(data_vali[i])




import csv
import numpy as np

class data_reader:

    def read(self, dir='vali_data_rev.csv'):
        print('loading ',dir,'...')
        reviews = []
        self.lengths = []
        self.ratings = []
        with open(dir, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                id = line[0]
                size = line[1]
                rating = line[2]
                if id != '':
                    self.lengths.append(int(size))
                    self.ratings.append(int(rating)-1)
                reviews.append(line[3:])
        self.data = np.zeros((len(self.lengths), 100, 300))
        for i in range(len(self.lengths)):
            self.data[i, :] = reviews[i*100: (i+1)*100]
        self.lengths = np.array(self.lengths)
        self.ratings = np.array(self.ratings)
        one_hot = np.zeros((self.ratings.shape[0], 5))
        for i in range(len(self.ratings)):
            one_hot[i, self.ratings[i]] = 1
        self.ratings = one_hot

    def next_batch(self, batch_size=10, whole=False):
        if whole == False:
            new_indices = np.random.permutation(self.data.shape[0])
            new_indices = new_indices[:batch_size]
            return self.data[new_indices, :], self.ratings[new_indices], self.lengths[new_indices]
        else:
            return self.data, self.ratings



# reader = data_reader()
# reader.read()
# data, rating, length = reader.next_batch()
# print(rating, length)
# data, rating, length = reader.next_batch()
# print(rating, length)
# data, rating, length = reader.next_batch()
# print(rating, length)


# a = np.array([[1,2,3],[4,2,3]])
# b = [0,1]
# print(a[:,b])






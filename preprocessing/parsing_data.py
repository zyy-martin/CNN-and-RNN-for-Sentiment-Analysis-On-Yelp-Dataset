import json
import csv
import psycopg2
conn = psycopg2.connect("dbname='yelp' user='Martin' host='localhost' ")
cur = conn.cursor()

# business =[]
# with open('yelp_dataset_challenge_round9/yelp_academic_dataset_business.json','rt') as b:
#     for line in b:
#         business.append(json.loads(line))




# for item in business:
#     if str(item['categories']).find('Restaurant') >= 0:
#         cur.execute("INSERT INTO business (business_id, name, neighborhood, address, city, state, postal_code, "
#                 "latitude, longitude, stars, review_count, is_open, attributes, category, hours, type) values"
#                 "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#                 (item['business_id'], item['name'], item['neighborhood'], item['address'],
#                  item['city'], item['state'], item['postal_code'], item['latitude'],
#                  item['longitude'], item['stars'], item['review_count'], item['is_open'],
#                  str(item['attributes']), str(item['categories']), str(item['hours']), item['type']))
# conn.commit()



# check_in = []
# with open('yelp_dataset_challenge_round9/yelp_academic_dataset_checkin.json','rt') as b:
#     for line in b:
#         check_in.append(json.loads(line))
#
# review = []
# with open('yelp_dataset_challenge_round9/yelp_academic_dataset_review.json','rt') as b:
#     for line in b:
#         review.append(json.loads(line))
#
# for item in review:
#     cur.execute("INSERT INTO review (review_id, user_id, business_id, stars, date, text, useful, funny, cool, type) values"
#                         "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#                         (item['review_id'], item['user_id'], item['business_id'], item['stars'],
#                          item['date'], item['text'], item['useful'], item['funny'],
#                          item['cool'], item['type']))
# conn.commit()


# tip = []
# with open('yelp_dataset_challenge_round9/yelp_academic_dataset_tip.json','rt') as b:
#     for line in b:
#         tip.append(json.loads(line))
#
# user = []
# with open('yelp_dataset_challenge_round9/yelp_academic_dataset_user.json','rt') as b:
#     for line in b:
#         user.append(json.loads(line))



cur.execute("SELECT * FROM restuarant_review ORDER BY business_id;")
i = 0
with open('restuarant_review.csv','wt') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['review_id','user_id','business_id','stars','date','text','useful','funny','cool','type'])
    for item in cur:
        print(i)
        i += 1
        writer.writerow(item)






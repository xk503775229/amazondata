
with open('/Users/kangxiao/PycharmProjects/first/amazon_data/new_oneAmazon/english_total_comments.txt','r') as fip1:
    count = 0
    for i in fip1.readlines():
        count += 1
        if count == 16294:
         print(i)
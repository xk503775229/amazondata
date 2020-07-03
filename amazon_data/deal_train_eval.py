

if __name__ == '__main__':
    train_data = []
    eval_data = []

    count = 0
    with open('/Users/kangxiao/PycharmProjects/first/amazon_data/total_comments_amazon_flags.txt',
              'r') as fip1:
        for i in fip1.readlines():
            count  += 1
            if count%5 != 0:
                train_data.append(i.strip())
            else:
                eval_data.append(i.strip())

            if count == 15000:
                break
    print(len(train_data))
    print(len(eval_data))
    with open('/Users/kangxiao/PycharmProjects/first/amazon_data/train_comments_amazon_flags.txt',
              'w') as fip2:
        for data in train_data:
            fip2.write(data+'\n')
    with open('/Users/kangxiao/PycharmProjects/first/amazon_data/eval_comments_amazon_flags.txt',
              'w') as fip3:
        for data2 in eval_data:
            fip3.write(data2+'\n')
        
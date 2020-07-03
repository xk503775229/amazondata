import nltk

def readData():
    name = '/Users/kangxiao/PycharmProjects/first/amazon_data/new_oneAmazon/english_total_questions.txt'
    comments = []
    with open(name,'r') as fip:



        for line in fip.readlines():
            temp = ''
            tokens = nltk.word_tokenize(line)
            for i in tokens:
                temp = temp + i + ' '

                # if i not in vocab:
                #     vocab[i] = 1
                # else:
                #     vocab[i] += 1


            # tagged = nltk.pos_tag(tokens)
            comments.append(temp)
            print(temp)
            # fip2.write(temp+'\n')
        return comments

if __name__ == '__main__':
    vocab = {}
    flags = []
    with open('/Users/kangxiao/PycharmProjects/first/amazon_data/total_comments_amazon.txt',
              'r') as fip1:
        for i in fip1.readlines():
            words = i.strip().split()
            tagged = nltk.pos_tag(words)
            print(tagged)
            temp = ''
            for word, pos in tagged:
                if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS':
                    temp = temp + str(1) + ' '
                else:
                    temp = temp + str(0) + ' '
            flags.append(temp)
            print(temp)
    with open('/Users/kangxiao/PycharmProjects/first/amazon_data/total_comments_amazon_flags.txt',
              'w') as fip2:
        for i in flags:
            fip2.write(i+'\n')
    #         for word in words:
    #             if word not in vocab:
    #                 vocab[word] = 1
    #             else:
    #                 vocab[word] += 1
    # with open('/Users/kangxiao/PycharmProjects/first/amazon_data/total_questions_amazon.txt',
    #           'r') as fip2:
    #     for i in fip2.readlines():
    #         words = i.strip().split()
    #         print(words)
    #         for word in words:
    #             if word not in vocab:
    #                 vocab[word] = 1
    #             else:
    #                 vocab[word] += 1
    # vocab =sorted(vocab.items(),key=lambda x:x[1],reverse=True)
    # print(vocab[0])
    # with open('/Users/kangxiao/PycharmProjects/first/amazon_data/english_vocab',
    #           'w') as fip3:
    #     for i in vocab:
    #         fip3.write(str(i[0])+' '+str(i[1])+'\n')



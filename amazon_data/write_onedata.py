import json

def read_data2(fip):
    questions =[]
    comments = []
    fip = open('/Users/kangxiao/PycharmProjects/first/amazon_data/dataQueCom/'+fip+'.json','r')
    for line in fip.readlines():
        #print(type(line))  # <class 'str'>
        result = json.loads(line)
        print(result['question'])
        #print(result)

        comment_list = eval(result['comments'])
        temp = ''
        for comment in comment_list:

            if float(comment[1]) > 0.5:
                temp = temp  + comment[0].strip('\n')
        if len(temp) != 0:
            comments.append(str(temp))
            questions.append(str(result['question']))

        # for i in list(result['comments']):
        #     print(i)
    fip.close()
            #print(result)
    return questions, comments

if __name__ == '__main__':
    name = 'PetSupplies'
    questions, comments = read_data2(name)
    print(len(questions))
    with open('/Users/kangxiao/PycharmProjects/first/amazon_data/new_oneAmazon/'+name+'_question.txt','w') as fip1:
        for item in questions:

            fip1.write(item+'\n')
    with open('/Users/kangxiao/PycharmProjects/first/amazon_data/new_oneAmazon/' + name + '_comments.txt',
              'w') as fip2:
        for item2 in comments:
            fip2.write(item2+'\n')


def read_data(fip):
    while True:
        line = fip.readline()
        line = line.strip('\n')
        if len(line) == 0:  # See https://github.com/abisee/pointer-generator/issues/1
            tf.logging.warning('Found an example with empty article text. Skipping it.')
            self._finished_reading = True
            break
        else:
            yield line
def fill_example_queue2():
    """Reads data from file and processes into Examples which are then placed into the example queue."""
    # 改这里
    # comm = open('/data/kxiao/flag_add/amazon_data/train_comments_amazon.txt','r')
    # ques = open('/data/kxiao/flag_add/amazon_data/train_questions_amazon.txt', 'r')
    # flag = open('/data/kxiao/flag_add/amazon_data/train_comments_amazon_flags.txt', 'r')
    comm = open('/Users/kangxiao/PycharmProjects/first/amazon_data/eval_comments_amazon.txt','r')
    ques = open('/Users/kangxiao/PycharmProjects/first/amazon_data/eval_questions_amazon.txt', 'r')
    flag = open('/Users/kangxiao/PycharmProjects/first/amazon_data/eval_comments_amazon_flags.txt', 'r')

    while True:
      try:
        article = next(read_data(comm))
        abstract_sentences = next(read_data(ques))
        print(abstract_sentences)
        # abstract = ' '.join(abstract_sentences)
        # print(abstract)
        # 加flag
        print(article)
        flags = next(read_data(flag))
        print(flags)
        break
      except StopIteration:  # if there are no more examples:
        tf.logging.info("The example generator for this example queue filling thread has exhausted data.")
if __name__ == '__main__':
    fill_example_queue2()

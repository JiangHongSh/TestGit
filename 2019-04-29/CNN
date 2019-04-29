import os
import tensorflow.contrib.keras as kr
from cnn.cnews_loader import open_file
from cnn.cnn_model import TCNNConfig, TextCNN

import numpy as np
import tensorflow as tf

def cnn(content):
    #tf.reset_default_graph()
    config = TCNNConfig()
    model = TextCNN(config)
    save_dir = 'cnn/checkpoints/textcnn'
    save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径

    contents = []
    contents.append(content)
    vocab_dir = os.path.join('cnn/cnews.vocab.txt')

    with open_file(vocab_dir) as fp:
        # 如果是py2 则每个值都转化为unicode
        words = [_.strip() for _ in fp.readlines()]
    word_to_id = dict(zip(words, range(len(words))))

    categories = ['1', '2', '3', '4']
    categories = [x for x in categories]
    cat_to_id = dict(zip(categories, range(len(categories))))

    data_id, label_id = [], []
    for i in range(len(contents)):
        data_id.append([word_to_id[x] for x in contents[i] if x in word_to_id])
        # label_id.append(cat_to_id[labels[i]])

    max_length = 600
    x_pad = kr.preprocessing.sequence.pad_sequences(data_id, max_length)
    x_test = x_pad

    session = tf.Session()
    session.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess=session, save_path=save_path)  # 读取保存的模型

    print(x_test)

    batch_size = 128
    data_len = len(x_test)
    num_batch = int((data_len - 1) / batch_size) + 1

    y_pred_cls = np.zeros(shape=len(x_test), dtype=np.int32)  # 保存预测结果 返回：返回来一个给定形状和类型的用0填充的数组
    for i in range(num_batch):  # 逐批次处理
        start_id = i * batch_size
        end_id = min((i + 1) * batch_size, data_len)
        feed_dict = {
            model.input_x: x_test[start_id:end_id],
            model.keep_prob: 1.0
        }
        y_pred_cls[start_id:end_id] = session.run(model.y_pred_cls, feed_dict=feed_dict)
    print(y_pred_cls)
    return y_pred_cls

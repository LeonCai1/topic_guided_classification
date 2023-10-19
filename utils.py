import argparse
import os
import csv
import numpy as np
from tqdm import tqdm
import nltk

nltk.download('punkt')
from nltk import word_tokenize
import re


def phrase_process():
    f = open(os.path.join(args.dataset, args.in_file))
    g = open(args.out_file, 'w')
    for line in tqdm(f):
        doc = ''
        temp = re.split("<phrase_Q=\d+\.\d{3}>", line)
        for seg in temp:
            temp2 = seg.split('</phrase>')
            if len(temp2) > 1:
                doc += ('_').join(temp2[0].split(' ')) + temp2[1]
            else:
                doc += temp2[0]
        g.write(doc.strip() + '\n')
    print("Phrase segmented corpus written to {}".format(args.out_file))
    return


def preprocess():
    f = open(os.path.join(args.dataset, args.in_file))
    docs = f.readlines()
    f_out = open(args.out_file, 'w')
    for doc in tqdm(docs):
        f_out.write(' '.join([w.lower() for w in word_tokenize(doc.strip())]) + '\n')
    return

def category_terms():
    dataset = 'movies'
    file_path = f'./data/{dataset}_cate/'
    cate_emb_dict = {}
    f = open(file_path + f'emb_{dataset}_category_t.txt')
    for index, line in enumerate(f):
        if index == 0:
            continue
        temp = line.split()
        cate_emb_dict[temp[0]] = ' '.join(temp[1:])
    cate_rep = {}
    f = open(file_path + f'res_{dataset}_category.txt')
    pre = None
    for line in f:
        tmp = line.split()
        if tmp[0] == 'Category':
            pre = line[len('Category ('): -3]
        else:
            cate_rep[pre] = line
    f = open(file_path + f'emb_{dataset}_category_w.txt')
    rep_dict = {}
    for idx, line in enumerate(f):
        if idx == 0:
            continue
        tmp = line.split()
        rep_dict[tmp[0]] = line

    for category in cate_emb_dict:
        f_out = open(file_path + f'{category}_terms.txt', 'w')
        f_out.write(category + ' ' + cate_emb_dict[category] + '\n')
        for repr in cate_rep[category].split():
            f_out.write(rep_dict[repr])


category_terms()
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='main', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#     parser.add_argument('--mode', type=int, default=-1)
#     parser.add_argument('--dataset', default='NEW')
#     parser.add_argument('--in_file', default='text.txt')
#     parser.add_argument('--out_file', default='./AutoPhrase/data/text.txt')
#     args = parser.parse_args()
#     if args.mode == 0:
#         preprocess()
#     else:
#         phrase_process()

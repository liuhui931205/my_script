import os


def down_test_data(down_path):
    path_list = []
    with open('/data/deeplearning/train_platform/data/gerneral_20180817/kd_all_test.lst', 'r') as f:
        data = f.readlines()
    for i in data:
        s = i.split('\t')
        path_list.append(s[2])

    for j in path_list:
        q = j.split('/')
        name = q[-1]

        open(os.path.join(down_path, name), "wb").write(open(j, "rb").read())


if __name__ == '__main__':
    down_path = '/data/deeplearning/train_platform/eva_sour_data/test_data/general'
    down_test_data(down_path)

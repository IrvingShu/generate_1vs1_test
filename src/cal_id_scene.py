import os
import sys
import matio
import argparse
import numpy as np

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--feature-root-folder', type=str, help='feature root folder')
    parser.add_argument('--gallery-list-path', type=str, help='feature list path')
    parser.add_argument('--probe-list-path', type=str, help='feature list path')
    parser.add_argument('--score-save-path', type=str, help='score saved path')
    
    return parser.parse_args(argv)

def read_feature(fea_root, path):
    fea_dict = dict()
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            full_path = os.path.join(fea_root, line.strip())
            x_vec = matio.load_mat(full_path).flatten()
            fea_dict[line.strip()] = x_vec
    return fea_dict

def cal_loop_sim(gallery_fea, probe_fea):
    same_people = []
    diff_people = []
    for key in probe_fea:
        same_pair = []
        diff_pair = []
        max_sim_same = 0.0
        max_sim_same_name = ''
        max_sim_diff = 0.0
        max_sim_diff_name = ''
        for key2 in gallery_fea:
            sim = np.dot(probe_fea[key], gallery_fea[key2]) / (np.linalg.norm(probe_fea[key], ord=2) * np.linalg.norm(gallery_fea[key2], ord=2))
            probe_label = key.split('/')[1]
            gallery_label = key2.split('/')[1]
            if probe_label == gallery_label:
                if sim > max_sim_same:
                    max_sim_same = sim
                    max_sim_same_name = key2.split('_')[0]
            else:
                if sim > max_sim_diff:
                    max_sim_diff = sim
                    max_sim_diff_name = key2.split('_')[0]

        same_pair.append(key.split('_')[0])
        same_pair.append(max_sim_same_name)
        same_pair.append(max_sim_same)
        diff_pair.append(key.split('_')[0])
        diff_pair.append(max_sim_diff_name)
        diff_pair.append(max_sim_diff)
        same_people.append(same_pair)
        diff_people.append(diff_pair)
        
    
    return same_people,diff_people

def main(args):
    print('===> args:\n', args)
    fea_root_folder = args.feature_root_folder
    gallery_list_path = args.gallery_list_path
    probe_list_path = args.probe_list_path
    score_save_path = args.score_save_path

    gallery_fea_dict = read_feature(fea_root_folder, gallery_list_path)
    probe_fea_dict = read_feature(fea_root_folder, probe_list_path)
    same_people, diff_people = cal_loop_sim(gallery_fea_dict, probe_fea_dict)
    print('same pleople: %d' %len(same_people))
    print('diff people: %d' %len(diff_people))

    with open(score_save_path, 'w') as f:
        for i in range(len(same_people)):
            f.write(same_people[i][0] + ' ' + same_people[i][1] + ' ' + str(same_people[i][2]) +'\n')


        for i in range(len(diff_people)):
            f.write(diff_people[i][0] + ' ' + diff_people[i][1] + ' ' + str(diff_people[i][2]) + '\n')
if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))

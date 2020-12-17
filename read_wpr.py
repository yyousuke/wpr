#!/usr/bin/env python3
import numpy as np
import pandas as pd
import struct
import sys
import os
import argparse
from datetime import datetime, timedelta


### デフォルト設定
# 入力、出力ディレクトリ
input_dir_default = "."
output_dir_default = "."
# 日付、地点
wpr_date_defalut = "20190504"
wpr_sta_defalut = "626"


class ReadWPR():
    def __init__(self, input_file):
        self.input_file = input_file

    def retrieve(self):
        # バイナリとして読み込み（1バイト毎に格納）
        with open(self.input_file, 'rb') as fin:
            r = fin.read()
        
        out = list()
        size = len(r)
        offset = 0
        chunk = 2
        while True:
            if offset > size:
                break
            try:
                # little endianの符号付き2バイト整数型
                #print(struct.unpack('<h', r[offset:offset+chunk]))
                out.extend( (struct.unpack('<h', r[offset:offset+chunk])) )
            except:
                print("Warn: invalid data size")
            offset += chunk
        print(out)
        print("num. of rec. = ", len(out))
        
        # 観測所番号
        num = ''.join( [str(x) for x in out[0:2]] )
        print("station = ", num)
        #print(out[0:2])
        # 緯度、経度
        lat = out[2] * 0.01
        lon = out[3] * 0.01
        # アンテナの標高
        z = out[4]
        print("longitude = ", lon, ", latitude = ", lat, ", height = ", z, "m")
        # 日付
        year = out[5]
        mon = out[6]
        day = out[7]
        print("date = ", year, "/", mon, "/", day)
        
        # 各時刻の観測層数(N)
        #print(out[8:100])
        num_layers = list()
        size = len(out)
        offset = 8
        chunk = 1
        while True:
            if offset + chunk - 1 > size:
                break
            if int(out[offset]) < 100:
                num_layers.extend(out[offset:offset+chunk])
            else:
                break
            offset += chunk
        num_times = len(num_layers)
        print(num_layers)
        
        # 観測値
        max_layers = np.array(num_layers).max() # 鉛直層の最大
        chunk = 6 # １層のデータが６
        data = np.zeros((num_times, max_layers, chunk))
        n = 0 # データ番号
        k = 0 # 鉛直層番号
        time = datetime(year, mon, day, 0, 10, 0)
        tindex = list()
        while True:
            print(time, offset)
            if offset + chunk - 1 > size:
                break
            if num_layers[n] > 0:
                inp = np.array(out[offset:offset+chunk])
                print(n, k, inp)
                if inp.shape[0] == chunk:
                    data[n,k,:] = inp[:]
                offset += chunk
                if num_layers[n] == max_layers:
                    nmax = n
            # 次のデータを読むための準備
            k += 1
            if k >= num_layers[n]:
                tindex.append(time)
                time += timedelta(minutes=10)
                n += 1
                k = 0
        
        #print(nmax)
        print(data[nmax,:,0], len(data[nmax,:,0]))
        #print(np.vstack(tindex), len(tindex))
        print(data)
        print(data[:,:,4].shape)
        return nmax, tindex, data


### options ###

# オプションの読み込み
def _construct_parser():
    parser = argparse.ArgumentParser(description='read WP data')
    parser.add_argument( '--wpr_date',
        type=str,
        help=('Date; yyyymmdd'),
        metavar='<wpr_date>'
    )
    parser.add_argument(
        '--wpr_sta',
        type=str,
        help=('Station number'),
        metavar='<wpr_sta>'
    )
    parser.add_argument(
        '--input_dir',
        type=str,
        help=('Path of input directory' ),
        metavar='<input_dir>'
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        help=('Path of output directory' ),
        metavar='<output_dir>'
    )

    return parser

def _parse_command(args):
    parser = _construct_parser()
    parsed_args = parser.parse_args(args[1:])
    if parsed_args.input_dir is None:
        parsed_args.input_dir = input_dir_default
    if parsed_args.output_dir is None:
        parsed_args.output_dir = output_dir_default
    if parsed_args.wpr_date is None:
        parsed_args.wpr_date = wpr_date_defalut
    if parsed_args.wpr_sta is None:
        parsed_args.wpr_sta = wpr_sta_defalut
    return parsed_args

### options ###


### utils ###

# path_to_dir: 作成するディレクトリ名
def os_mkdir(path_to_dir):
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)

### utils ###


if __name__ == '__main__':
    # オプションの読み込み
    args = _parse_command(sys.argv)
    # 日付、地点
    date = str(args.wpr_date)
    sta = str(args.wpr_sta)
    # 入出力ディレクトリ
    input_dir = args.input_dir
    output_dir = args.output_dir
    os_mkdir(output_dir) # 出力ディレクトリ作成
    # 入力ファイル名
    input_filename = "wpr" + date + "." + sta
    input_filedir = os.path.join(input_dir, input_filename)
    # 出力ファイル名
    output_filedir_qua = os.path.join(output_dir, "data_qua." + sta + ".csv")
    output_filedir_dir = os.path.join(output_dir, "data_dir." + sta + ".csv")
    output_filedir_spd = os.path.join(output_dir, "data_spd." + sta + ".csv")
    output_filedir_w = os.path.join(output_dir, "data_w." + sta + ".csv")
    output_filedir_height =  os.path.join(output_dir, "data_height." + sta + ".csv")
    output_filedir_time = os.path.join(output_dir, "data_time." + sta + ".csv")

    # ReadWPR Classの初期化
    wpr = ReadWPR(input_filedir)
    # ReadWPR.retrieveメソッドを使いデータの取得
    nmax, tindex, data = wpr.retrieve()

    # 時刻データ書き出し
    pd.Series(data[nmax,:,0]).to_csv(output_filedir_height, header=None)
    pd.Series(np.ravel(tindex)).to_csv(output_filedir_time, header=None)
    # 時間ー高度面のデータ書き出し
    data_qua = pd.DataFrame(data[:,:,1], index=tindex, columns=data[nmax,:,0])
    data_dir = pd.DataFrame(data[:,:,2], index=tindex, columns=data[nmax,:,0])
    data_spd = pd.DataFrame(data[:,:,3], index=tindex, columns=data[nmax,:,0])
    data_w   = pd.DataFrame(data[:,:,4], index=tindex, columns=data[nmax,:,0]) * 0.1
    data_qua.to_csv(output_filedir_qua)
    data_dir.to_csv(output_filedir_dir)
    data_spd.to_csv(output_filedir_spd) # [m/s]
    data_w.to_csv(output_filedir_w) # [m/s]


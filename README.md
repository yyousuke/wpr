
気象庁のウインドプロファイラデータを読み込み、matplotlibで作図を行うためのpythonプログラムです。

1. read_wpr.py
ウインドプロファイラデータを読み込み、csvファイルを書き出す

使用法：
./read_wpr.py 
  -h, --help            show this help message and exit
  --wpr_date <wpr_date>
                        Date; yyyymmdd
  --wpr_sta <wpr_sta>   Station number
  --input_dir <input_dir>
                        Path of input directory
  --output_dir <output_dir>
                        Path of output directory

Station numberはwpr_sta.csv

2. map_wpr.py
matplotlibを使い作図する


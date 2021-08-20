# wpr

気象業務支援センター提供のCDに収録された気象庁のウインドプロファイラデータを読み込み、matplotlibで作図を行うためのpythonプログラム

## 1. read_wpr.py

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

＊Station numberはwpr_sta.csv参照

## 2. map_wpr.py

matplotlibを使い作図する

地点番号（sta_id)をread_wpr.pyで書き出した地点に合わせ、作図時に表示される地点名（sta_name）やタイトル（title）を適切に書き換える。

＊Google colaboratoryを用いて、上記の解析・作図を行う方法を https://yyousuke.github.io/matplotlib/wpr_colab.html に載せた。

作成者：山下陽介（国立環境研究所）

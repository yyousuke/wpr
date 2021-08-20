# wpr

気象業務支援センター提供のCDに収録された気象庁のウインドプロファイラデータを読み込み、matplotlibで作図を行うためのpythonプログラム

## 1. read_wpr.py

ウインドプロファイラデータを読み込み、csvファイルを書き出す

**使用法**：

./read_wpr.py 

  -h, --help show this help message and exit

  --wpr_date <wpr_date> 

  --wpr_sta <wpr_sta>  

  --input_dir <input_dir> 

  --output_dir <output_dir> 

- **時刻**  --wpr_date 6桁の番号(yyyymmdd)

- **地点番号**（Station number）：--wpr_sta 5桁の番号

＊地点番号は、wpr_sta.csv参照

- **入力ディレクトリへのパス**： --input_dir 

- **出力ディレクトリへのパス**： --output_dir


## 2. map_wpr.py

matplotlibを使い作図する

地点番号（sta_id)をread_wpr.pyで書き出した地点に合わせ、作図時に表示される地点名（sta_name）やタイトル（title）を適切に書き換える。

＊Google colaboratoryを用いて、上記の解析・作図を行う方法を https://yyousuke.github.io/matplotlib/wpr_colab.html に載せた。

作成者：山下陽介（国立環境研究所）

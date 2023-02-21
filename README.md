# wpr

気象業務支援センター提供のCDに収録された気象庁のウインドプロファイラデータを読み込み、matplotlibで作図を行うためのpythonプログラム

## 0. 実行環境の準備

下記のパッケージを導入する

- Numpy

- Pandas

- matplotlib

## 1. read_wpr.py

ウインドプロファイラデータを読み込み、csvファイルを書き出す

- **使用法**：

    % ./read_wpr.py オプション

- **出力**：output_dir以下に出力される

    data_qua.地点番号.csv（品質管理情報、 quality flag）

    data_dir.地点番号.csv（風向、wind direction）

    data_spd.地点番号.csv（風速、wind speed）

    data_w.地点番号.csv（鉛直速度、vertical velocity）

    data_height.csv（データの高度一覧、height list of data）

    data_time.csv（時刻一覧、time list）

### オプション

- **-h |  --help**： ヘルプメッセージを表示し終了（show help message and exit）

- **--wpr_date** <wpr_date> ：日付を8桁の番号で（8-digit date; yyyymmdd）

    例：2019年5月4日のデータを変換する：--wpr_date 20190504

- **--wpr_sta** <wpr_sta> ：3桁の地点番号（3-digit station number）

    地点番号は、wpr_sta.csv参照

    例：熊谷：--wpr_sta 626

- **--input_dir** <input_dir> ：入力ディレクトリへのパス（path of input directory）

- **--output_dir** <output_dir> ：出力ディレクトリへのパス（path of output directory）

## 2. map_wpr.py

matplotlibを使い作図する

地点番号（sta_id)をread_wpr.pyで書き出した地点に合わせ、作図時に表示される地点名（sta_name）やタイトル（title）を適切に書き換える。

- **使用法**：

    % ./map_wpr.py

- **出力**：

    wpr.地点名.png

## 備考

Google colaboratoryを用いて、上記の解析・作図を行う方法を [https://yyousuke.github.io/matplotlib/wpr_colab.html](https://yyousuke.github.io/matplotlib/wpr_colab.html)に載せた。

作成者：山下陽介（国立環境研究所）

# SemanticSegmentation-demo
セマンティックセグメンテーションを実装するためのデモ

実行するうえでの推奨環境や必要なモジュールをいかにまとめます。

### 0, 環境
- os: windows10
- エディター: VSCode
- 言語: Python3.9.5
- アノテーションツール: labelme
- GPU: Geforce RTX 20系, or 30系
- Git

※ モデルのトレーニングをするうえでGPUは必ず必要です。
ノートPCではなくデスクトップPCで実装することを推奨します。

### 1, セットアップ

#### git clone

1. PowerShellまたはコマンドプロンプトでコードをクローンします

`
git clone https://github.com/TechC-SugarCane/SemanticSegmentation-demo
`

1. 以下のリンクをクリックしてデータセットをダウンロードします
    - [dataset.zip 630MiB](https://sugarcane.blob.core.windows.net/demo-dataset/dataset.zip "dataset.zip 630MiB")

1. ダウンロードしたデータセットを解凍してSemanticSegmentation-demoフォルダーの直下に保存します

#### モジュールのインストール
次のコマンドをコマンドを入力して必要なモジュールをすべてインストールします。

`
pip install requirements.txt
`

インストールされているか確認する

``` python
import cv2
import PIL
import torch
import matplotlib as plot
import segmentation_models_pytorch as smp
import albumentations
import glob
import tqdm

print(cv2.__version__)
print(PIL.__version__)
print(torch.__version__)
print(plot.__version__)
print(smp.__version__)
print(albumentations.__version__)
print(glob.__version__)
print(tqdm.__version__)
```

### 2 アノテーション

コマンドラインまたはパワーシェルに以下のコマンドを打つ
`
labelme
`

 - 左のバーにあるopendirをクリックし画像が保存されているフォルダーを選択する

 - Create polygonsを選択し、AIに覚えさせたい部分をポイントする

 - ポイントを終えると別の画面が出てくるのでタグを選択してOKのボタンを押す(タグがないときは新しく作る)

 - エクスプローラーが開くので保存したい場所を選択して保存する

 メモ: 最後のプロセスをオブジェクトごとにやるのはめんどくさいので、file->SaveAutomaticalyをクリックしておくと手間を少し省くことができます

 ### 3, 画像の前処理

 通常の画像とマスク画像の前処理が異なるので順番に記載していきます

 #### 通常画像の場合

- ImageProcess.ipynbの中にあるプログラムを上から実装します

#### マスク画像の場合

- powerShellまたはコマンドプロンプトで以下を実装します

`
python json_to_img.py "jsonデータが保存されているパス" -o="保存先のパス" -label_files="label.txtが保存されているパス"
`

※label.txtは自分で作成する必要があります

### 4, トレーニング

train_model.ipynbにあるプログラムを上から実装してきます

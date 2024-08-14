# ShunScanner
42 Network PicineのC言語の課題のレビューの手間を大幅に軽減するツール

## インストール

以下のコードを実行
```
bash <(curl -L https://raw.githubusercontent.com/himoto-42/ShunScanner/main/bin/install.sh)
```
または`install.sh`を[ダウンロード](https://raw.githubusercontent.com/himoto-42/ShunScanner/main/bin/install.sh)して実行

## アップデート

以下のコードを実行
```
bash <(curl -L https://raw.githubusercontent.com/himoto-42/ShunScanner/main/bin/update.sh)
```
または`update.sh`を[ダウンロード](https://raw.githubusercontent.com/himoto-42/ShunScanner/main/bin/update.sh)して実行


## 使い方

```
sscan

> +++++++++++++++++++++++++++++++++++++++++++++++++++++++
> ========== Profile List ==========
> latest Update : 2024-08-13-18:32
> [0] "C Piscine C00"
> [1] "C Piscine C01"
> +++++++++++++++++++++++++++++++++++++++++++++++++++++++
>
> Please select a profile number : 使用したいプロファイルの番号　例）1
> Please enter the target repository link : スキャン対象のリポジトリのリンク　例）git@vogsphere-v2.42tokyo.jp:vogsphere/intra-uuid-{}
```

## 出力の見方

### [ENTRY POINT] 
テストファイルの内容

### [OUTPUT] 
テストファイルの実行結果

## 目的
コンパイル操作などの時間を軽減して
アルゴリズムなどのコードレビューに時間をより多く使えるようにするために作られました。

このツールを使っただけでレビューを終了するなどの行為は絶対に行わないでください。

## 注意事項
- このツールはテストケースをすべて網羅しているわけではありません
- このツールを使用して発生したいかなる損害についても我々（開発者）は責任を負いません。

## プロファイルの作り方
```
{
    "Project": "プロジェクト名",
    "Author": "作成者の名前",
    "profiles": [
        {
            "name": "問題タイトル",
            "scan": {
                "directory": "提出するディレクトリ 例）ex00",
                "files": [
                    // 提出する必要があるファイル
                    "0.c",
                    "1.c"
                ],
                "entry": "base64 に変換されたテストコード",
                "exist_main": false // main.cが必要な課題かどうか,
                "excute_timeout": 5,
            }
        },
    ]
}
```

### テストコードの作り方
```
/** 別ファイルとして作成されるためテストコード内で使用する関数はincludeまたはプロトタイプ宣言が必要です **/
void	ft_putchar(char c);

int	main(void)
{
	ft_putchar('a');
	ft_putchar('\n');
	ft_putchar('$');
	ft_putchar('1');
}
```
以下のサイトでbase64に変換可能

https://www.base64encode.org/

# HR-ADUC-Datasimulator

HR-ADUC-Datasimulator は、Active Directory ユーザーとグループ属性のシミュレーションデータを生成するための Python スクリプトです。実際のユーザー情報ではなくシミュレーションデータを使用してデータ抽出プロセスのテストとデモンストレーションを容易にすることを目的としています。

## 前提条件

このスクリプトを正常に動作させるためには、次の前提条件が必要です：
1. スクリプトを実行するマシンにPythonがインストールされていること。このスクリプトの開発に使用されたバージョンは3.12.2です。3.6以降のバージョンを使用することを推奨します。
2. 次のモジュールがインストールされていること：
    a. pandas：
        このライブラリはデータ構造とデータ解析ツールを提供します。
    b. configparser：
        このモジュールはINI形式の設定ファイルで作業することを可能にします。
    c. Faker：
        このライブラリは、名前、住所、電話番号などの偽のデータを生成します。
    d. randomまたはrandom2：
        これらのモジュールはランダムな数値を生成するための関数を提供します。
    e. math：
        このモジュールは、三角関数、指数関数、対数関数などの標準的な数学関数のセットを提供します。
    f. unidecode：
        このモジュールはUnidecode文字列をASCIIに変換します。

configparser、random、およびmathモジュールは通常、Pythonに含まれています。
pandas、Faker、およびunidecodeモジュールは外部パッケージです。

## 特徴

- Active Directory (AD) アカウントの属性を抽出するためのランダムデータを生成します。
- 実際のユーザー情報を公開せずにデータ抽出プロセスをデモンストレーションするのに役立ちます。
- AD アカウントと人事 (HR) 抽出との間のデータ整合性をテストおよび検証できます。
- ADUC サーバーのセキュリティを向上させるための異常を強調し、変更を提案します。

## 使用法

1. リポジトリをローカルマシンにクローンするかダウンロードします。
2. あなたの言語に対応するparameters_[XX].iniファイルを複製し、parameters.iniという名前に変更してください。
3. parameters.ini ファイルをカスタマイズしてデータ生成プロセスの特定の設定を定義します。
4. HR-ADUC-Datasimulator.py スクリプトを実行してシミュレーションデータを生成します。
5. 出力を分析して、テスト、デモンストレーション、またはセキュリティの改善目的に使用します。

## ライセンス

HR-ADUC-Datasimulator は GNU Lesser General Public License v3.0 (LGPL-3.0) の下でライセンスされています。このスクリプトはライセンスの条件の下で使用、変更、配布できます。

詳細については、[LICENSE](https://github.com/ShaoLunix/HR-ADUC-Datasimulator/blob/main/LICENSE) ファイルを参照してください。

## 貢献

このプロジェクトへの貢献は歓迎されます。問題が発生した場合、改善の提案がある場合、新機能を提供したい場合は、GitHub で問題を開くかプルリクエストを送信してください。

## 免責事項

このスクリプトは、いかなる種類の保証もなしに提供されます。自己責任で使用してください。

## 著者

Stéphane-Hervé

## 連絡先

質問、フィードバック、またはサポートが必要な場合は、https://github.com/ShaoLunix/HR-ADUC-Datasimulator/issues に連絡してください。

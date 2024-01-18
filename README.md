# udemy-llm-apps

## 操作方法

起動

- poetry run streamlit run home.py

仮装環境が破損していたりしてstreamlitが起動できない場合はリセットする

- poetry install

- poetry add streamlit@1.25.0

SQLiteのインストール

- sudo apt update

- sudo apt install -y sqlite3

SQLiteにデータのインポート

- poetry run python init_sqlite.py

データベースに接続してデータの確認

- sqlite3 sample.db

~~~
.tables
select * from category limit 10;
~~~
# raw-download-from-cloud-storage

Google Cloud Storage でメタデータに `Content-Encoding:gzip` があるオブジェクトを展開しないで gzip のままダウンロードする。

`gsutil cp` コマンドや他言語のクライアント ライブラリでは展開してしまうが、Python のクライアント ライブラリではオプションを指定（raw_download=True）することで可能。

参考

- [gzip 圧縮ファイルのトランス コーディング](https://cloud.google.com/storage/docs/transcoding?hl=ja)
- [download_to_filename](https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob)

## Install

```bash
pip install -r requirements.txt
```

create .evn, and set GOOGLE_APPLICATION_CREDENTIALS

example)

```text
GOOGLE_APPLICATION_CREDENTIALS=key.json
```

## Run

```bash
python main.py {bucket_name} {prefix} {download_folder}
```

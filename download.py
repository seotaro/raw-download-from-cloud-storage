import sys
import os
from google.cloud import storage
from dotenv import load_dotenv
load_dotenv()


def download(bucket, src, folder):
    try:
        dest = os.path.join(folder, src)
        os.makedirs(os.path.dirname(dest), exist_ok=True)

        blob = bucket.blob(src)
        blob.download_to_filename(
            dest, raw_download=True)  # デフォルトのタイムアウトは60[sec]

        print(src, '->', dest)

    except Exception as e:
        print(src, '->', e)


def main(bucket_name, prefix, folder):
    client = storage.Client()

    blobs = client.list_blobs(bucket_name, prefix=prefix)
    bucket = client.bucket(bucket_name)
    for blob in blobs:
        download(bucket, blob.name, folder)


if __name__ == "__main__":
    bucket_name = sys.argv[1]
    prefix = sys.argv[2]
    folder = sys.argv[3]

    main(bucket_name, prefix, folder)

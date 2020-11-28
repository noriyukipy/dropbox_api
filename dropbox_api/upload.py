import dropbox
from pathlib import Path


def main(access_token, src, dst):
    """
    Args:
        src (str): the file/directory path in local
        dst (str): the file/directory path in remote
    """
    dbx = dropbox.Dropbox(access_token)

    src = Path(src)
    dst = Path(dst) / src.name

    print("Upload file")
    print(f"Src: {src}")
    print(f"Dst: {dst}")

    with open(src, "rb") as f:
        dbx.files_upload(f.read(), str(dst))


if __name__ == "__main__":
    import fire

    fire.Fire(main)

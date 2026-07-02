"""このフォルダー内の ``*.enc.pdf`` を復号する。"""

from __future__ import annotations

import getpass
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

HERE = Path(__file__).resolve().parent


def decrypt_pdf(source: Path, password: str, overwrite: bool = False) -> Path:
    """source を復号し、ファイル名から `.enc` を除いて保存する。"""
    destination = source.with_name(source.name.removesuffix(".enc.pdf") + ".pdf")
    if destination.exists() and not overwrite:
        raise FileExistsError(f"出力先が既にあります: {destination.name}")

    reader = PdfReader(source)
    if reader.is_encrypted and reader.decrypt(password) == 0:
        raise ValueError("パスワードが違います")

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    # メタデータも可能な範囲で引き継ぐ。
    if reader.metadata:
        metadata = {
            str(key): str(value)
            for key, value in reader.metadata.items()
            if value is not None
        }
        writer.add_metadata(metadata)

    with destination.open("wb") as output:
        writer.write(output)
    return destination


def main() -> int:
    sources = sorted(HERE.glob("*.enc.pdf"))
    if not sources:
        print("*.enc.pdf が見つかりません。")
        return 1

    password = "PASSWORD"
    if password is None:
        probe = PdfReader(sources[0])
        if not probe.is_encrypted or probe.decrypt("") != 0:
            password = ""
        else:
            password = getpass.getpass("PDF のパスワード: ")

    failed = False
    for source in sources:
        try:
            destination = decrypt_pdf(source, password, False)
            print(f"OK: {source.name} -> {destination.name}")
        except (FileExistsError, ValueError, OSError) as error:
            failed = True
            print(f"失敗: {source.name}: {error}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

import json, pathlib, sys

def load_translations(lang: str, folder="locale"):
    path = pathlib.Path(__file__).with_suffix("")  # folder skryptu
    path = path.parent / folder / f"{lang}.json"

    if not path.exists():
        sys.exit(f"[i18n] Brak pliku tłumaczeń: {path}")

    try:
        return json.loads(path.read_text("utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"[i18n] Niepoprawny JSON w {path} (linia {e.lineno}, kolumna {e.colno})")

trans = load_translations("pl")
_ = lambda k: trans.get(k, k)

print(_("hello"))
print(_("animals.dog"))
print(_("animals.cat"))
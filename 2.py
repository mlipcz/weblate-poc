import json, pathlib

def load_translations(lang: str, folder="locale"):
    path = pathlib.Path(folder, f"{lang}.json")
    return json.loads(path.read_text("utf-8"))

trans = load_translations("pl")

def _(msgid: str) -> str:
    return trans.get(msgid, msgid)   # fallback do oryginału

print(_("hello"))

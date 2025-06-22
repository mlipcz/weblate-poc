import i18n
from pathlib import Path

BASE_DIR = Path(__file__).parent
i18n.load_path.append(str(BASE_DIR / "locale"))
i18n.set("locale", "pl")        # albo np. powłoka/zmienna środowiskowa

print(i18n.t("hello"))          # ➜ Witaj, świecie!
print(i18n.t("exit"))           # ➜ Zakończ
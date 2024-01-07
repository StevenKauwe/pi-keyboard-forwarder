from evdev import ecodes

from src.hid import keycodes

with open("keycodes.txt", "w") as f:
    f.write("")
with open("ecodes.txt", "w") as f:
    f.write("")

i = 0
for name, value in keycodes.__dict__.items():
    if name.startswith("_") or name.startswith("dataclasses"):
        continue
    with open("keycodes.txt", "a") as f:
        i += 1
        f.write(f"{name}\n")

for name, value in ecodes.__dict__.items():
    if name.startswith("_") or name.startswith("ecodes"):
        continue
    with open("ecodes.txt", "a") as f:
        f.write(f"{name}\n")

import json

from ecodes_to_hid import _MAPPING
from openai import OpenAI

client = OpenAI()


with open("ecodes.txt", "r") as f:
    ecodes = f.read().splitlines()
    key_ecodes = "\n".join([x for x in ecodes if x.startswith("KEY_")])
with open("keycodes.txt", "r") as f:
    keycodes = f.read().splitlines()


def get_hid_chunk_from_openai(next_hid_chunk):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        # model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": key_ecodes
                + "\n\nCreate the mapping from ecodes to the HID names provided. Only return the json mapping, e.g.\n\n```json\n{\necodes.KEY_1: hid.KEYCODE_NUMBER_1,\n}\n```",
            },
            {"role": "user", "content": next_hid_chunk},
        ],
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    raw_text = response.choices[0].message.content
    json_text = raw_text.split("```json\n")[1].split("\n```")[0]
    return json.loads(json_text)


ecodes_to_hid = _MAPPING

# remove the example mappings
for k, v in ecodes_to_hid.items():
    if v in keycodes:
        keycodes.pop(keycodes.index(v))

n_mappings_per_request = 20
for i in range(0, len(keycodes), n_mappings_per_request):
    next_hid_chunk = "\n".join(keycodes[i : i + n_mappings_per_request])
    hid_chunk = get_hid_chunk_from_openai(next_hid_chunk)
    ecodes_to_hid.update(hid_chunk)


with open("ecodes_to_hid.py", "w") as f:
    f.write("_MAPPING = " + json.dumps(ecodes_to_hid))
    f.write("\n")

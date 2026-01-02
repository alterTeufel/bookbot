def get_num_words(text: str) -> str:
    return len(text.split())

def get_char_count(text: str) -> dict:
    counts = {}
    for ch in text.lower():
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_on_num(item):
    return item["num"]

def get_char_count_to_list_sorted(counts: dict) -> list:
    out = []
    for ch, n in counts.items():
        out.append({"char": ch, "num": n})
    out.sort(reverse=True, key=sort_on_num)
    return out

# main.py
print("スタート!")

import re

def remove_mentions(text):
    """
    テキスト内の@で始まるメンションを削除し、前後の空白をトリムする関数。
    """
    return re.sub(r'@\S+\s*', '', text).strip()

# テスト
text = "@bot テスト"
print(text)
clean_text = remove_mentions(text)
print(clean_text)  # "テスト"
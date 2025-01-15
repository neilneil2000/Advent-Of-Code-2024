def word_check(words, check_word="APPLE"):
    words = list(map(lambda x: "".join(x), words))
    return sum(map(lambda x: x.count(check_word) + x[::-1].count(check_word), words))


def checker(words, check_word="APPLE"):
    l = len(words) - 1
    words_a = list(
        zip(*["." * (l - i) + word + "X" * i for i, word in enumerate(words)])
    )
    words_b = list(
        zip(*["." * i + word + "X" * (l - i) for i, word in enumerate(words)])
    )

    words_c = list(zip(*words))

    return (
        word_check(words, check_word)
        + word_check(words_a, check_word)
        + word_check(words_b, check_word)
        + word_check(words_c, check_word)
    )


words_list = [
    ["AXXXX", "XPXXX", "XXPXX", "XXXLX", "XXXXE"],
    ["EXXXX", "XLXXX", "XXPXX", "XXXPX", "XXXXA"],
    ["XXXXA", "XXXPX", "XXPXX", "XLXXX", "EXXXX"],
    ["XXXXE", "XXXLX", "XXPXX", "XPXXX", "AXXXX"],
    ["APPLE", "XXXXX", "XXXXX", "XXXXX", "XXXXX"],
    ["ELPPA", "XXXXX", "XXXXX", "XXXXX", "XXXXX"],
    ["AXXXX", "PXXXX", "PXXXX", "LXXXX", "EXXXX"],
    ["EXXXX", "LXXXX", "PXXXX", "PXXXX", "AXXXX"],
]

for words in words_list:
    print(checker(words))

words = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
ans = checker(words.splitlines(), "XMAS")
print(ans)

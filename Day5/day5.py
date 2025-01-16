from day5_input import rules_list, page_list


def order_ok(rules: list, pages: list) -> int:
    """Return Middle page number if page order meets requirements of rules, else returns 0"""
    for i, first in enumerate(pages):
        for second in pages[i:]:
            if second + "|" + first in rules:
                return 0
    return int(pages[len(pages) // 2])


def main():

    ans = sum(order_ok(rules_list, pages.split(",")) for pages in page_list)
    print(f"Day 5 Part 1: {ans}")


if __name__ == "__main__":
    main()

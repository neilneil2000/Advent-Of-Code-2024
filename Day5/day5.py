from day5_input import rules_list, page_list


def order_ok(rules: list, pages: list) -> int:
    """Return Middle page number if page order meets requirements of rules, else returns 0"""
    for i, first in enumerate(pages):
        for second in pages[i:]:
            if second + "|" + first in rules:
                return 0
    return int(pages[len(pages) // 2])


def compile_rules(rules: list[str]) -> dict:
    """Return dictionary of rules"""
    rules_dict = {}
    for rule in rules:
        a, b = rule.split("|")
        rules_dict[a] = {b}.union(rules_dict.get(a, set()))
    return rules_dict


def get_first_page(rules, pages) -> str:
    """Figure out first page in this list of pages"""
    if len(pages) == 1:
        return pages[0]
    for i, page in enumerate(pages):
        if page not in rules:
            continue
        if set(pages[i + 1 :]).issubset(rules[page]):
            # print(f"{page} is first page in {pages}")
            return page
    raise ValueError


def get_correct_order(rules: dict[str, set], pages: list) -> list:
    correct_order = []
    while pages:
        next_page = get_first_page(rules, pages)
        pages.remove(next_page)
        correct_order.append(next_page)
    return correct_order


def main():
    ans = sum(order_ok(rules_list, pages.split(",")) for pages in page_list)
    print(f"Day 5 Part 1: {ans}")

    rules = compile_rules(rules_list)
    total = 0
    for pages in page_list:
        correct_order = get_correct_order(rules, pages.split(","))
        pages = pages.split(",")
        if pages == correct_order:
            continue
        total += int(correct_order[len(correct_order) // 2])
    print(f"Day 5 Part 2: {total}")


if __name__ == "__main__":
    main()

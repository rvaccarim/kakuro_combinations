import itertools
import collections
from functools import reduce
from typing import List

KakuroData = collections.namedtuple('KakuroData', 'sum length factors')
combinations: List['KakuroData'] = []
Style = collections.namedtuple('Style', 'text background')


def find_combinations():
    # we get all the possible combinations that have 2 to 9 factors
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for length in range(2, 10):
        for combination in itertools.combinations(numbers, length):
            total_sum = sum(combination)
            factors_str = "".join(map(str, combination))

            data = KakuroData(sum=total_sum, length=length, factors=factors_str)
            combinations.append(data)

    combinations.sort()


# alternative implementation
# def find_combinations2():
#     # we get all the possible combinations that have 2 to 9 factors
#     for length in range(2, 10):
#         for combination in itertools.combinations('123456789', length):
#             # reduce iterates through a collection and shortens it by applying a function to the two first elements,
#             # then applies the same function to the result and the next element
#             total_sum = reduce(lambda x, y: int(x) + int(y), combination)
#             factors_str = "".join(combination)
#
#             data = KakuroData(sum=total_sum, length=length, factors=factors_str)
#             combinations.append(data)
#
#     combinations.sort()


def create_html(mode):
    black = "#000000"
    grey = "#999999"

    # 1 = color
    # 2 = monochrome
    with open('factors.html', 'w') as f:
        if mode == 1:
            # text color, background
            colors = [Style("", ""),
                      Style("", ""),
                      Style("000000", "#D0A9F5"),
                      Style("000000", "#A9A9F5"),
                      Style("000000", "#A9D0F5"),
                      Style("000000", "#A9F5D0"),
                      Style("000000", "#D0A9F5"),
                      Style("000000", "#99FFFF"),
                      Style("000000", "#F2F5A9"),
                      Style("000000", "#F5A9A9")]
        else:
            colors = [Style("", ""),
                      Style("", ""),
                      Style("#FFFFFF", "#000000"),
                      Style("#000000", "#FFFFFF"),
                      Style("#FFFFFF", "#000000"),
                      Style("#000000", "#FFFFFF"),
                      Style("#FFFFFF", "#000000"),
                      Style("#000000", "#FFFFFF"),
                      Style("#FFFFFF", "#000000"),
                      Style("#000000", "#FFFFFF")]

        f.write(open_html())
        f.write(head())
        f.write("<body>\n")
        f.write("<b>")
        f.write("<font size='3'>Kakuro factors</font>")
        f.write("</b>\n")

        f.write("<table>\n<tr>\n")
        for length in range(2, 10):
            f.write(table_row(f"{length}-factor   ", colors[length].text, colors[length].background))
        f.write("</tr>\n")
        f.write("</table>\n")

        f.write("<table border='1'>\n")

        previous = combinations[0][0]
        new_row = True

        for combination in combinations:
            if previous != combination.sum:
                f.write(table_row(previous, black, grey))
                f.write("</tr>\n")
                new_row = True

            if new_row:
                f.write("<tr>\n")
                f.write(table_row(combination.sum, black, grey))
                new_row = False

            i = combination.length
            f.write(table_row(combination.factors, colors[i].text, colors[i].background))

            previous = combination.sum

        f.write(table_row(previous, black, grey))
        f.write("</tr><P>\n")
        f.write("</table>\n")
        f.write("</body>\n")
        f.write("</html>\n")


def open_html():
    return "<!DOCTYPE html>\n<html>\n"


def head():
    return "<head>\n<title>\nKakuro factors\n</title>\n</head>\n"


def table_row(text, text_color, bg_color):
    return f"<td align='center' bgcolor='{bg_color}'><font size='2' face='Arial' color='{text_color}'>{text}</font></td>\n"


def main():
    find_combinations()
    create_html(mode=1)
    print("Done!")


if __name__ == "__main__":
    main()

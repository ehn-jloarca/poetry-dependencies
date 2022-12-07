from poetry_versioning.main import find_random_timezone, get_time
from quoters import Quote


def print_tz():
    tz = find_random_timezone()
    print(get_time(tz))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_tz()
    print(Quote.print_programming_quote())

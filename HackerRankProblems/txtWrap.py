import textwrap

def wrap(string, max_width):
    wraper = textwrap.TextWrapper(width=max_width)
    word_list = wraper.wrap(text=string)
    list_items=""
    for items in word_list:
        list_items = f"{list_items+items}\n"
    return list_items

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
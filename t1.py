from Utils.generate import generator
from Utils.context import Session


def adv_print(*args, start='', sep='\n', max_line=5, in_file=False):

    if not args:
        return start
    for content in args:
        if len(start + content) > max_line:
            result = (start + content)[:max_line] + '\n'
            print_line = start + content
            while len(print_line) >= max_line:
                print_line = print_line[max_line:]
                result += print_line[:max_line] + '\n'
            print(result + sep)
            if in_file:
                with open('file.txt', 'a', encoding='utf-8') as f:
                    f.write(result)
        else:
            result = start + content + sep
            print(result)
            if in_file:
                with open('file.txt', 'a', encoding='utf-8') as f:
                    f.write(result)
    for item in generator('C:\\Users\\Александр\\PycharmProjects\\HW_2.4.2\\file.txt'):
        print(item)

if __name__ == '__main__':
    with Session():
        adv_print('ааааааа', 'ббб', 'вввввввввввв', sep='\n', max_line=7, in_file=True)
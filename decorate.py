#!/usr/bin/env python
# coding: utf8

from sys import argv

def read_file(filepath):
    summary = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if (len(line) in range(4,6)) and line[-2:].isdigit():
                continue
            else:
                summary.append(line)
        f.close()

    return summary

def format_input(summary):
    for index, line in enumerate(summary):
        if (len(line)) in range(7,9) and line[-2:] in ('AM', 'PM'):
            summary[index-1] = '\n{0} [{1}]'.format(summary[index-1], line)
            del summary[index]

    return summary

def assemble_output(summary):
    with open('output.txt', 'w+', encoding='utf-8') as f:
        f.write("\n".join(summary))
        f.close()

    print('Decoration complete!\n')


def main():
    try:
        print('Reading..\n')
        summary = read_file(argv[1])
        print('Formatting..\n')
        formatted = format_input(summary)
        print('Decorating..\n')
        assemble_output(formatted)
        print('Result: Output.txt')
    except IndexError:
        print('Invalid filepath')
    except FileNotFoundError:
        print('File not found')
    pass


if __name__ == '__main__':
    main()
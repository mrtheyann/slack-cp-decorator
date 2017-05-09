def reading():
    summary = []

    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if (len(line) in range(4,6)) and line[-2:].isdigit():
                continue
            else:
                summary.append(line)
        f.close()

    return summary

def formatting(summary):
    for index, line in enumerate(summary):
        if (len(line)) in range(7,9) and line[-2:] in ('AM', 'PM'):
            summary[index-1] = '\n{0} [{1}]'.format(summary[index-1], line)
            del summary[index]
    return summary

def assembling(summary):
    with open('output.txt', 'w+', encoding='utf-8') as f:
        f.write("\n".join(summary))
        f.close()
    print('Decoration complete!\n')


def main():
    print('Reading..\n')
    summary = reading()
    print('Formatting..\n')
    formatted = formatting(summary)
    print('Decorating..\n')
    assembling(formatted)
    print('Result: Output.txt')
    pass


if __name__ == '__main__':
  main()
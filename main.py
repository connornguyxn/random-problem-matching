from requests import get
from tabulate import tabulate

# read items and candidates from file with utf-8 encoding
with open('items.txt', 'r', encoding='utf-8') as f:
    items = f.read().splitlines()
with open('candidates.txt', 'r', encoding='utf-8') as f:
    candidates = f.read().splitlines()


def get_sequence(min, max):
    url = f'https://www.random.org/sequences/?min={min}&max={max}&col=1&format=plain&rnd=new'
    response = get(url)
    # format response to int list
    return [int(i) for i in response.text.split()]


# multiply each item of b to match items
b = candidates * (len(items) // len(candidates))
# shuffle b using random.org interger sequence generator
order = get_sequence(0, len(b) - 1)
b = [b[i] for i in order]


print(f'Remaining items: {len(items) - len(b)}')
if input('Match remaining items? (y/n) ') == 'y':
    order = get_sequence(0, len(candidates))
    # match remaining items to candidates
    b += [candidates[i] for i in order[:len(items) - len(b)]]


# match items and b and write to file
with open('match.txt', 'w', encoding='utf-8') as f:
    f.write(tabulate(zip(items, b), tablefmt='plain'))
print('Results written to match.txt')
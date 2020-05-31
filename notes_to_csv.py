"""Utility for converting my note taking style to csv for anki"""
import os


def reformat(all_text):

    # separate cards by the delimeter
    cards = all_text.split('---')

    # shave off the first and last cards as they are headers or empty
    # also clean up newlines
    cards = [card.strip() for card in cards[1:-1]]


    # split fields
    cards = [card.split('\n\n') for card in cards]

    # handle instances in which I elaborate on the back of the card
    for index, card in enumerate(cards):
        if len(card) > 2:
            cards[index] = [card[0], '<br><br>'.join(card[1:])]

    # join stuff
    cleaned_up = []

    for card in cards:
        clean_card = [field.strip() for field in card]
        clean_card = '\t'.join(clean_card)
        cleaned_up.append(clean_card)

    cards = cleaned_up

    cards = '\n'.join(cards)

    return cards

def main():

    print('This script takes a text file and reformats for import into Anki')
    filepath = 'UNSET'

    while not os.path.exists(filepath):
        filepath = input('Text file: ').strip()

    base = os.path.splitext(filepath)[0]

    with open(filepath, 'r') as infile:
        text = infile.read()

    reformatted_notes = reformat(text)

    cards_qty = len(reformatted_notes.split('\n'))
    print(f'Writing out {cards_qty} cards...')

    outpath = base + '_reformatted.txt'

    with open(outpath, 'w') as outfile:
        outfile.write(reformatted_notes)

    input('Success!')

if __name__ == '__main__':
    main()

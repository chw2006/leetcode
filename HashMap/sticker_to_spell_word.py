# This is variant of Stickers to Spell Word, except we are only given one sticker. 
# Return the number of stickers needed to spell word. Each letter in the sticker can be used only once.

from collections import Counter
from math import ceil

def stickerToSpellWord(sticker, word):
    # Count the # of occurences of each letter in both sticker and word
    # Iterate through the word count. 
    # Make sure the letter in the word is also in the sticker. If not, we can return -1. 
    # If the letter is in the sticker count, we need to determine how many stickers we need.
    # So we need to divide the count in word by the count in sticker. We also need to round up, so use ceil. 
    # We want the max of the count, since that is what is neccessary to spell the word.
    sticker_count = Counter(sticker)
    word_count = Counter(word)
    num_stickers = 0
    for k in word_count.keys():
        if k not in sticker_count:
            return -1
        else:
            # If k is in sticker count, the number of stickers we need is occurences in word / occurences in sticker
            stickers_needed = ceil(word_count[k] / sticker_count[k])
            num_stickers = max(num_stickers, stickers_needed)
    return num_stickers

print(stickerToSpellWord("banana", "anna")) # 1
print(stickerToSpellWord("banana", "mango")) # -1
print(stickerToSpellWord("aaaaaab", "aaaaaaaaaaaa")) # 2

# T: O(N), where N is the # of unique characters in word.
# S: O(N), we keep 2 maps

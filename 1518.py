'''
Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a variable-length binary string, such as 0101 or 111110, where shorter lengths correspond to more common letters.
To accomplish this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing the path, descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between characters and their encoded binary strings.
'''
 
def build_tree(freq: dict):
    # convert frequency dict to list of most frequent chars. could also use heap or counter
    chars = [(val, key) for key, val in freq.items()]
    chars.sort(reverse=True)
    chars = [key for val, key in chars]
    
    mapping = {}
    r_code = '0'
    l_code = '1'

    # keep prepending lefts before a final right for left branch, and vice versa for right branch to create a valid code
    for i, char in enumerate(chars):
        if i % 2:
            r_code = '1' + r_code
            mapping[char] = r_code
        else:
            l_code = '0' + l_code
            mapping[char] = l_code

    return mapping


f = {
    'c': 4,
    'a': 3,
    't': 2,
    's': 1,
}
print(build_tree(f))
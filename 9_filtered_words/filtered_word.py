import sys,locale
filtered_words = r'words.txt'
filtered_words_dict = {}

with open(filtered_words) as f:
    for line in f:
        word = line.strip()
        if not filtered_words_dict.has_key(word):
            filtered_words_dict[word] = True

# while True:
#     if filtered_words_dict.has_key(raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True)).encode('utf-8')):
#         print"yes"
#     else:
#         print"no"

while True:
    s = raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True)).encode('utf-8')
    for key in filtered_words_dict.keys():
        while s.find(key) != -1:
            start = s.find(key)
            if start != -1:
                s = s[:start] + '*' + s[start + len(key):]
    print s
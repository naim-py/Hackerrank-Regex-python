import re
for _ in range(int(input())):
    pattern = r'^[\.._][0-9]+[a-zA-Z]*_?$'
    # + mane akadhik sonkha bste pare
    # * mane akadhik letter bste pare
    # ? mane sese _ or letter jekono kichu bste pare
    match = bool(re.search(pattern,input()))
    if match:
        print('VALID')
    else:
        print('INVALID')
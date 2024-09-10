'''
extract the 18 charact before and 18 character after the word
we are locating for.
'''

## Data
letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''
## One-Liner
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1


## for loop equivalent
def query(stext, sq):
    if sq in stext:
        start_loc =stext.find(sq)-18
        stop_loc =stext.find(sq)+18
        found = stext[start_loc:stop_loc]
        return found

    else:
        return -1


## Result
print(find(letters_amazon, 'SQL'))
print(query(letters_amazon, 'SQL'))
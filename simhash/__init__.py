#! /usr/bin/env python

from table import PyCorpus as Corpus
from table import PyTable  as Table
from table import PyHash   as hash
from table import PyHashFp as hash_fp
from table import PyHashToken as hash_token
from table import PyHashHasher as hash_hasher

def _string_hash(v):
    hashbits = 64
    if v == "":
        return 0
    else:
        x = ord(v[0])<<7
        m = 1000003
        mask = 2**hashbits-1
        for c in v:
            x = ((x*m)^ord(c)) & mask
        x ^= len(v)
        if x == -1:
            x = -2
        return x

def hash_tokenpy(tokens):
    hashers = [_string_hash(v) for v in tokens]
    return hash_hasher(hashers)


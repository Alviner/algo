# -*- coding: utf-8 -*-
import json
import hashlib
import time


class Block:
    def __init__(self, idn: int, hash_prev, nonce):
        self.id = idn
        self.time = time.time()
        self.hash_prev = hash_prev
        self.hash = None
        self.nonce = nonce

    def set_hash(self, hash_value):
        self.hash = hash_value

    def __repr__(self):
        return f'Block({self.id}, {self.hash}, {self.nonce})'


class Blockchain:
    def __init__(self, zeroes=3):
        self.chain = []
        self.zeroes = zeroes
        self.add_block('00000', 0)

    def hash(self, block: Block):
        block_string = json.dumps(
            {'id': block.id,
             'time': block.time,
             'nonce': block.nonce,
             'hash_prev': block.hash_prev},
            sort_keys=True).encode()
        return hashlib.md5(block_string).hexdigest()

    def add_block(self, hash_prev, nonce):
        block = Block(idn=len(self.chain) + 1,
                      hash_prev=hash_prev,
                      nonce=nonce)
        block.set_hash(self.hash(block))
        self.chain.append(block)
        return block

    def proof_of_work(self):
        last_block = self.chain[-1]
        last_hash = self.hash(last_block)
        nonce = 0
        while self.valid_proof(last_hash, nonce) is False:
            nonce += 1
        return nonce

    def valid_proof(self, last_hash, nonce):
        guess = f'{last_hash}{nonce}'.encode()
        guess_hash = hashlib.md5(guess).hexdigest()
        return guess_hash[-self.zeroes:] == '0' * self.zeroes

    def is_valid(self):
        last_block = self.chain[0]
        current_index = 1

        while current_index < len(self.chain):
            block = self.chain[current_index]
            if block.hash_prev != self.hash(last_block):
                return False

            if not self.valid_proof(block.hash_prev, block.nonce):
                return False
            last_block = block
            current_index += 1
        return True


def test_bch():
    blockchain = Blockchain(zeroes=2)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()
    blockchain.add_block(nonce=nonce, hash_prev=last_block.hash)

    assert blockchain.is_valid()


if __name__ == '__main__':
    test_bch()

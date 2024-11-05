import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request


class Blockchain :

  def __init__(self):
      self.current_transactions = []
      self.chain = []
      self.nodes = set()

# Create the genesis block
self.new_block(previous_hash = '1', proof = 100)

def register_node(self, address):
  """
  Add a new node to the list of nodes

  :param address: Address of node. Eg. 'http://192.168.0.5:5000'
  """

  parsed_url = urlparse(address)
  if parsed_url.netloc:
     self.nodes.add(parsed_url.netloc)
  elif parsed_url.path
  # Accepts an URL without scheme like '192.168.0.5:5000'.
     self.nodes.add(parsed_url.path)
  else
     raise ValueError('Invalid URL')


 def valid_chain(self, chain):
   """
   Determine ifa given blockchain is valid

   :param chain: A blockchain
   :return: True if valid, False if not
   """

   last_block = chain[0]

   current_index = 1

   while current_index < len(chain):
      block = chain[current_index]
      print(f'{last_block'})
      print(f'{block'})
      print("\n--------\n")
      # check that the hash of the block is correct

      last_block_hash = self.hash(last_block)
      if block['previous_hash'] != last_block_hash;
      return False

     #check that the proof of work is correct
     if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
     return False

     last_block = block
     current_index += 1

     return True

     def resolve_conflicts(self):
     """
     This is our consensus algorithm, it resolves conflicts
     by replacing our chain with the the longest one in the network.

     :return: True if our chain was replaced, False if not
     """

     neighbours = self.nodes
     new_chain = None

    # We're only looking for chains longer than ours

    max_length = len(self.chain)

    # Grab and verify the chains from all the nodes in our network
    for node in neighbours:
        response = requests.get(f'http://{node}/chain')

        if response.status_code == 200:
            length = response.json()['length]
            chain = response.json()['chain']

            # check if the length is longer and the chain is valid

            if length > max_length and self.valid_chain(chain):

              max_length = length
              new_chain = chain

           # Replace our chain if we discovered a new, valid  chain longer than ours
           if new_chain:
               self.chain = new_chain
               return True

           return False

       def new_block(self, proof, previous_hash):
       """
       Create a new Block in the Blockchain

       :param proof: The proof given by the proof of Work algorithm
       :param previous_hash: Hash of previous Block
       :return: New Block
       """

       block = {
           'index': len(self.chain) + 1,
           'timestamp': time(),
           'transactions': self.current_transactions,
           'proof': proof,
           'previous_hash': previous_hash or self.hash(self.chain[-1]),
                }

          # Reset the current list of transactions
              self.current_transactions = []
               self.chain.append(block)
               return block


          def new_transaction(self, sender, recipient, amount):
              """
              Creates a new transaction to go into a next mined block
              :param Sender: Address of the sender
              :param recipient: Address of the recipient
              :param Amount: Amount
              :return: The index of the block that will hold this transaction
              """
              self.current_transactions.append({
                  'sender' : sender,
                  'recipient' : recipient,
                  'amount' : amount,
                    })

                return  self.last_block['index'] + 1

         @property
         def last_block(self):
             return self.chain[-1]

         @staticmethod
         def hash(block):
             """
             Creates a SHA-256 hash of a Block

             :param block: Block
             """

             # We must make sure that the Dictionary is Ordered, or we will have inconsistent hashes
             block_string = json.dumps(block, sort_keys = True).encode()
             return hashlib.sha256(block_string).hexdigest()

       def proof_of_work(self, last_block):
           """
           Simple Proof of Work Algorithm:

            - Find a number p' such that hash(pp') contains leading 4 zeros
            - where p is the previous proof,   and p' is the new proof

            :param last_block: <dict> last Block
            :return: <int>
            """

            last_proof = last_block['proof']
            last_hash = self.hash(last_block)

            proof = 0
            while self.valid_proof(last_proof, proof, last_hash) is False:
              proof += 1

            return  proof

          @staticmethod
          def valid_proof(last_proof, proof, last_hash):
              """
              validates the proof

              :param last_proof: <int> Previous Proof
              :param proof: <int> Current Proof
              :param last_hash: <str> The hash of the Previous Block
              :return: <bool> True if Correct, False if not.

              """
              guess = f'{last_proof}{proof}{last_hash}'.encode()
              guess_hash = hashlib.sha256(guess).hexdigest()
              return guess_hash[:4] = "0000"


       # Instantiate the node
       app = Flask(__name__)

       # Generate a globally unique address for this node
       node_identifier = str(uuid4()).replace('-','')

       # Instantiate the Blockchain
       blockchain = Blockchain()

       @app.route('/mine', method=['GET'])
       def mine():
           # We run the proof of work algorithm to get the next proof...
           last_block = blockchain.last_block
           proof = blockchain.proof_of_work(last_block)

           # We must receive a reward for finding the proof.
           # The sender is "0" to signify that this node has mined a new coin.
           blockchain.new_transaction(
               sender="0",
               recipient = node_identifier,
               amount =1,
               )
       # Forge the new block by adding it to the chain
       previous_hash = blockchain.hash(last_block)
       block = blockchain.new_block(proof, previous_hash)

       response = {
           'message' : "New Block forged",
           'index' : block['index'],
           'transactions' : block['transactions'],
           'proof' : block['proof'],
           'previous_hash' : block['previous  hash']
                }
             return jsonify(response), 200   

        @app.route('/transactions/new', methods=['POST'])

        def new_transaction():
            values = request.get_json()

            # check that the required fields are in the POST'ed data
            required = ['sender', 'recipient', 'amount']
            if not all(k in values for k in required):
                return 'Missing values', 400

            # Create a new Transaction 
            index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

            response = {'message': f'Transaction will be added to Block {index}'}
            return jsonify(response), 201

        @app.route('/chain', method=['GET'])
        def full_chain():
            response = {
            'chain' : blockchain.chain,
            'length' : len(blockchain.chain),
            }
            return jsonify(response), 200

            @app.route('nodes/register' , method=['POST'])

            def register_nodes():
                values = request.get_json()

                nodes = values.get_nodes('nodes')
                if nodes is None:
                     return "Error: Please supply a valid list of nodes", 400

                for node in nodes
                    blockchain.register_node(node)

                
       
               

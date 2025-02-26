const crypto = require("crypto");

class Blockchain {
  constructor() {
    this. chain = [];
    this.pendingtransactions = [];
    this.newBlock();
    this.peers = new Set();
  }

  /**
  * adds a node to our peer table
  */

  addPeer(host) {
    this.peers.add(host);
  }

  /**
  * adds a node to our peer table
  */
  getPeers() {
       return Array.from(this.peers);
  }
  /**
  * creates a new block containing any
  outstanding transaction
  */
  newBlock(previousHash, nonce = NULL) {
    let block = {
      
  index: this.chain.length, 

    
timestamp: new Date().toISOString(),
      
  transactions: this.pendingtransactions,
      previousHash,
      nonce
    };
    block.hash = Blockchain.hash(block);

    console.log('Created block ${block.index}');

    // Add the new block to the blockchain

    this.chain.push(block);

    // Reset pending transactions
    this.pendingTransactions = [];
  }
  /**
  * generates a SHA-256 hash of the block
  */
static hash(block) {
  const blockString = JSON.stringify(block,Object.keys(block).sort());
  return crypto.createHash("sha256").update(blockString).digest("hex");
}

/**
* returns the last block in the chain
  
*/
  lastBlock()
  {
    return this.chain.length && this.chain[this.chain.length-1];
  } 

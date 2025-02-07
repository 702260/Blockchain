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

    
    
    
      
    
  

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
  /**
  * Returns the last block in the chain
  **/
  lastBlock() {
    return this.chain.length && this.chain[this.chain.length - 1];
  }
  /* Determines if a hash begins with a "difficulty" number of 0s
  *
  * @param hashofBlock: the hash of the block (hex string)
  * @param difficulty: an integer defining the difficulty
  */
  static powIsAcceptable(hashofBlock, difficulty) {
    return hasofBlock.slice(0,difficulty) ==="0".repeat(difficulty);
  }
  /**
  * Genarates a random 32 byte string
 */
  static nonce() {
  return crypto.createHash("sha256").update(crypto.randomBytes(32)).digest("hex");
  }

  /**
  * Proof of Work mining algorithm
  *
  * We hash the block with random string until the hash begins with
  * a difficulty number of 0s.
  */ 
  mine(blocktoMine = null, difficulty = 4){
    const block = blockToMine || this.lastBlock();

    while(true) {
     block.nonce = Blockchain.nonce();
     if(Blockchain.powIsAcceptable(blockChain.hash(block), difficulty)) {
       console.log("We mined a block!")
       console.log(` - Block hash: ${Blockchain.hash(block)}`;
       console.log(`   - nonce:        ${block.nonce}`);
       return block;
     }
    }
  }
}
module.exports = Blockchain;
    

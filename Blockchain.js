const crypto = require("crypto");

class Blockchain 
  {
   constructor() {
     this.chain = [];
     this.pendingtransaction = [];
     this.newBlock();
     this.peers = new Set();
   }

    /**
    * Adds a node to our peer
    */
    addPeer(host) {
      this.peers.add(host);
    }

    /**
   * Adds a node to our peer table
   */
    getPeers() {
      return Array.from(this.peers);
    }
    /**
    * creates a new block containing any
    outstanding transaction
    */
    newBlock(previousHash, nonce = null) {
      let block = {


  
    
    
     
     
     
     
     
     
    
    


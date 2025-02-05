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
  

    
    
    
      
    
  

const crypto = require("crypto");

class Blockchain {
  constructor() {
    this. chain = [];
    this.pendingtransactions = [];
    this.newBlock();
    this.peers = new Set();
  }
  

    
    
    
      
    
  

using System;
using System.Collections.generic;

namespace BlockChainDemo
{
  public class Block
  {
    public int Index {get; set;}
    public Datetime Timestamp {get; set;}
    public List<transaction> Transactions {get;  set;}
    public int Proof {get; set;}
    public string PreviousHash {get; set;}

    public override string ToString()
    {
      return $"{Index} [{Timestamp.Tostring("yyyy-MM-dd HH:mm:ss)}] Proof: {Proof} | PrevHash: {PreviousHash} | Trx: {Transactions.Count}";
    }
  }
}

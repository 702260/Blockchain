using System;
using System.Collections.generic;

namespace BlockChainDemo
{
  public class Block
  {
    public int Index {get; set;}
    public Datetime Timestamp {get; set;}
    public List<transaction> Transactions {get;  set;}

using Newtonsoft.json
using System.Configuration
using System.IO
using System.Net
using System.Net.Http

namespace BlockChainDemo
{
  public class WebServer
  {
    public WebServer(BlockChain chain)
    {
      var settings = ConfigurationManager.Appsettings;
      
  


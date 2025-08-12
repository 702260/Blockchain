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
      string host = settings["host"]?.Length > 1 settings["host"] : "localhost";
      string port = settings["port"]?.Length > 1 settings["port"] : "12345";

      var server = new TinyWebServer.WebServer(request =>
                   {
       string path = request.Url.PathAndQuery.ToLower();
       string query = "";
        string json = "";
        if(path.Contains("?"))
        {
          string[] parts = path.Split('?');
          path = parts[0];
          query = parts[1];
        }
        switch (path)
        {
            //GET: http://localhost:12345/mine
          case "/mine":
            return chain.Mine();
     // POST: http://localhost:12345/transactions/new
       
                     
  


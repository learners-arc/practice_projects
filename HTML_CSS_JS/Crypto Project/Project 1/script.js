var btc = document.getElementById("Bitcoin");
var eth = document.getElementById("Ethereum");
var tet = document.getElementById("Tether");
var xrc = document.getElementById("XRC");

var settings = {
    "async": true,
    "scrossDomain": true,
    "url": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?symbol=BTC,ETH,USDT,XRP&convert=USD",
    "method": "GET"
}

$.ajax(settings).done(function (response) {
    btc.innerHTML = response.Bitcoin.usd;
    eth.innerHTML = response.Ethereum.usd;
    tet.innerHTML = response.Tether.usd;
    xrc.innerHTML = response.XRC.usd;

});



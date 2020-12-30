"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.addHouseMarkers = addHouseMarkers;

var _axiosHelper = require("./axiosHelper.js");

var mapsPlaceholder = [];
var lat;
var lon;
var place;
var mymap = L.map('mapid').setView([53.28209075, -6.408079325], 10);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
var input = document.getElementById("searchAddress");
var autocomplete = new google.maps.places.Autocomplete(input);
autocomplete.setFields(["address_components", "geometry", "icon", "name"]);
autocomplete.addListener("place_changed", function () {
  place = autocomplete.getPlace();
  lat = place.geometry.location.lat();
  lon = place.geometry.location.lng();
  console.log(lat, lon);
});
console.log('hello');
var form = document.getElementById("form");
form.addEventListener('submit', handleForm);

function handleForm(event) {
  console.log('hello');
  event.preventDefault();
  form.style.display = 'none';
  mymap.setView([lat, lon], 15);
  console.log(lat, lon);
  var Address = document.getElementById('searchAddress').value;
  var propertyType = document.getElementById('property-type').value;
  var numBeds = document.getElementById('numBeds').value;
  (0, _axiosHelper.getRentData)(lat, lon, numBeds, propertyType);
  var soldHouses = (0, _axiosHelper.getAddresses)(lat, lon, numBeds, propertyType);
  setTimeout(function afterTwoSeconds() {
    console.log('hellotimer');
    console.log(soldHouses.length);
  }, 10000);
}

function addHouseMarkers(soldHouses) {
  console.log('addHouseMarkers');

  for (var i = 0; i < soldHouses.length; i++) {
    lat = soldHouses[i].lat;
    lon = soldHouses[i].lon;
    var address = soldHouses[i].address;
    var price = soldHouses[i].price;
    console.log(lat);
    var marker = L.marker([lat, lon]).addTo(mymap);
    marker.bindPopup("House Address : " + address + '<br/> Price : ' + price);
  }
}
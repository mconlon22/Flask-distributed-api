"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.getAddresses = getAddresses;
exports.getRentData = getRentData;

var _rentsChart = require("./rentsChart.js");

function getAddresses(lat, lon, Address, numBeds, propertyType) {
  var values = [];
  console.log('propertyType' + propertyType);
  console.log('numBeds' + numBeds);
  console.log(Address);
  var bodyFormData = new FormData();
  bodyFormData.append('lat', lat);
  bodyFormData.append('lon', lon);
  console.log(bodyFormData);
  axios({
    method: 'POST',
    url: 'http://10.97.81.17 /getHousePrices',
    data: bodyFormData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(function (response) {
    //handle success
    (0, _rentsChart.addHouseMarkers)(response.data);
  })["catch"](function (response) {
    //handle error
    console.log('error' + response);
  });
  return values;
}

function getRentData(lat, lon, numBeds, propertyType, callback) {
  var values = [];
  var suburb = '';
  console.log('getting rent data1');
  var bodyFormData = new FormData();
  bodyFormData.append('lat', lat);
  bodyFormData.append('lon', lon);
  bodyFormData.append('numBeds', numBeds);
  bodyFormData.append('propertyType', 'All property types');
  axios({
    method: 'post',
    url: 'http://10.101.185.76/getRentPrices',
    data: bodyFormData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }).then(function (response) {
    //handle success
    response.data.map(function (obj) {
      console.log(obj.Suburb);
      console.log(obj);
      suburb = obj.Suburb;
      values.push(obj.value);
    });
    console.log(values);
    console.log(suburb);
    var ctx = document.getElementById('myChart').getContext('2d');
    var myLineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
        datasets: [{
          label: "Average Rent in ".concat(suburb, " "),
          data: values
        }]
      },
      options: {
        bezierCurve: false,
        //remove curves from your plot
        scaleShowLabels: false,
        //remove labels
        tooltipEvents: [],
        //remove trigger from tooltips so they will'nt be show
        pointDot: false,
        //remove the points markers
        scaleShowGridLines: true //set to false to remove the grids background

      }
    });
  })["catch"](function (response) {
    //handle error
    console.log('error' + response);
  });
}
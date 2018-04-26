var SerialPort = require('serialport');
var port = new SerialPort('/dev/ttyACM0', function (err) {
  if (err) {
    return console.log('Error: ', err.message);
  }
});

port.on('data', function (data) {
  // general debug function: print serial data
  console.log('Data:', data.toString());

  // initial setup: the Arduino sends a'r' character when it's ready to start in its setup() method.
  if(data.toString() == 'r') {
    serAvailable();
  }
});

port.on('open', function() {

});

function serAvailable() {
  port.write('0', function(err) {
    if (err) {
      return console.log('Error on write: ', err.message);
    }
    console.log('message written');
  });
}

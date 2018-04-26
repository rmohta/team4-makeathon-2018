const express = require('express')
const app = express()
var available = false
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
    //serAvailable();
    available = true
  }
});

port.on('open', function() {

});

function writeAvailable(aValue) {
  port.write(aValue, function(err) {
    if (err) {
      return console.log('Error on write: ', err.message);
    }
    //console.log('message written');
  });
}

app.get('/', (req, res) => res.send('Hello from SmartyBin!'))
app.get('/recylce', (req, res) => {
    if(available) {
        writeAvailable('8')
        res.send('Recycling')
    } else {
        res.send('NOT READY to Recycle')
    }
    
})
app.get('/trash', (req, res) =>{
    if(available) {
        writeAvailable('9')
        res.send('Trash')
    } else {
        res.send('NOT READY to Trash')
    }
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))
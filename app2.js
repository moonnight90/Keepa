import WebSocket from "ws";
import decompressTheData from "./app.js";
// WebSocket server URL
const url = 'wss://push.keepa.com/apps/cloud/?app=keepaWebsite&version=2.0';

// Create a WebSocket instance
const ws = new WebSocket(url);

// WebSocket event listeners
ws.on('open', function open() {
  console.log('Connected to WebSocket server');
  
  // Sending a message once connected (optional)
  let msg = "bVS5bhRREPyXF0/Q97HhYIEDY/lYbCNEsJI3sGQu7xgJIf4dvX4eLwFh63XXVFdVz+92WHZPy/bhy/562X353jbo4Mycxmw0tYf7trEMmdryvx6LmDrE8nxoGwKY2s/90+Hh29e24ak97g7Lh+/3u2XfNjC1H8/7p19X+8Pz49I2vxu2zaeGpIAextCmhk5BbkTapjbDfOd29pbet6kBa5CTSG+bIW8vLvzKrvuLsxIiZa4AaYTRX0RRLAPv1hdkF+uFSbILVAEiIZFcH0XlcCH1OLZhFTPE+cdLydPTemFVFwR6LVTNO5omC1FKoWVIKEYUHRRGcpcqwBgsPG2dSUqsFYzTGTA7NKAABWB2aLQQJNLobTP4dptnt3byD4PgwRqVAvXuBVoVBGQtzHyoE+qYboH1IhoUplWwJDIZDkEiSVVrBpmDmDXKLFHCrlxvAw5VcZbSOjyEhGsfYNdgTvIjUYOa0WRTilg1cCQTXM0ClVhZE5u+GJxOIAydATCahBHXpgEK4lnQnWikCY99MoksoRgoIBomry4QCOpIVcgpXmT2VGGKGmMU9Mqa8LXwzK71DOGXdn6TN6uNYWPTGeLNdns229m6nApR6WZIFojFrfJG4qMgBQZ0qI8KpiuCH3VzKACwFAA2rBlhQmY8htw7hxUAGaE2NUcgB5bjlaANdULZzYfbZgFkMOiYOKdTlgsM7kISlXgREgWHyhsCZgBXLEfIVepkksPdk2zMmIop2RpLYoAqULSb5zqOyQKgx3w1C4Ht5TRF2GlwE8C0zGoDRmDRsE6nQ3d7qdBUCADQi+iLOkNRISMiGjkIpLQgLTQwDBAurWdIi7sTl24jWoASuXRBZoik89uLm1I0JV3TaPw26oJTBzSQIA1P60pYyAZAvnn37iZOVkE41BLb5z9TW74tu8fxpzy0TapSouWfvw=="

//   ws.send(new Buffer(msg,'base64'));
});

ws.on('message', function incoming(data) {
  console.log('Received message from server:', data);
  let d = decompressTheData(data.toString('base64'));
  console.log(d);
});

ws.on('close', function close() {
  console.log('Disconnected from WebSocket server');
});

ws.on('error', function error(err) {
  console.error('WebSocket encountered error:', err);
});

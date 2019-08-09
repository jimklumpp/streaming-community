# Web Socket Client Sample

WebSocketClientSample version 1.0 2/26/2015 = Copyright 2014 TIBCO Software, Inc.
Author: Lucus Darnell - TIBCO Software, Inc. (ldarnell@tibco.com)

## Description

The purpose of this sample is to demonstrate how to subscribe & publish messages to a WebSocket server.

If you have any questions or comments about this sample, feel free to email me at ldarnell@tibco.com

## General Usage Notes

In order for this demo to work, you will need access to a WebSocket server. There is a WebSocket server project provided by StreamBase which is accessible by going to: File > Load StreamBase Sample StreamBase Standard Adapters > Web Server Request Response adapters
	  
## Configuration and Usage

* On the event flow, click on WebSocketClient and go to the Operator Properties tab.	
* Enter the URI of the websocket server you wish to connect to.
* Enter the context path you wish to subscribe and publish messages to.
* Save your changes.
* Right-click on "WebSocketClientSample" in the Package Explorer on the left and select: Run As > StreamBase LiveView Project.
* Right-click on "WebSocketClientSample.sbapp" in the Package Explorer on the left and select: Run As > StreamBase Application.
* Launch LiveVie Desktop.
* Under "Workspace", select "Download" and click the "Select..." button.
* Select the project in the list and click the "OK" button.
* Click the "OK" button again to launch the LiveView Desktop. 
* Open "client.html" with a standard web browser (do not use the web browser inside Studio as it does not support WebSockets).
* Enter the full URL (including context path) of your WebSocket server and click the "Connect" button.
* Type a message in the bottom text box and click the "Send" button.
* You should see this message appear in LiveView Desktop.
* In LiveView Desktop, enter a message in the "inputMessage" text box on the right and click the "Submit" button at the bottom-right.
* You should see this message appear in the web browser.
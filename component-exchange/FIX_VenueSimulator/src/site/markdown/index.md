# FIX Venue Simulator

This project provides an application to create an Integration and Stress Test Platform for an application using the 
FIX adapter as a client to an exchange venue. The venue simulator will provide a known response to orders. The known
response is useful in integration testing for your client order-submission algorithms. It proves 
especially useful in a stress-test environment where you want repeatable tests that give same the results and 
application loads for the same inputs.

To run the demo, start the Demo_FIXVenueSimulator.sbapp application in StreamBase Studio or on the StreamBase command line. 
Instead of manually triggering an order, for a demo mode you can run the feed simulation demo.sbfs (from the Test/Debug perspective's 
"Feed Simulation" panel) to supply one order per second (by default). This feed simulation will vary along several stock 
symbols and the two configured venues (FIX sessions). Alternately, you can start the feed simulation by sending a (null) 
tuple into the FeedSim_ToggleOnOff input stream.

As configured here, there are two FIX sessions created and used by the feed simulation ("VENUE1" and "VENUE2"). 
You can configure others by editing the client and server cfg files provided (QuickFix/J configuration format). 
You can vary the venue simulation fill rates and (partial) fill quantities as discussed below.

There are 4 parameters that are set up in the sbd.sbconf file to control fill rates. These are:
1. FillRate: The Rate at which to fill orders in the order book (Day, GTC), in number of seconds (1/2 second between each fill)
 	**\<operator-parameter name="FillRate" value="0.5"/>**
2. FillQty: The quantity to fill each order (300 shares per fill, up to the complete order) 
 	**\<operator-parameter name="FillQty" value="300"/>**
3. IOCFillRt: The "rate" at which to cancel IOC orders (3 translates to filling every third order -- cancel the rest) 	
 	**\<operator-parameter name="IOCFillRt" value="3"/>**
4. FillSleepMilliSecs: number of milliseconds to sleep between sending each partial fill in the orderBook 
 	**\<operator-parameter name="FillSleepMilliSecs" value="1"/>**
 	consider that the new order arrival rate (steady state open orders), the FillRate and FillSleepMilliSecs 
 	need to be rational. It would be safest and reasonable to set FillSleepMilliSecs to '0'.

The example client (with embedded, concurrent venue simulator) is supplied in the Demo_FIXVenueSimulator.sbapp. 
Supply a single order request to the "ManuallyCreateNewOrder" input stream with the fields:
* TimeInForce (0 or 1 for a Order Book entry that will slowly fill, or 3 for a Immediate-or-Cancel order)
* Symbol (traded product identifying ticker)
* session (a string that should match one of the Venue session names in the FIX cfg files, defined here as 
 "VENUE1" and "VENUE2")

You can run this as a Venue-Simulation-only application by running FIXsimulatorVenueOnly.sbapp at the
StreamBase command line prompt with this command: 
     `sbd -f sbd.sbconf FIXsimulatorVenueOnly.sbapp`

To integrate this into your test environment, investigate the CreateClientOrder.sbapp to see 
how basic orders and cancels are submitted. You can modify fixServer.sbapp to add or change venue features.

The example client FIX adapter is set up in Trace mode so that full display of FIX data is displayed on the 
console. In a performance test environment, disable trace mode to supress the verbose output.
 
All components are in sub-folders as listed here:

Component Folder|Purpose
----------------|--------
project folder|Demo_FIXVenueSimulator.sbapp -- the demo. <br> FIXsimulatorVenueOnly.sbapp -- to run the Venue Server only.
VenueSimulation|contains the Venue simulator sbapps (parent and fillModule).
FIX_data|this will contain the FIX data store and logs for the various FIX sessions subfolders and files are automatically created by the QuickFIX software upon application startup.
Test|contains the client test/demo application module and feed simulation.
reference|the StreamBase schema definitions for various FIX message types. If you need to add additional fields to an execution report, for example, edit the schema, and have the CompIDswitch in fixServer.sbapp pass this added field (and add logic to set the field value).
					
					


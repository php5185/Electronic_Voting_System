package visual;

import gnu.io.CommPortIdentifier;
import gnu.io.PortInUseException;
import gnu.io.SerialPort;
import gnu.io.SerialPortEvent;
import gnu.io.SerialPortEventListener;
import gnu.io.UnsupportedCommOperationException;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Date;
import java.util.Enumeration;
import java.util.TooManyListenersException;

/*import com.positiveaccess.idecode.IDecode;
import com.positiveaccess.idecode.IDriversLicense;
import com.positiveaccess.idecode.IFormat;
 */
/**
 * Class declaration
 * 
 * 
 * @author
 * @version 1.8, 08/03/00
 */
public class ComControl implements Runnable, SerialPortEventListener{
	static CommPortIdentifier portId1;
	InputStream inputStream;
	byte[] totalReadBuffer = null;
	SerialPort serialPort1;
	Thread readThread;
	protected String divertCode = "10";
	static String TimeStamp;
	String scannedInput = "";
	String tempInput = "";

	public static void main(String[] args){
		try{
			Enumeration ports = CommPortIdentifier.getPortIdentifiers();
			
			while(ports.hasMoreElements()){
				CommPortIdentifier port = (CommPortIdentifier) ports.nextElement();
				String type;
				switch(port.getPortType()){
				case CommPortIdentifier.PORT_PARALLEL:
					type = "Parallel";
					break;
				case CommPortIdentifier.PORT_SERIAL:
					type = "Serial";
					break;
				default: // / Shouldn't happen
					type = "Unknown";
					break;
				}
				System.out.println(port.getName() + ": " + type);
			}

			portId1 = CommPortIdentifier.getPortIdentifier("COM6");//llamar esas lineas
			ComControl reader = new ComControl();
			//System.out.println("lololo");
		}

		catch(Exception e){
			TimeStamp = new java.util.Date().toString();
		}
	};

	public ComControl(){
		try{
			TimeStamp = new java.util.Date().toString();
			serialPort1 = (SerialPort) portId1.open("ComControl", 2000);
		}
		catch(PortInUseException e) {
		}
		try {
			inputStream = serialPort1.getInputStream();
		}
		catch(IOException e){
			e.printStackTrace();
		}
		try {
			serialPort1.addEventListener(this);
		}
		catch(TooManyListenersException e) {
		}
		serialPort1.notifyOnDataAvailable(true);
		try {
			serialPort1.setSerialPortParams(9600,
					SerialPort.DATABITS_8,
					SerialPort.STOPBITS_1,
					SerialPort.PARITY_NONE);

			serialPort1.setDTR(false);
			serialPort1.setRTS(false);

		}
		catch(UnsupportedCommOperationException e) {
			e.printStackTrace();
		}

		readThread = new Thread(this);
		readThread.start();
		//System.out.println("es quei a");
	}

	/**
	 * Method declaration
	 * 
	 * 
	 * @see
	 */
	public void run() {
		while(true){
		try {
			Thread.sleep(30000);
		}
		catch(InterruptedException e)      {
			e.printStackTrace();
		}
	}
	}

	/**
	 * Method declaration
	 * 
	 * 
	 * @param event
	 * 
	 * @see
	 */
	public void serialEvent(SerialPortEvent event)   {
		switch(event.getEventType())
      {
      case SerialPortEvent.BI:
      case SerialPortEvent.OE:
      case SerialPortEvent.FE:
      case SerialPortEvent.PE:
      case SerialPortEvent.CD:
      case SerialPortEvent.CTS:
      case SerialPortEvent.DSR:
      case SerialPortEvent.RI:
      case SerialPortEvent.OUTPUT_BUFFER_EMPTY:
         break;
      case SerialPortEvent.DATA_AVAILABLE:
         //TimeStamp = new java.util.Date().toString();
        // System.out.println("*DATA avail: " + TimeStamp);
		 
		//while (true){
		//if (event.getEventType() == SerialPortEvent.DATA_AVAILABLE) {
			try
			{
				System.out.println("count: " + inputStream.available());
				byte[] readBuffer = new byte[inputStream.available()];
				//while(inputStream.available() > 0)
				//{
					int numBytes = inputStream.read(readBuffer);
				//}
				totalReadBuffer = readBuffer;
				System.out.print(new String(readBuffer));
				
				String lectura = new String(readBuffer);
				/*String bien = lectura.replaceAll("\\s","");
				if(bien.equalsIgnoreCase("ALP") || bien.equalsIgnoreCase("PRSC")){
					System.out.print("LO LLE BIEN CREO");
				};*/
				
				
			}
			catch(IOException e)         {
			}
			catch(Exception ex)         {
				ex.printStackTrace();
			}
			break;
		}
	}
	//}
}
package visual;

import gnu.io.CommPortIdentifier;
import gnu.io.PortInUseException;
import gnu.io.SerialPort;
import gnu.io.SerialPortEvent;
import gnu.io.SerialPortEventListener;
import gnu.io.UnsupportedCommOperationException;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Desktop;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;

import javax.swing.DefaultComboBoxModel;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.border.EmptyBorder;
import javax.swing.border.EtchedBorder;
import javax.swing.border.LineBorder;
import javax.swing.border.TitledBorder;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumnModel;

import gnu.io.CommPortIdentifier;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.TooManyListenersException;

import javax.swing.SwingConstants;
import javax.swing.JTextField;

import org.apache.pdfbox.jbig2.segments.Table;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.PDPageContentStream;
import org.apache.pdfbox.pdmodel.font.PDType1Font;


public class Conteo extends JDialog implements Runnable, SerialPortEventListener{
	private Dimension dim;
	private final JPanel contentPanel = new JPanel();
	private static JTable table;
	private static Object[] fila;
	private static DefaultTableModel tableModel;
	private JButton btnCancelar;
	private String code;
	private int numero=0;
	JButton btnVotoNulo;

	///serial
	static CommPortIdentifier portId1;
	InputStream inputStream;
	byte[] totalReadBuffer = null;
	SerialPort serialPort1;
	Thread readThread;
	protected String divertCode = "10";
	static String TimeStamp;
	String scannedInput = "";
	String tempInput = "";


	private final int PUERTO = 5556; //Puerto para la conexión
	private final String HOST = "192.168.40.2"; //Host para la conexión
	protected String mensajeServidor; //Mensajes entrantes (recibidos) en el servidor
	protected ServerSocket ss; //Socket del servidor
	protected Socket cs; //Socket del cliente
	protected DataOutputStream salidaServidor, salidaCliente; //Flujo de datos de salida
	protected DataInputStream leer, bufferDeEntrada;


	public static ArrayList<String> partidos = new ArrayList(Arrays.asList("ALPAIS","APD","BIS","FNP","Frente Amplio","MODA","PAL","PHD","PLD","PQDC","PRD","PRI","PRM","PRSC","PRSD","PTD","PUN","UDC"));
	public static ArrayList<String> nombre = new ArrayList(Arrays.asList("Alianza Paaís","Partido Alianza por la Democracia","Bloque Institucional Socialista Demócrata","Fuerza Nacional Progresista","Frente Amplio","Movimiento Democrático Alternativo","Partido de Acción Liberal","Partido Humanitario Dominicano","Partido de la Liberación Dominicana","Partido Quisqueyano Demócrata Cristiano","Partido de la Revolución Dominicana","Partido Revolucionario Independiente","Partido Revolucionario Moderno","Partido Reformista Social Cristiano","Partido Revolucionario Social Demócrata","Partido de los Trabajadores Dominicanos","Partido de Unidad Nacional","Partido Unión Democrática Cristiana"));
	public static ArrayList<Integer> conteo = new ArrayList(Arrays.asList(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0));
	public static int nulos=0;

	private static String observ="0";
	private static int obser=0;
	private JTextField txtNulos;
	private JTextField txtMesa;


	/**
	 * Launch the application.
	 */
	/*
	public static void main(String[] args) {
		try {
			String imp="jj";
			Conteo dialog = new Conteo(imp, imp, imp);
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	 */

	/**
	 * Create the dialog.
	 */
	public Conteo(final String lectura, final String orden, final String myPass) {

		setIconImage(Toolkit.getDefaultToolkit().getImage(Conteo.class.getResource("/Icon/copyjce.png")));
		setTitle("Listado de Compa\u00F1\u00EDas");
		setModal(true);
		setResizable(false);
		setBounds(100, 100, 1335, 735);
		dim = super.getToolkit().getScreenSize(); 
		super.setSize(dim.width+12, dim.height-33);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBackground(Color.WHITE);
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);

		JPanel panel = new JPanel();
		panel.setBorder(new LineBorder(new Color(204, 153, 0)));
		panel.setFocusable(false);
		panel.setBackground(Color.WHITE);
		panel.setBounds(10, 11, 1346, 654);
		contentPanel.add(panel);
		panel.setLayout(null);

		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(234, 126, 875, 514);
		panel.add(scrollPane);

		table = new javax.swing.JTable(){
			public boolean isCellEditable(int rowIndex, int colIndex) {
				return false; 
			}
		};
		table.setShowGrid(false);
		table.setShowHorizontalLines(false);
		table.setShowVerticalLines(false);

		tableModel = new DefaultTableModel();
		String[] columnNames = {"No.","Asociación Política","Sigla Asoc. Política","Tipo de Voto"};
		tableModel.setColumnIdentifiers(columnNames);
		loadTablaSol(0);
		scrollPane.setViewportView(table);

		JLabel lbljunta = new JLabel("");
		lbljunta.setBounds(492, 12, 359, 63);
		lbljunta.setIcon(new ImageIcon(Conteo.class.getResource("/Icon/junta.png")));
		panel.add(lbljunta);

		JLabel lblNewLabel_2 = new JLabel("ELECCIONES ORDINARIAS GENERALES DEL 17 DE MAYO DEL 2020 PARA ELEGIR AL PRESIDENTE Y VICEPRESIDENTE DE LA REPUBLICA");
		lblNewLabel_2.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_2.setBounds(214, 87, 915, 27);
		panel.add(lblNewLabel_2);

		JLabel Escudo = new JLabel("");
		Escudo.setBounds(85, 12, 60, 60);
		Escudo.setIcon(new ImageIcon(Conteo.class.getResource("/Icon/escudo.png")));
		panel.add(Escudo);

		JLabel label = new JLabel("");
		label.setBounds(1198, 12, 60, 60);
		label.setIcon(new ImageIcon(Conteo.class.getResource("/Icon/escudo.png")));
		panel.add(label);

		JLabel lblCantidadDeVotos = new JLabel("Cant. de Votos Nulos:");
		lblCantidadDeVotos.setBounds(1165, 585, 171, 22);
		panel.add(lblCantidadDeVotos);

		txtNulos = new JTextField();
		txtNulos.setEditable(false);
		txtNulos.setText(Integer.toString(nulos));
		txtNulos.setBounds(1165, 618, 127, 22);
		panel.add(txtNulos);
		txtNulos.setColumns(10);
		
		JLabel lblMesaElectoral = new JLabel("Mesa Electoral:");
		lblMesaElectoral.setBounds(1165, 518, 127, 21);
		panel.add(lblMesaElectoral);
		
		txtMesa = new JTextField();
		txtMesa.setEditable(false);
		txtMesa.setBounds(1165, 552, 127, 20);
		txtMesa.setText(lectura);//agregé todo eso
		panel.add(txtMesa);
		txtMesa.setColumns(10);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setBorder(new EtchedBorder(EtchedBorder.LOWERED, null, null));
			buttonPane.setBackground(Color.WHITE);
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				btnCancelar = new JButton("Cancelar");
				btnCancelar.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						int reply = JOptionPane.showConfirmDialog(null, "Se Perderán todos los Datos. ¿Desea Continuar?", null, JOptionPane.YES_NO_OPTION);
						if (reply == JOptionPane.YES_OPTION) {
							dispose();
						}


					}
				});

				JButton btnVotoObservado = new JButton("Voto Observado");
				btnVotoObservado.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent arg0) {
						Observado obs = new Observado(lectura, myPass); 
						obs.setModal(true);
						obs.setLocationRelativeTo(null);						
						obs.setVisible(true);
						obs.setResizable(false);		

					}
				});

				JButton btnEnviarEImprimir = new JButton("Enviar e Imprimir");
				btnEnviarEImprimir.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent arg0) {
						//System.out.println("los resultados");
						String env ="";

						for(int aux: conteo){
							env+=Integer.toString(aux);
							env+=",";
						}

						//0,3 primera vez, 0,4 para revision
						String ver1="";		
						String envio = "0,3,"+lectura+",1,"+observ+",0,"+env+"0,"+nulos;
						if(orden.equalsIgnoreCase("1,1,1,0")){
							envio = "0,3,"+lectura+",1,"+observ+",1,"+env+"1,"+nulos;
						}

						//String envio = "0,3,"+lectura+",1,"+observ;
						try
						{
							cs =new Socket();
							cs.connect(new InetSocketAddress(HOST, PUERTO),10000);
							//cs = new Socket(HOST, PUERTO);
							//Flujo de datos hacia el servidor
							salidaServidor = new DataOutputStream(cs.getOutputStream());

							salidaServidor.writeUTF(envio);
					
							BufferedReader entrada = new BufferedReader(new InputStreamReader(cs.getInputStream()));

							while((mensajeServidor = entrada.readLine()) != null) //Mientras haya mensajes desde el cliente
							{
								ver1=mensajeServidor;
							}
							/////hacer lo del pdf aqui

							/*while((mensajeServidor = entrada.readLine()) != null) //Mientras haya mensajes desde el cliente
				            {
				                //Se muestra por pantalla el mensaje recibido
				                System.out.println(mensajeServidor);
				                ver2=mensajeServidor;
				            }*/

							/*String[] dos=ver1.split("0");
							System.out.println("dos en 0: "+dos[0]);

							String[] aux= dos[0].split(",");
							for(String ll: aux){
								partidos.add(ll);
								conteo.add(0);
							}
							String[] aux1= dos[1].split(",");
							for(String ll: aux1){
								nombre.add(ll);
								//conteo.add(0);
							}*/

							cs.close();//Fin de la conexión

						}
						catch (Exception e)
						{
							JOptionPane.showMessageDialog(null, "Fallo en la conexión con el servidor remoto", null, JOptionPane.ERROR_MESSAGE, null);
							//System.out.println("fallo total \n");
							//System.out.println(e.getMessage());
						}



						/*
						System.out.println(env);

						//System.out.println(nombre);
						System.out.println(partidos);						
						System.out.println(conteo);*/












						///////////////////////////pdf   pdf PDF PDF//////////////////////////////				





						dispose();
						PDDocument document = new PDDocument();
						PDPage page = new PDPage();
						document.addPage(page);
						try { 
							PDPageContentStream contentStream = new PDPageContentStream(document, page);

							contentStream.beginText();

							contentStream.setFont( PDType1Font.TIMES_ROMAN, 18 );

							//Setting the leading
							contentStream.setLeading(14.5f);

							//Setting the position for the line
							contentStream.newLineAtOffset(10, 750);
							contentStream.showText("                                          JUNTA CENTRAL ELECTORAL");

							contentStream.newLine();
							contentStream.setFont( PDType1Font.TIMES_ROMAN, 14 );
							contentStream.showText("                                   ELECCIONES ORDINARIAS GENERALES PRESIDENCIALES");
							contentStream.newLine();
							contentStream.showText("                                                               DEL 17 DE MAYO DEL 2020");
							contentStream.newLine();
							contentStream.newLine();
							contentStream.setFont( PDType1Font.TIMES_ROMAN, 16 );
							contentStream.showText("                                                  MESA ELECTORAL "+lectura);

							contentStream.newLine();
							contentStream.newLine();
							contentStream.setFont( PDType1Font.TIMES_ROMAN, 13 );
							contentStream.showText("      No.           Votos                 Agrupación Política                                          Firmas de Miembros");
							contentStream.setFont( PDType1Font.TIMES_ROMAN, 16 );
							contentStream.newLine();

							int no=4;
							int agrupa=60;
							int tot = 5;

							String sno="";
							String ssigla="";
							String sagrupa="";							
							String stotal="";
							//String fina="";

							for(int i=0; i<partidos.size(); i++){
								if(i<=8){
									sno =relleno(Integer.toString(i+1), 20);
								}								
								else if(i>=9){
									sno =relleno(Integer.toString(i+1), 19);
								}


								//ssigla=relleno(partidos.get(i), 20);
								ssigla=partidos.get(i);
								//sagrupa=relleno(nombre.get(i),50);
								sagrupa=nombre.get(i);
								stotal=rellenototal(Integer.toString(conteo.get(i)), 3);
								//relleno(Integer.toString(conteo.get(i)), 3);
								stotal=relleno(stotal, 20);

								contentStream.newLine();
								contentStream.setFont( PDType1Font.TIMES_ROMAN, 12 );

								contentStream.showText("      "+sno + stotal+ ssigla);//+" ("+ ssigla +")");								
								contentStream.setFont( PDType1Font.TIMES_ROMAN, 8 );
								contentStream.showText("  ("+sagrupa+")                                        ");//+" ("+ ssigla +")");

								if(i==0){
									contentStream.showText("                                                          Presidente");//+" ("+ ssigla +")");
								}
								if(i==2){
									contentStream.showText("                       Secretario");//+" ("+ ssigla +")");
								}
								if(i==4){
									contentStream.showText("                                         Primer Vocal");//+" ("+ ssigla +")");
								}
								if(i==6){
									contentStream.showText("                                               Segundo Vocal");//+" ("+ ssigla +")");
								}
								if(i==8){
									contentStream.showText("                             Sustituto de Secretario");//+" ("+ ssigla +")");
								}

								if(i==9){
									contentStream.setFont( PDType1Font.TIMES_ROMAN, 10 );
									contentStream.showText("       Delegados");//+" ("+ ssigla +")");
								}
								if(i==10){
									contentStream.showText("                          1.___________________");
								}
								if(i==11){
									contentStream.showText("                            2.___________________");
								}
								if(i==12){
									contentStream.showText("                                 3.___________________");
								}
								if(i==13){
									contentStream.showText("                           4.___________________");
								}
								if(i==14){
									contentStream.showText("                5.___________________");
								}
								if(i==15){
									contentStream.showText("                     6.___________________");
								}
								if(i==16){
									contentStream.showText("                                          7.___________________");
								}
								if(i==17){
									contentStream.showText("                          8.___________________");
								}


								/*if(i==10){
									sno =relleno(Integer.toString(i+1), 20);
									contentStream.newLine();
									contentStream.showText(sno + stotal+ sagrupa+" ("+ ssigla +")");
								}*/
								//contentStream.showText(sno + stotal+ sagrupa+" ("+ ssigla +")");

								//System.out.println(sno.length()+"  "+stotal.length()+"  "+ssigla.length()+"  "+sagrupa.length()+"  ");

							}
							int all=total()+nulos;
							int validos=all-obser-nulos;
							
							System.out.println(18);
							contentStream.newLine();
							contentStream.setFont( PDType1Font.TIMES_ROMAN, 13 );
							contentStream.newLine();
							contentStream.showText("      Total de Votos Válidos:          "+rellenototal(Integer.toString(validos), 3));

							contentStream.newLine();
							contentStream.showText("      Total de Votos Observados:    "+rellenototal(Integer.toString(obser), 3));
							contentStream.newLine();
							contentStream.showText("      Total de Votos Nulos:             "+rellenototal(Integer.toString(nulos), 3));
							contentStream.newLine();
							contentStream.showText("      Total de Votos Emitidos:        "+rellenototal(Integer.toString(all), 3));


							contentStream.endText();
							contentStream.close();
							
							//document.save("C:/Users/Prueba/Desktop/eclipse/pdfBoxHelloWorld.pdf");

							String directory ="C:/Users/paola/Desktop/JCE/Resultados"+lectura+".pdf";
							document.save(directory);//"C:/Users/paola/Desktop/JCE/Resultados.pdf");
							document.close();

							if(Desktop.isDesktopSupported()){
								try{
									File theUMFile =new File(directory);
									Desktop.getDesktop().open(theUMFile);
								}
								catch(FileNotFoundException fnf){
									
								}
								catch(IllegalArgumentException fnf){

								}
								catch(IOException ex){

								}
							}


							//dispose();//quite eso
							conteo.clear();
							for(int y=0; y<18; y++){
								conteo.add(0);
							}
							//conteo = Arrays.asList(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0));
							observ="0";
							obser=0;
							nulos=0;
							



						} 
						catch (IOException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}

					}
				});				
				btnEnviarEImprimir.setIcon(new ImageIcon(Conteo.class.getResource("/Icon/Ok_opt.png")));
				buttonPane.add(btnEnviarEImprimir);
				btnVotoObservado.setIcon(new ImageIcon(Conteo.class.getResource("/Icon/search-icon-11851.png")));
				buttonPane.add(btnVotoObservado);

				JButton btnVotoNulo_1 = new JButton("Voto Nulo");
				btnVotoNulo_1.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent arg0) {
						Nulo obs = new Nulo(lectura, myPass); 
						obs.setModal(true);
						obs.setLocationRelativeTo(null);						
						obs.setVisible(true);
						obs.setResizable(false);
						txtNulos.setText(Integer.toString(nulos));

					}
				});
				btnVotoNulo_1.setIcon(new ImageIcon(Conteo.class.getResource("/Icon/menos.jpg")));
				buttonPane.add(btnVotoNulo_1);

				//btnVotoNulo = new JButton("Voto Nulo");
				//buttonPane.add(btnVotoNulo);
				btnCancelar.setIcon(new ImageIcon(Conteo.class.getResource("/Icon/close-btn.png")));
				//btnVotoNulo.setIcon(new ImageIcon(Conteo.class.getResource("/Icon/menos.png")));
				btnCancelar.setActionCommand("Cancel");
				buttonPane.add(btnCancelar);
			}
		}	











		String ver="";
		String ver2="";
		String envio = "0,2";
		/*try
		{
			cs = new Socket(HOST, PUERTO);
			//cs =new Socket();
			//cs.connect(new InetSocketAddress(HOST, PUERTO),5000);
			//Flujo de datos hacia el servidor
			salidaServidor = new DataOutputStream(cs.getOutputStream());

			salidaServidor.writeUTF(envio);

			BufferedReader entrada = new BufferedReader(new InputStreamReader(cs.getInputStream()));
			
			
			
			while((mensajeServidor = entrada.readLine()) != null) //Mientras haya mensajes desde el cliente
			{
				//Se muestra por pantalla el mensaje recibido
				System.out.println(mensajeServidor);
				ver=mensajeServidor;
				//ver.
			}

			/*while((mensajeServidor = entrada.readLine()) != null) //Mientras haya mensajes desde el cliente
            {
                //Se muestra por pantalla el mensaje recibido
                System.out.println(mensajeServidor);
                ver2=mensajeServidor;
            }*/

			/*String[] dos=ver.split("0");
			

			String[] aux= dos[0].split(",");
			for(String ll: aux){
				partidos.add(ll);
				conteo.add(0);
			}
			String[] aux1= dos[1].split(",");
			for(String ll: aux1){
				nombre.add(ll);
				//conteo.add(0);
			}

			cs.close();//Fin de la conexión


		}
		catch (Exception e)
		{
		}*/

















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
				
			}

			portId1 = CommPortIdentifier.getPortIdentifier("COM6");//llamar esas lineas
			//ComControl reader = new ComControl();



			//////////////////////
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




			///////////////////////////



			//poner aqui la funcion entera de concontrol
		}	
		catch(Exception e){
			TimeStamp = new java.util.Date().toString();
		}













	}

	public static void loadTablaSol(int selection) {
		tableModel.setRowCount(0);
		fila = new Object[tableModel.getColumnCount()];


		table.setModel(tableModel);
		table.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
		table.getTableHeader().setReorderingAllowed(false);
		TableColumnModel columnModel = table.getColumnModel();
		columnModel.getColumn(0).setPreferredWidth(137);
		columnModel.getColumn(1).setPreferredWidth(320);
		columnModel.getColumn(2).setPreferredWidth(245);
		columnModel.getColumn(3).setPreferredWidth(170);
		/*columnModel.getColumn(4).setPreferredWidth(170);
		columnModel.getColumn(5).setPreferredWidth(173);
		 */

	}

	public String rellenototal(String can, int rell){
		String relleno="0";
		String nada="";
		int lc=can.length();
		for(int ca=lc; ca<rell; ca++){
			nada+=relleno;
		}
		can=nada+can;
		return can;

	}
	public String relleno(String can, int rell){
		String relleno=" ";
		//String can= Integer.toString(cant); 
		int lc=can.length();
		for(int ca=lc; ca<rell; ca++) {
			can=can+relleno;
		}
		return can;
	}

	/*	@SuppressWarnings("deprecation")
	public static void drawTable(PDPage page, PDPageContentStream contentStream,
			float y, float margin,
			String[][] content) throws IOException {
		final int rows = content.length;
		final int cols = content[0].length;
		final float rowHeight = 20f;
		final float tableWidth = page.getMediaBox().getWidth()-(2*margin);
		final float tableHeight = rowHeight * rows;
		final float colWidth = tableWidth/(float)cols;
		final float cellMargin=5f;

		//draw the rows
		float nexty = y ;
		for (int i = 0; i <= rows; i++) {
			contentStream.drawLine(margin,nexty,margin+tableWidth,nexty);
			nexty-= rowHeight;
		}

		//draw the columns
		float nextx = margin;
		for (int i = 0; i <= cols; i++) {
			contentStream.drawLine(nextx,y,nextx,y-tableHeight);
			nextx += colWidth;
		}

		//now add the text
		contentStream.setFont(PDType1Font.HELVETICA_BOLD,12);

		float textx = margin+cellMargin;
		float texty = y-15;
		for(int i = 0; i < content.length; i++){
			for(int j = 0 ; j < content[i].length; j++){
				String text = content[i][j];
				contentStream.beginText();
				contentStream.moveTextPositionByAmount(textx,texty);
				contentStream.drawString(text);
				contentStream.endText();
				textx += colWidth;
			}
			texty-=rowHeight;
			textx = margin+cellMargin;
		}
	}

	 */
	public static int total(){
		int total=0;
		for(int i=0; i<conteo.size(); i++){
			total+=conteo.get(i);
		}
		return total;
	}
	public static int count(String lectu, String tipo){
		int i=0;
		int res=0;
		if (lectu.equalsIgnoreCase("FRE")){
			lectu="Frente Amplio";
		}
		if (lectu.equalsIgnoreCase("ALP")){
			lectu="ALPAIS";
		}
		
		for(String aux: partidos){

			if(aux.equalsIgnoreCase(lectu)){
				
				fila[0]=numerovoto();
				fila[1]=nombre.get(i);//"Normal";
				fila[2]=lectu;
				fila[3]=tipo;
				tableModel.addRow(fila);

				if(tipo.equalsIgnoreCase("Observado")){
					observ="1";
					obser+=1;
				}

				int nume= conteo.get(i)+1;
				conteo.set(i, nume);
				res=1;
				return 1;
			}
			i++;

		}
		return res;		

	}

	public static int numerovoto(){
		int cont=0;
		for(Integer aux: conteo){
			cont+=aux;
		}
		return cont+1;
	}


	public void run() {
		while(true){//agrege eso
			try {
				Thread.sleep(100);
			}
			catch(InterruptedException e)      {
				e.printStackTrace();
			}
		}
	}


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
				
				byte[] readBuffer = new byte[inputStream.available()];
				//while(inputStream.available() > 0)
				//{
				int numBytes = inputStream.read(readBuffer);
				//}
				totalReadBuffer = readBuffer;
				//System.out.print(new String(readBuffer));
				String lectura= new String(readBuffer); 
				//System.out.println(lectura);
				//prueba.setText(new String(readBuffer));
				//int display= numero +1;
				String bien = lectura.replaceAll("\\s","");


				///////////////////////////////////////////////////////////////////////////////
				//poner un if para buscar la mesa en el servidor				
				int hey =count(bien, "Normal");
				//numero=+1;
				if (hey==0){
					JOptionPane.showMessageDialog(null, "Asociación Política no válida", null, JOptionPane.ERROR_MESSAGE, null);
				}

				//conectarme a la base de datos para verificar el codigo 
			}
			catch(IOException e)         {
			}
			catch(Exception ex)         {
				ex.printStackTrace();
			}
			break;
		}
	}
}

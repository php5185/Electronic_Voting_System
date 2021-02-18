package visual;

import java.io.IOException;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.PDPageContentStream;
import org.apache.pdfbox.pdmodel.font.PDType1Font;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class pdfbox {
	private static ArrayList<String> presidente = new ArrayList<>();
	private static ArrayList<Integer> votoPresi = new ArrayList<>();
	private static String []info = new String[3];
	private static String []info2 = new String[3];


	public static void main(String[] args) {
		String ganador = null, empate=null, vicepres=null, empvice=null;
		int cant=0, cantemp=0;
		boolean segunda =false;

		try { //para conectarse a la base de datos
			int total=0;

			Connection myConn = DriverManager.getConnection("jdbc:mariadb://localhost:3306/voto?user=root&password=microena");
			Statement myStmt = myConn.createStatement();

			ResultSet cantvotos = myStmt.executeQuery("SELECT COUNT(*) FROM Registro_voto");
			while (cantvotos.next()){
				total =Integer.parseInt(cantvotos.getString(1));
				}


			ResultSet pres = myStmt.executeQuery("SELECT DISTINCT presidente FROM Registro_voto");

			while (pres.next()){
				presidente.add(pres.getString(1));
				
			}


			//contar los votos de cada candidato de las presidenciales 
			ResultSet votopres;
			String presiden;
			for(String aux: presidente) {

				presiden="SELECT COUNT(presidente) as hola FROM Registro_voto WHERE presidente='"+aux+"'";
				votopres= myStmt.executeQuery(presiden);
				while(votopres.next()) {
					votoPresi.add(votopres.getInt(1));
				}

			}




			//buscar el ganador

			int i, pos =0, posemp=0;


			int max = Integer.MIN_VALUE;
			for(int p=0; p<votoPresi.size(); p++){
				if(votoPresi.get(p) > max){
					max = votoPresi.get(p);
					cant=max;
					pos=p;
				}
			}

			if(((total/50)+1)<cant) {
				ganador= presidente.get(pos);
				vicepres=getVicepresidente(ganador);
				//buscar al vice y generar el pdf

			}
			else {

				segunda=true;
				ganador= presidente.get(pos);
				vicepres=getVicepresidente(ganador);

				for(int p=0; p<votoPresi.size(); p++){
					if(votoPresi.get(p) > max & p!=pos){
						max = votoPresi.get(p);
						cantemp=max;
						posemp=p;
					}
				}

				empate=presidente.get(posemp);
				empvice=getVicepresidente(empate);
				//buscar el vice se puede hacer una funcion y generar el pdf
			}  

		}
		catch (Exception exc) {
			exc.printStackTrace();

		}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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
			contentStream.showText("                                        LISTADO DE CANDIDATOS GANADORES");

			contentStream.newLine();
			contentStream.setFont( PDType1Font.TIMES_ROMAN, 13 );
			contentStream.showText(" CARGO                 POSICION         VOTOS           PARTIDO       CEDULA             NOMBRE");

			contentStream.newLine();
			contentStream.newLine();
			contentStream.setFont( PDType1Font.TIMES_ROMAN, 16 );
			contentStream.showText(" NIVEL PRESIDENCIAL");


			contentStream.newLine();
			contentStream.newLine();

			getInfo(ganador);
	

			String relleno=" ";
			String can= Integer.toString(cant); 
			int lc=can.length();
			for(int ca=lc; ca<20; ca++) {
				can=can+relleno;
			}
			
			String par= info[0]; 
			int part=info[0].length();
			for(int ca=part; ca<21; ca++) {
				par=par+relleno;
			}


			contentStream.newLine();
			contentStream.setFont( PDType1Font.TIMES_ROMAN, 12 );
			contentStream.showText( " PRESIDENTE                   1                        "+can+"  "+par+info[1]+"         "+ganador);

			contentStream.newLine();
			contentStream.setFont( PDType1Font.TIMES_ROMAN, 12 );
			contentStream.showText( " VICEPRESIDENTE          1                        "+can+"  "+par+info[2]+"         "+vicepres);
			contentStream.newLine();
			
			
			if (segunda) {
				
				String canemp= Integer.toString(cantemp); 
				int len=canemp.length();
				for(int ca=len; ca<20; ca++) {
					canemp=canemp+relleno;
				}
				
				getInfo2(empate);
				
				String parem= info2[0]; 
				int parte=info2[0].length();
				for(int ca=parte; ca<21; ca++) {
					parem=parem+relleno;
				}
				contentStream.newLine();
				contentStream.setFont( PDType1Font.TIMES_ROMAN, 12 );
				contentStream.showText( " PRESIDENTE                   2                        "+canemp+"  "+parem+info2[1]+"         "+empate);

				contentStream.newLine();
				contentStream.setFont( PDType1Font.TIMES_ROMAN, 12 );
				contentStream.showText( " VICEPRESIDENTE          2                        "+canemp+"  "+parem+info2[2]+"         "+empvice);
					
				
				
			}


			contentStream.endText();
			contentStream.close();

			document.save("C:/Users/Prueba/Desktop/eclipse/pdfBoxHelloWorld.pdf");
			document.close();
		} 
		catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}




	private static String getVicepresidente(String presidente) {
		String vicepresidente=null;
		try {
			Connection myConn = DriverManager.getConnection("jdbc:mariadb://localhost:3306/voto?user=root&password=microena");
			Statement myStmt = myConn.createStatement();
			ResultSet mesa = myStmt.executeQuery("SELECT vicepresidente FROM Registro_voto WHERE presidente='"+presidente+"' LIMIT 1");

			while (mesa.next()){
				//mesa_electoral.add(mesa.getString(1));
				vicepresidente=mesa.getString(1);
			}
		}
		catch (Exception exc) {
			exc.printStackTrace();

		}
		return vicepresidente;

	}

	private static void getInfo(String nombre) {

		try {
			Connection myConn = DriverManager.getConnection("jdbc:mariadb://votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com:3306/votacion?user=prueba&password=holahola");
			Statement myStmt = myConn.createStatement();

			ResultSet mesa = myStmt.executeQuery("SELECT sigla_partido, cedula_presidente, cedula_vicepresidente FROM Candidatos WHERE original=1 AND nombre_presidente='"+nombre+"'");
			
			while (mesa.next()){
				info[0]=mesa.getString(1);
				info[1]=mesa.getString(2);
				info[2]=mesa.getString(3);
				//mesa_electoral.add(mesa.getString(1));

			}
		}
		catch (Exception exc) {
			exc.printStackTrace();

		}

	}
	
	
	private static void getInfo2(String nombre) {

		try {
			Connection myConn = DriverManager.getConnection("jdbc:mariadb://votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com:3306/votacion?user=prueba&password=holahola");
			Statement myStmt = myConn.createStatement();

			ResultSet mesa = myStmt.executeQuery("SELECT sigla_partido, cedula_presidente, cedula_vicepresidente FROM Candidatos WHERE original=1 AND nombre_presidente='"+nombre+"'");
			
			while (mesa.next()){
				info2[0]=mesa.getString(1);
				info2[1]=mesa.getString(2);
				info2[2]=mesa.getString(3);

			}
		}
		catch (Exception exc) {
			exc.printStackTrace();
		}

	}

}
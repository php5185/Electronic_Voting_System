package visual;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Toolkit;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import java.awt.Color;

import javax.swing.border.TitledBorder;
import javax.swing.border.LineBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JPasswordField;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;




public class LoginConteo extends JDialog  {

	private final int PUERTO = 5556; //Puerto para la conexión
	private final String HOST = "192.168.40.2"; //Host para la conexión
	protected String mensajeServidor; //Mensajes entrantes (recibidos) en el servidor
	protected ServerSocket ss; //Socket del servidor
	protected Socket cs; //Socket del cliente
	protected DataOutputStream salidaServidor, salidaCliente; //Flujo de datos de salida
	protected DataInputStream leer, bufferDeEntrada;


	private final JPanel contentPanel = new JPanel();
	private JTextField usuario;
	private JPasswordField password;


	/**
	 * Launch the application.
	 */
	/*public static void main(String[] args) {
		try {
			LoginConteo dialog = new LoginConteo();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}*/

	/**
	 * Create the dialog.
	 */
	public LoginConteo() {
		setIconImage(Toolkit.getDefaultToolkit().getImage(LoginConteo.class.getResource("/Icon/copyjce.png")));
		setTitle("Ingresar ");
		setBounds(100, 100, 385, 260);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBackground(Color.WHITE);
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);

		JPanel panel = new JPanel();
		panel.setBackground(Color.WHITE);
		panel.setBorder(new LineBorder(new Color(204, 153, 0)));
		panel.setBounds(10, 11, 349, 166);
		contentPanel.add(panel);
		panel.setLayout(null);

		JLabel lblNewLabel = new JLabel("Usuario");
		lblNewLabel.setBounds(36, 76, 98, 22);
		panel.add(lblNewLabel);

		JLabel lblNewLabel_1 = new JLabel("Contrase\u00F1a");
		lblNewLabel_1.setBounds(36, 121, 98, 22);
		panel.add(lblNewLabel_1);

		usuario = new JTextField();
		usuario.setBounds(124, 76, 192, 22);
		panel.add(usuario);
		usuario.setColumns(10);

		password = new JPasswordField();
		password.setBounds(124, 121, 192, 22);
		panel.add(password);

		JLabel lblNewLabel_2 = new JLabel("Una Vez Terminado el Per\u00EDodo de Votaci\u00F3n Utilice ");
		lblNewLabel_2.setBounds(36, 11, 345, 14);
		panel.add(lblNewLabel_2);

		JLabel lblNewLabel_3 = new JLabel("el Usuario y la Contrase\u00F1a de su Mesa Electoral");
		lblNewLabel_3.setBounds(36, 25, 273, 14);
		panel.add(lblNewLabel_3);

		JLabel lblNewLabel_4 = new JLabel("para Iniciar el Conteo de Votos f\u00EDsiscos. ");
		lblNewLabel_4.setBounds(36, 40, 280, 14);
		panel.add(lblNewLabel_4);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setBackground(Color.WHITE);
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("Ingresar");
				okButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent arg0) {
						///llamar el socket
						String myPass=String.valueOf(password.getPassword());
						String ver="";
						if(!usuario.getText().equalsIgnoreCase("") && !myPass.equalsIgnoreCase("") && !myPass.equalsIgnoreCase("-1-1-1")){
							String envio = "0,1,"+usuario.getText()+","+myPass;
							try
							{
								//cs = new Socket(HOST, PUERTO);
								cs =new Socket();
								cs.connect(new InetSocketAddress(HOST, PUERTO),9000);
								
								//Flujo de datos hacia el servidor
								salidaServidor = new DataOutputStream(cs.getOutputStream());

								salidaServidor.writeUTF(envio);
								BufferedReader entrada = new BufferedReader(new InputStreamReader(cs.getInputStream()));

								while((mensajeServidor = entrada.readLine()) != null) //Mientras haya mensajes desde el cliente
								{
									//Se muestra por pantalla el mensaje recibido
									
									ver=mensajeServidor;
								}
								


								cs.close();//Fin de la conexión
								
								//orden: contrase;a, recibido, observado, reobs
								if (ver.equalsIgnoreCase("1,0,0,0")){//entra por 1ra vez
									dispose();
									
									Conteo conteo = new Conteo(usuario.getText(), ver, myPass);
									conteo.setModal(true);
									conteo.setLocationRelativeTo(null);						
									conteo.setVisible(true);
									conteo.setResizable(false);								
								}
								else if (ver.equalsIgnoreCase("1,1,1,0")){//entra por segunda vez
									
									//enviar un 1 en el constructor por si se quiere hacer doble revision
									dispose();
									Conteo conteo = new Conteo(usuario.getText(), ver, myPass);
									conteo.setModal(true);
									conteo.setLocationRelativeTo(null);						
									conteo.setVisible(true);
									conteo.setResizable(false);								
								}
								else{
									String[] pp=ver.split(",");
									
								
									if(pp[0].equalsIgnoreCase("0")){
										JOptionPane.showMessageDialog(null, "Usuario o contraseña incorrecta", null, JOptionPane.ERROR_MESSAGE, null);								
									}
									else {
										JOptionPane.showMessageDialog(null, "Esta mesa electoral ya fue computada", null, JOptionPane.ERROR_MESSAGE, null);

									}
								}
								

							}
							catch (Exception e){
								JOptionPane.showMessageDialog(null, "Fallo en la conexión con el servidor remoto", null, JOptionPane.ERROR_MESSAGE, null);
								
							}

							dispose();




							/*							
						dispose();
						Conteo conteo = new Conteo(usuario.getText());
						conteo.setModal(true);
						conteo.setLocationRelativeTo(null);						
						conteo.setVisible(true);
						conteo.setResizable(false);*/
						}
						else{
							//JOptionPane.showMessageDialog(null, "Solicitud realizada satisfectoriamente", null, JOptionPane.INFORMATION_MESSAGE, null);

							JOptionPane.showMessageDialog(null, "Usuario o contraseña incorrectaAA", null, JOptionPane.ERROR_MESSAGE, null);

						}
					}
				});
				okButton.setIcon(new ImageIcon(LoginConteo.class.getResource("/Icon/Ok_opt.png")));
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
			{
				JButton cancelButton = new JButton("Cancelar");
				cancelButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent arg0) {
						dispose();
					}
				});
				cancelButton.setActionCommand("Cancel");
				cancelButton.setIcon(new ImageIcon(LoginConteo.class.getResource("/Icon/close-btn.png")));
				buttonPane.add(cancelButton);
			}
		}
	}
}

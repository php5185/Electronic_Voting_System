package visual;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Toolkit;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.ImageIcon;
import javax.swing.JFormattedTextField;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.text.MaskFormatter;
import javax.swing.JTextField;
import javax.swing.JButton;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.PreparedStatement;

public class Phone extends JFrame {

	private JPanel contentPane;
	private JFormattedTextField textField;
	JButton btnNewButton;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Phone frame = new Phone();
					frame.setLocationRelativeTo(null);
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Phone() {
		/*setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);*/
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setBackground(Color.WHITE);
		setContentPane(contentPane);
		contentPane.setLayout(null);
		setIconImage(Toolkit.getDefaultToolkit().getImage(Phone.class.getResource("/Icon/copyjce.png")));
		
		JLabel lblProgramaParaGenerar = new JLabel("Programa Para Establecer el N\u00FAmero Telef\u00F3nico");
		lblProgramaParaGenerar.setBounds(72, 93, 308, 50);
		contentPane.add(lblProgramaParaGenerar);

		JLabel lblYContraseasDe = new JLabel("Del Sistema de Alertas en las Cabinas Electr\u00F3nicas");
		lblYContraseasDe.setBounds(67, 139, 316, 50);
		contentPane.add(lblYContraseasDe);

		JLabel lblJunta = new JLabel("");
		lblJunta.setBounds(37, 15, 366, 63);
		lblJunta.setIcon(new ImageIcon(Phone.class.getResource("/Icon/junta.png")));
		contentPane.add(lblJunta);
		
		//textField = new JFormattedTextField();
		try{
			MaskFormatter mas = new MaskFormatter("###-###-####");
			mas.setPlaceholderCharacter(' ');

			textField = new JFormattedTextField(mas);
		}catch (Exception e){}
		textField.addKeyListener(new KeyAdapter() {//revisar ese action listener
			@Override
			public void keyReleased(KeyEvent e) {
				/*if(!textField.getText().equalsIgnoreCase("###-###-####") && textField.getText().indexOf(" ")==-1){
					btnNewButton.setEnabled(true);
					System.out.println(11);
				}
				if(textField.getText().equalsIgnoreCase("")){
					System.out.println(00);
					
					btnNewButton.setEnabled(false);
				}*/
				if(textField.getText().indexOf(" ")==-1){
					btnNewButton.setEnabled(true);
				}
				else{
					btnNewButton.setEnabled(false);
				}
			}
		});
		textField.setBounds(98, 205, 96, 23);
		contentPane.add(textField);
		textField.setColumns(10);
		
		btnNewButton = new JButton("Aceptar");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String num=textField.getText();
				num =num.replace("-","");
				
				
				String SQL= "UPDATE NTP SET phone = ? WHERE control = 1";
				//int affectedrows = 0;
				try {
					Connection myConn = DriverManager.getConnection("jdbc:mariadb://votacion.chdzg63tyr59.us-east-1.rds.amazonaws.com:3306/votacion?user=prueba&password=holahola");
					//Statement myStmt = myConn.createStatement();
					//ResultSet mesa = myStmt.executeQuery("SELECT id_col_elec, AES_DECRYPT(pass, UNHEX(SHA2('elecciones2020',512))) FROM Colegio_electoral");//puedo encriptar aux

					PreparedStatement pstmt = myConn.prepareStatement(SQL);
					pstmt.setString(1, num);//"2018-12-12 11:11:11");
					
					
					
					pstmt.executeUpdate();
					
				}
				catch (Exception exc) {
					exc.printStackTrace();
				}
				
				JOptionPane.showMessageDialog(null, "Número Registrado Satisfactoriamente", null, JOptionPane.INFORMATION_MESSAGE, null);
				textField.setText("");
				btnNewButton.setEnabled(false);
				
			}
		});
		btnNewButton.setEnabled(false);
		btnNewButton.setBounds(234, 204, 89, 23);
		contentPane.add(btnNewButton);
	}
}

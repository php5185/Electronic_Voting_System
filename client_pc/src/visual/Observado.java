package visual;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Toolkit;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import java.awt.Color;

import javax.swing.border.TitledBorder;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.SwingConstants;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Observado extends JDialog {

	private final JPanel contentPanel = new JPanel();
	private JTextField user;
	private JPasswordField pass;
	private JTextField siglaPart;

	/**
	 * Launch the application.
	 */
	/*public static void main(String[] args) {
		try {
			String mesa="ll";
			Observado dialog = new Observado(mesa,mesa);
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}*/

	/**
	 * Create the dialog.
	 */
	public Observado(final String mesa, final String myPass) {
		setIconImage(Toolkit.getDefaultToolkit().getImage(Observado.class.getResource("/Icon/copyjce.png")));
		setTitle("Voto Observado");
		setBounds(100, 100, 450, 300);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBackground(Color.WHITE);
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBackground(Color.WHITE);
		panel.setBorder(new TitledBorder(null, "Credenciales", TitledBorder.LEADING, TitledBorder.TOP, null, null));
		panel.setBounds(10, 11, 414, 100);
		contentPanel.add(panel);
		panel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Usuario:");
		lblNewLabel.setBounds(26, 23, 96, 21);
		panel.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("Contrase\u00F1a:");
		lblNewLabel_1.setBounds(26, 59, 81, 22);
		panel.add(lblNewLabel_1);
		
		user = new JTextField();
		user.setEditable(false);
		user.setEnabled(false);
		user.setBounds(136, 23, 200, 21);
		user.setText(mesa);
		panel.add(user);
		user.setColumns(10);
		
		pass = new JPasswordField();
		pass.setBounds(136, 59, 200, 21);
		panel.add(pass);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBackground(Color.WHITE);
		panel_1.setBorder(new TitledBorder(null, "Voto Observado", TitledBorder.LEADING, TitledBorder.TOP, null, null));
		panel_1.setBounds(10, 122, 414, 100);
		contentPanel.add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblNewLabel_2 = new JLabel("Sigla Partido:");
		lblNewLabel_2.setBounds(26, 29, 96, 22);
		panel_1.add(lblNewLabel_2);
		
		siglaPart = new JTextField();
		siglaPart.setBounds(136, 29, 200, 21);
		panel_1.add(siglaPart);
		siglaPart.setColumns(10);
		
		JLabel label = new JLabel("*");
		label.setForeground(Color.RED);
		label.setBounds(105, 29, 15, 14);
		panel_1.add(label);
		
		JLabel lblNewLabel_3 = new JLabel("*Escribir Igual a Como se Encuentra en el Voto Impreso");
		lblNewLabel_3.setHorizontalAlignment(SwingConstants.RIGHT);
		lblNewLabel_3.setForeground(Color.RED);
		lblNewLabel_3.setBounds(56, 68, 348, 21);
		panel_1.add(lblNewLabel_3);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("Aceptar");
				okButton.addActionListener(new ActionListener() {
					
					public void actionPerformed(ActionEvent arg0) {
						String contra=String.valueOf(pass.getPassword());
						if(!siglaPart.getText().equalsIgnoreCase("") && !contra.equalsIgnoreCase("") && !contra.equalsIgnoreCase("-1-1-1")){
							
							if (myPass.equals(contra)){
								//siglaPart.getText()
								int veri =Conteo.count(siglaPart.getText(), "Observado");
								if (veri==1){
									//mensaje satisfactorio
									JOptionPane.showMessageDialog(null, "Voto Observado Registrado Satisfactoriamente", null, JOptionPane.INFORMATION_MESSAGE, null);
									dispose();
								}
								else{
									JOptionPane.showMessageDialog(null, "Sigla del Partido Incorrecta", null, JOptionPane.ERROR_MESSAGE, null);
								}					
								
							}
							else{
								JOptionPane.showMessageDialog(null, "Contraseña Incorrecta", null, JOptionPane.ERROR_MESSAGE, null);
								
							}
							
						}
						else{
							JOptionPane.showMessageDialog(null, "Contraseña o Sigla Partido Incorrecta", null, JOptionPane.ERROR_MESSAGE, null);
						}
						
						
					}
				});
				okButton.setActionCommand("OK");
				okButton.setIcon(new ImageIcon(Observado.class.getResource("/Icon/Ok_opt.png")));
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
				cancelButton.setIcon(new ImageIcon(Observado.class.getResource("/Icon/close-btn.png")));
				buttonPane.add(cancelButton);
			}
		}
	}
}

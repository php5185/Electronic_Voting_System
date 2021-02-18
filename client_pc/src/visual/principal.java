package visual;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.SystemColor;
import java.awt.Toolkit;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JSeparator;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;

//import visualDialog.Login;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;





public class principal extends JFrame {
	private Dimension dim;
	private JPanel panel;

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					principal frame = new principal();
					frame.setLocation(-7, 0);//poner eso con Conteo
					//frame.setLocationRelativeTo(null);
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
	public principal() {
		setForeground(new Color(204, 153, 0));
		setFont(new Font("Dialog", Font.BOLD, 12));
		setBackground(SystemColor.windowText);
		setResizable(false);
		setTitle("JUNTA CENTRAL ELECTORAL");
		setIconImage(Toolkit.getDefaultToolkit().getImage(principal.class.getResource("/Icon/copyjce.png")));
		
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBackground(Color.WHITE);
		contentPane.setForeground(Color.WHITE);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		/*panel = new JPanel();
		panel.setForeground(Color.WHITE);
		panel.setBackground(Color.WHITE);
		panel.setBounds(0, 0, 1362, 646);
		contentPane.add(panel);
		panel.setLayout(null);*/
		
		JLabel label = new JLabel("");label.setBackground(new Color(10,20,15,100));
		label.setIcon(new ImageIcon(principal.class.getResource("/Icon/logoPrinc.png")));
		label.setBounds(313, 46, 740, 562);
		contentPane.add(label);
		
		JSeparator separator_3 = new JSeparator();
		separator_3.setBackground(new Color(204, 153, 0));
		separator_3.setBounds(0, 0, 1360, 16);
		contentPane.add(separator_3);

		
		setBounds(100, 100, 548, 360);
		dim = super.getToolkit().getScreenSize(); 
		super.setSize(dim.width+12, dim.height-33);
		
		JMenuBar menuBar = new JMenuBar();
		menuBar.setBackground(Color.WHITE);
		setJMenuBar(menuBar);

		JMenu menu = new JMenu(" ");
		menu.setBackground(Color.WHITE);
		menu.setEnabled(false);
		menuBar.add(menu);

		JMenu registroVoto = new JMenu("COMPUTAR MESA    ");
		registroVoto.setFont(new Font("Segoe UI", Font.BOLD, 12));
		registroVoto.setIcon(new ImageIcon(principal.class.getResource("/Icon/asignar.png")));
		//mnSolicitarTrabajo.setIcon(new ImageIcon(Principal.class.getResource("/Icon/d.png")));
		//mntmSolicitar_1.setIcon(new ImageIcon(Principal.class.getResource("/Icon/regOfer.png")));
		menuBar.add(registroVoto);
		
		JMenuItem mntmRegistro = new JMenuItem("CONTEO DE VOTOS");
		mntmRegistro.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				LoginConteo reg = new LoginConteo();
				reg.setModal(true);
				reg.setLocationRelativeTo(null);
				reg.setVisible(true);
				reg.setResizable(false);
				
			}
		});
		mntmRegistro.setFont(new Font("Segoe UI", Font.BOLD, 12));
		mntmRegistro.setBackground(Color.WHITE);
		mntmRegistro.setIcon(new ImageIcon(principal.class.getResource("/Icon/aa_opt (1).png")));
		registroVoto.add(mntmRegistro);
	}
}

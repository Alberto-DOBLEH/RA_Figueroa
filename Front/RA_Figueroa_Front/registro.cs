using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;

namespace RA_Figueroa_Front
{
    public partial class registro : Form
    {
        private Form1 formulario_principal;
        public registro(Form1 principal)
        {
            InitializeComponent();
            formulario_principal = principal;
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            Usuario? user = new Usuario();

            string nombre_user = nombre.Text;
            string edad_user = edad.Text;
            string username_user = usuario.Text;
            string contraseña_user = contraseña.Text;
            string c_contraseña_user = c_contraseña.Text;
            string ciudad_user = ciudad.Text;

            if (contraseña_user == c_contraseña_user)
            {
                Usuario? usuariocomprobacion = await UsuarioService.ConsultarUsuarioAsync(username_user);

                if (usuariocomprobacion == null)
                {
                    user.Nombre = nombre_user;
                    user.Edad = int.Parse(edad_user);
                    user.Username = username_user;
                    user.Password = contraseña_user;
                    user.Ciudad = ciudad_user;

                    // Llamar al método para crear el usuario
                    UsuarioService usuarioService = new UsuarioService();
                    bool resultado = await usuarioService.CrearUsuarioAsync(user);

                    if (resultado)
                    {
                        MessageBox.Show("Usuario creado con éxito.");
                        this.Close(); // Cierra el formulario de registro
                        formulario_principal.Show(); // Muestra el formulario principal
                    }
                    else
                    {
                        MessageBox.Show("Hubo un error al crear el usuario. Por favor, intenta de nuevo.");
                    }
                }
                else
                {
                    MessageBox.Show("Ese Username ya esta en uso");
                }
            }
            else
            {
                MessageBox.Show("Las contraseñas no coinciden");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            formulario_principal.Show(); // Mostrar el formulario principal
            this.Close(); // Cerrar el formulario actual
        }
    }
}

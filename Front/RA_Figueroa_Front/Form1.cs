namespace RA_Figueroa_Front
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private async void button1_Click(object sender, EventArgs e)
        {
            pagina_principal form_principal = new pagina_principal();
            try
            {
                string contra = pass.Text;
                string username = user.Text; // Username del usuario a consultar

                Usuario? usuario = await UsuarioService.ConsultarUsuarioAsync(username);

                if (usuario != null)
                {
                    if (usuario.Password == contra)
                    {
                        form_principal.Show();
                        this.Hide();
                    }
                    else
                    {
                        MessageBox.Show("La contraseña es incorrecta");
                    }
                }
                else
                {
                    MessageBox.Show("No se encontró el usuario.");
                }
            }
            catch (Exception ex)
            {
                // Manejo de errores
                MessageBox.Show($"Ocurrió un error: {ex.Message}");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            registro form2 = new registro(this); // Pasar la referencia del formulario principal
            form2.Show();
            this.Hide(); // Ocultar el formulario principal
        }
    }
}

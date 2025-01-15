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
            pagina_principal pagina_Principal = new pagina_principal();
            try
            {
                string password = pass.Text;
                string username = user.Text; // Username del usuario a consultar

                Usuario? usuario = await UsuarioService.ConsultarUsuarioAsync(username);

                if (usuario != null)
                {
                    if(usuario.Password == password)
                    {
                        pagina_Principal.Show();
                        this.Close();
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

    }
}

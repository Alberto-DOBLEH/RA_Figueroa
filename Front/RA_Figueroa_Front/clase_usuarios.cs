using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace RA_Figueroa_Front
{
    public class Usuario
    {
        public int IdUsuario { get; set; }
        public string? Nombre { get; set; }
        public int Edad { get; set; }
        public string? Username { get; set; }
        public string? Password { get; set; }
        public string? Ciudad { get; set; }
    }

    public class UsuarioService
    {
        private static readonly HttpClient client = new HttpClient();
        private const string BaseUrl = "http://localhost:8000/api/";

        private static string BuildUrl(string endpoint) => $"{BaseUrl}{endpoint}";

        public async Task<bool> CrearUsuarioAsync(Usuario usuario)
        {
            try
            {
                string url = BuildUrl("agregarusuarios");

                var datos = new
                {
                    nombre = usuario.Nombre,
                    edad = usuario.Edad,
                    usuario = usuario.Username,
                    contraseña = usuario.Password, 
                    ciudad = usuario.Ciudad
                };

                string jsonData = JsonSerializer.Serialize(datos);

                StringContent content = new StringContent(jsonData, Encoding.UTF8, "application/json");
                HttpResponseMessage response = await client.PostAsync(url, content);

                if (response.IsSuccessStatusCode)
                {
                    Console.WriteLine("Usuario añadido con éxito.");
                    return true;
                }
                else
                {
                    Console.WriteLine($"Error al crear el usuario: {response.StatusCode}");
                    return false;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error al crear el usuario: {ex.Message}");
                return false;
            }
        }

        public static async Task<Usuario?> ConsultarUsuarioAsync(string username)
        {
            try
            {
                // Construir la URL con el username
                string url = BuildUrl($"informacionusername/{username}");

                // Enviar la solicitud GET
                HttpResponseMessage response = await client.GetAsync(url);

                // Verificar si la solicitud fue exitosa
                if (response.IsSuccessStatusCode)
                {
                    // Leer el contenido de la respuesta como JSON
                    string responseContent = await response.Content.ReadAsStringAsync();

                    // Deserializar el JSON a un objeto Usuario
                    Usuario? usuario = JsonSerializer.Deserialize<Usuario>(responseContent);

                    Console.WriteLine("Usuario consultado con éxito.");
                    return usuario;
                }
                else
                {
                    Console.WriteLine($"Error al consultar el usuario: {response.StatusCode}");
                    return null;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error al consultar el usuario: {ex.Message}");
                return null;
            }
        }


        // Métodos adicionales como Eliminar, Consultar, y Editar irían aquí
    }
}

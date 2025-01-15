namespace RA_Figueroa_Front
{
    partial class registro
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            nombre = new TextBox();
            usuario = new TextBox();
            c_contraseña = new TextBox();
            edad = new TextBox();
            contraseña = new TextBox();
            ciudad = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            label6 = new Label();
            label7 = new Label();
            button1 = new Button();
            button2 = new Button();
            SuspendLayout();
            // 
            // nombre
            // 
            nombre.Location = new Point(347, 85);
            nombre.Name = "nombre";
            nombre.Size = new Size(100, 23);
            nombre.TabIndex = 0;
            // 
            // usuario
            // 
            usuario.Location = new Point(347, 175);
            usuario.Name = "usuario";
            usuario.Size = new Size(100, 23);
            usuario.TabIndex = 1;
            // 
            // c_contraseña
            // 
            c_contraseña.Location = new Point(347, 263);
            c_contraseña.Name = "c_contraseña";
            c_contraseña.Size = new Size(100, 23);
            c_contraseña.TabIndex = 2;
            // 
            // edad
            // 
            edad.Location = new Point(347, 131);
            edad.Name = "edad";
            edad.Size = new Size(100, 23);
            edad.TabIndex = 3;
            // 
            // contraseña
            // 
            contraseña.Location = new Point(347, 219);
            contraseña.Name = "contraseña";
            contraseña.Size = new Size(100, 23);
            contraseña.TabIndex = 4;
            // 
            // ciudad
            // 
            ciudad.Location = new Point(347, 307);
            ciudad.Name = "ciudad";
            ciudad.Size = new Size(100, 23);
            ciudad.TabIndex = 5;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Verdana", 14.25F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label1.Location = new Point(318, 31);
            label1.Name = "label1";
            label1.Size = new Size(141, 23);
            label1.TabIndex = 6;
            label1.Text = "Registrarse:";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(366, 67);
            label2.Name = "label2";
            label2.Size = new Size(54, 15);
            label2.TabIndex = 7;
            label2.Text = "Nombre:";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(378, 113);
            label3.Name = "label3";
            label3.Size = new Size(36, 15);
            label3.TabIndex = 8;
            label3.Text = "Edad:";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(372, 157);
            label4.Name = "label4";
            label4.Size = new Size(63, 15);
            label4.TabIndex = 9;
            label4.Text = "Username:";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(362, 201);
            label5.Name = "label5";
            label5.Size = new Size(70, 15);
            label5.TabIndex = 10;
            label5.Text = "Contraseña:";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(334, 245);
            label6.Name = "label6";
            label6.Size = new Size(125, 15);
            label6.TabIndex = 11;
            label6.Text = "Confirmar contraseña:";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(372, 289);
            label7.Name = "label7";
            label7.Size = new Size(48, 15);
            label7.TabIndex = 12;
            label7.Text = "Ciudad:";
            // 
            // button1
            // 
            button1.Location = new Point(347, 358);
            button1.Name = "button1";
            button1.Size = new Size(100, 23);
            button1.TabIndex = 13;
            button1.Text = "Registrarse";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Location = new Point(12, 509);
            button2.Name = "button2";
            button2.Size = new Size(75, 23);
            button2.TabIndex = 14;
            button2.Text = "Regresar";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // registro
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 544);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(label7);
            Controls.Add(label6);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(ciudad);
            Controls.Add(contraseña);
            Controls.Add(edad);
            Controls.Add(c_contraseña);
            Controls.Add(usuario);
            Controls.Add(nombre);
            Name = "registro";
            Text = "registro";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox nombre;
        private TextBox usuario;
        private TextBox c_contraseña;
        private TextBox edad;
        private TextBox contraseña;
        private TextBox ciudad;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private Label label6;
        private Label label7;
        private Button button1;
        private Button button2;
    }
}
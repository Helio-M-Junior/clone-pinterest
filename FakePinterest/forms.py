# Forms do site FakePinterest
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from FakePinterest.models import Usuario

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    lembrar = BooleanField("Lembrar de mim")
    submit = SubmitField("Login")

   
class CadastroForm(FlaskForm):
    nome = StringField("Nome de Usuario", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=8)])
    confirmar_senha = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("senha")])
    submit = SubmitField("Cadastrar")
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email ja cadastrado. Faça login para continuar.")
        
     
class FotoForm(FlaskForm):
    imagem = FileField("Escolha uma imagem", validators=[DataRequired()])
    submit = SubmitField("Postar")  
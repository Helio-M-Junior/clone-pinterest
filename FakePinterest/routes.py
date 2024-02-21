import os
from werkzeug.utils import secure_filename
from FakePinterest import app, database, bcrypt
from FakePinterest.forms import CadastroForm, LoginForm, FotoForm
from FakePinterest.models import Usuario, Foto
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
            login_user(usuario, remember=form.lembrar.data)
            return redirect(url_for('perfil', id_usuario=usuario.id))
        
    return render_template('login.html', form=form)

@app.route('/cadastro', methods=['GET', 'POST'])
def criar_conta():
    form = CadastroForm()
    if form.validate_on_submit():
        senha = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        usuario = Usuario(nome=form.nome.data, email=form.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit()
        return redirect(url_for('login'))
    return render_template('criar_conta.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()
    return render_template('feed.html', fotos=fotos)

@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):
    if int(id_usuario) is int(current_user.id):
        form = FotoForm()
        if form.validate_on_submit():
            arquivo = form.imagem.data
            nome_arquivo = secure_filename(arquivo.filename)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], nome_arquivo)
            arquivo.save(path)
            foto = Foto(imagem=arquivo.filename, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        
        return render_template('perfil.html', usuario=current_user, form=form)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)
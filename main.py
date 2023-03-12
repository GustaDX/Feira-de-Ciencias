from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    global verifica
    if (re.search(regex, email)):
        verifica = True

    else:
        verifica = False


def conecta():
    global conexao, Cursor
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        passwd='')
    print('conectado')
    Cursor = conexao.cursor()


def desconecta():
    conexao.close()


def verifica_cadastro():
    Nomeg = Nome.get()
    Telefoneg = Telefone.get()
    Emailg = Email.get()
    Data_Nascimentog = Data_Nascimento.get()

    numero_Nomeg = len(Nomeg)
    vca = True
    for i in range(0, numero_Nomeg):
        if Nomeg[i] == '1':
            vca = False
        elif Nomeg[i] == '2':
            vca = False
        elif Nomeg[i] == '3':
            vca = False
        elif Nomeg[i] == '4':
            vca = False
        elif Nomeg[i] == '5':
            vca = False
        elif Nomeg[i] == '6':
            vca = False
        elif Nomeg[i] == '7':
            vca = False
        elif Nomeg[i] == '8':
            vca = False
        elif Nomeg[i] == '9':
            vca = False
        elif Nomeg[i] == '0':
            vca = False

    numero_Telefoneg = len(Telefoneg)
    vct = False
    for i in range(0, numero_Telefoneg):
        if Telefoneg[i] == '1':
            vct = True
        elif Telefoneg[i] == '2':
            vct = True
        elif Telefoneg[i] == '3':
            vct = True
        elif Telefoneg[i] == '4':
            vct = True
        elif Telefoneg[i] == '5':
            vct = True
        elif Telefoneg[i] == '6':
            vct = True
        elif Telefoneg[i] == '7':
            vct = True
        elif Telefoneg[i] == '8':
            vct = True
        elif Telefoneg[i] == '9':
            vct = True
        elif Telefoneg[i] == '0':
            vct = True

    numero_data = len(Data_Nascimentog)
    vcd = False

    for i in range(0, numero_data):
        if Data_Nascimentog[i] == '1':
            vcd = True
        elif Data_Nascimentog[i] == '2':
            vcd = True
        elif Data_Nascimentog[i] == '3':
            vcd = True
        elif Data_Nascimentog[i] == '4':
            vcd = True
        elif Data_Nascimentog[i] == '5':
            vcd = True
        elif Data_Nascimentog[i] == '6':
            vcd = True
        elif Data_Nascimentog[i] == '7':
            vcd = True
        elif Data_Nascimentog[i] == '8':
            vcd = True
        elif Data_Nascimentog[i] == '9':
            vcd = True
        elif Data_Nascimentog[i] == '0':
            vcd = True

    if vca == True and len(Nomeg) <= 30 and len(Nomeg) >= 2:
        if vct == True and len(Telefoneg) == 11:
            check(Emailg)
            if verifica == True:
                if vcd == True and len(Data_Nascimentog) == 10:
                    conecta()
                    Cursor.execute('USE Hospital;')
                    conexao.commit()
                    Cursor.execute(
                        f'INSERT INTO pacientes(Nome, Telefone, Email, Data_Nascimento) VALUES ("{Nomeg}", "{Telefoneg}", "{Emailg}", "{Data_Nascimentog}");')
                    conexao.commit()
                    desconecta()
                    Concluido()

                else:
                    messagebox.showinfo('Erro de Cadastro', \
                                        f'''
                                            Data Invalido
                                            Formato Correto:
                                            00/00/0000
                                            ''')
            else:
                messagebox.showinfo('Erro de Cadastro', \
                                    f'''
                                    Email Invalido
                                    Verifique seu email
                                    ''')
        else:
            messagebox.showinfo('Erro de Cadastro', \
                                f'''
                                Telefone Invalido
                                Formato Correto:
                                00000000000
                                ''')
    else:
        messagebox.showinfo('Erro de Cadastro', \
                            f'''
                            Nome Invalido
                            Verifique o Nome informado
                            pode counter no maximo 30 caracteres
                            ''')


def Concluido():
    try:
        imagem.destroy()
        Nome.destroy()
        Email.destroy()
        Telefone.destroy()
        Data_Nascimento.destroy()

    finally:
        conecta()
        Cursor.execute('USE Hospital;')
        conexao.commit()
        Cursor.execute(f'UPDATE senha SET status = "finalizado" WHERE Senha = {senha};')
        conexao.commit()
        desconecta()
        imagemc = Label(tela, image=fotoh, border=0)
        imagemc.place(x=0, y=0)
        Conclui = Button(tela, text='Confirmar', font='arial, 23', width=10, border=0, bg='#eaf6ff',
                         activebackground='#eaf6ff', fg='#038acd', activeforeground='#038acd', command=Cadastro)
        Conclui.place(x=lado / 2.32, y=cima / 1.803)


def Cadastro():
    global imagem, Nome, Email, Telefone, Data_Nascimento, Cadastrar, senha, verifico

    conecta()
    Cursor.execute('USE hospital;')
    conexao.commit()
    Cursor.execute(f"SELECT * FROM senha WHERE status = 'atendimento'")
    conexao.commit()
    dados = Cursor.fetchone()
    desconecta()

    imagem = Label(tela, image=fotoc, border=0)
    imagem.place(x=0, y=0)

    Nome = Entry(tela, border=0, fg='#eaf6ff', font='arial, 15', bg='#57daff')
    Nome.place(x=lado / 12, y=cima / 3.33, relwidth=lado / 2520, relheight=cima / 14000)

    Telefone = Entry(tela, border=0, fg='#eaf6ff', font='arial, 15', bg='#57daff')
    Telefone.place(x=lado / 12, y=cima / 2.36, relwidth=lado / 2520, relheight=cima / 14000)

    Email = Entry(tela, border=0, fg='#eaf6ff', font='arial, 15', bg='#57daff')
    Email.place(x=lado / 12, y=cima / 1.832, relwidth=lado / 2520, relheight=cima / 14000)

    Data_Nascimento = Entry(tela, border=0, fg='#eaf6ff', font='arial, 15', bg='#57daff')
    Data_Nascimento.place(x=lado / 12, y=cima / 1.498, relwidth=lado / 2520, relheight=cima / 14000)

    Cadastrar = Button(tela, text='Cadastrar', font='arial, 23', width=10, border=0, bg='#038acd',
                       activebackground='#038acd', fg='#eaf6ff', activeforeground='#eaf6ff', command=verifica_cadastro)
    Cadastrar.place(x=lado / 3.8, y=cima / 1.25)
    verifico = False
    v = False
    while v == False:
        if verifico == True:
            v = True

        if Cursor.rowcount == 0:
            try:
                conecta()
                Cursor.execute('USE hospital;')
                conexao.commit()
                Cursor.execute(f"SELECT * FROM senha WHERE status = 'atendimento'")
                conexao.commit()
                dados = Cursor.fetchone()
            
            finally:
                try:
                    desconecta()
                
                finally:
                    tela.update()

        elif Cursor.rowcount != 0:
            senha = dados[0]

            Senha_texto = Label(tela, text=f'{dados[0]}', border=0, font='arial, 60', bg='#57daff', fg='#eaf6ff',
                                        padx=lado / 100, width=int(lado / 151))
            Senha_texto.place(x=lado / 1.51, y=cima / 2.95)

            nome_texto = Label(tela, text=f'{dados[1]}', border=0, font='arial, 20', bg='#57daff', fg='#eaf6ff',
                                    padx=lado / 100, width=int(lado / 50))
            nome_texto.place(x=lado / 1.51, y=cima / 1.71)
            v = True

def closing():
    global verifico
    verifico = True
    tela.destroy()
        
# Definições de tela

tela = Tk()
lado, cima = (tela.winfo_screenwidth()), (tela.winfo_screenheight())
tela.geometry('%dx%d+0+0' % (lado, cima - cima / 20))
tela.config(background='#363636', )
tela.title('SESI Med')
tela.iconbitmap('icon.ico')
tela.protocol("WM_DELETE_WINDOW", closing)
image = Image.open('Cadastro.png')
resize_image = image.resize((lado, int(cima - cima / 20)))
fotoc = ImageTk.PhotoImage(resize_image)
image = Image.open('Concluido.png')
resize_image = image.resize((lado, int(cima - cima / 20)))
fotoh = ImageTk.PhotoImage(resize_image)

# banco
conecta()
Cursor.execute('CREATE DATABASE IF NOT EXISTS Hospital;')
conexao.commit()
print('Conecta')
Cursor.execute('USE Hospital;')
conexao.commit()
Cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes(
    Id_Paciente int PRIMARY KEY AUTO_INCREMENT,
    Nome varchar(30),
    telefone varchar(11),
    Email varchar(40),
    Data_Nascimento varchar(10));''')
conexao.commit()
print('Comando executado')
desconecta()
Cadastro()

tela.mainloop()

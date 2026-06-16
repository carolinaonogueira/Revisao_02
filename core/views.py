from django.shortcuts import render, redirect
from datetime import date

dados_usuario = {}

def inicio(request):
    return render(request, 'inicio.html')


def cadastro(request):
    erros = []

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')

        if len(nome) < 3:
            erros.append("O nome deve possuir pelo menos 3 caracteres.")

        if '@' not in email:
            erros.append("O e-mail deve conter o símbolo @.")

        nascimento = date.fromisoformat(data_nascimento)
        hoje = date.today()

        idade = hoje.year - nascimento.year

        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1

        if idade < 18:
            erros.append("O usuário deve ter 18 anos ou mais.")

        if erros:
            return render(request, 'cadastro.html', {'erros': erros})

        dados_usuario['nome'] = nome
        dados_usuario['email'] = email
        dados_usuario['idade'] = idade

        return redirect('sucesso')

    return render(request, 'cadastro.html')


def sucesso(request):
    return render(request, 'sucesso.html', {'dados': dados_usuario})

var objetoJs = {
    agencia:'5678-7',
    conta: '38438-4',
    tipo: 'física',
    nome: 'Mario josuedison de gausez',
    cpf: '43442194851'
};

var textoJson = JSON.stringify(objetoJs);

localStorage.setItem('stringJSON', textoJson)
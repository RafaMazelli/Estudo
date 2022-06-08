/*var cores = [
    {id: 1, nome: 'amarelo'},
    {id: 3, nome: 'azul'},
    {id: 4, nome: 'marrom'},
    {id: 5, nome: 'laranja'},
    {id: 6, nome: 'rosa'}
];

var nomeCores = [];

cores.forEach(function(cor){
    nomeCores.push(cor.nome);
});
console.log(nomeCores);*/
var cores = [
    {id: 1, nome: 'amarelo1'},
    {id: 3, nome: 'azul2'},
    {id: 4, nome: 'marrom3'},
    {id: 5, nome: 'laranja4'},
    {id: 6, nome: 'rosa5'}
];
var nomeCores = [];

const corNome = cores.map(cor => cor.nome);

console.log(corNome);

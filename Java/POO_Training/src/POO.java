public class POO {
    public static void main(String[] args) {
        //---------------Instanciando Objetos----------------------------
        User[] users = new User[10]; // Instanciando um array de Objetos

        for(int i=0; i < users.length; i++){ // Percorrendo o array  e definindo as propriedades concatenando um nome qualquer com o indice definido na variavel i
            User actual = new User();
            actual.setFirstName("Individois" + i);
            actual.setLastName("Sobrenorme" + i);
            actual.setLogged(false);
            actual.setPassword(123 + i);
            users[i] = actual;
        }



        //---------------- Saída na Tela-----------------------------

        for (int i = 0; i < 10; i++){ //percorrendo o array e imprimindo na tela seus objetos
            System.out.println("Nome: " + users[i].getFirstName() + " " + users[i].getLastName() + " // senha: " + users[i].getPassword() + " // " + "logado: " + "\u001B[31m" + users[i].getLogged()+ "\u001B[0m"); // 1 Objeto instanciado
            }

        
        users[3].setLogged(true); // Mudando o estado do Objeto 1(user[3])

        System.out.println("-------------------------------------------------------------------");
        
        for (int i = 0; i < 10; i++){ //reimprimindo os objetos do array para verificar a modificação feita do atributo islogged
            System.out.println("Nome: " + users[i].getFirstName() + " " + users[i].getLastName() + " // senha: " + users[i].getPassword() + " // " + "logado: " + users[i].getLogged()); // reimprimindo para verificar na saida a mudanca da propriedade atraves do Setter
            }

    }
}

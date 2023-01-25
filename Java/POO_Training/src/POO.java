public class POO {
    public static void main(String[] args) {
        //---------------Instanciando Objetos----------------------------
        User[] users = new User[]{// Instanciando um array de Objetos

            new User(false, "fulano1", "da silvano", 1234),
            new User(false, "sicrano1", "da silcrano", 1234),
            new User(false, "fulano2", "da silvano2", 1234)
        }; 

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

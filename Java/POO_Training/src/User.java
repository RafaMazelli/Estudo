public class User {
    
    public boolean isLogged; // definindo propriedade do molde do objeto
    public String firstName; // definindo propriedade do molde do objeto
    public String lastName; // definindo propriedade do molde do objeto
    public int password; // definindo propriedade do molde do objeto

    public void setLogged(boolean logged){ // definindo um metodo
        isLogged = logged;
    }

    public String fullName(){ //definindo um metodo com retorno
        return firstName + " " + lastName;
    }
    
}

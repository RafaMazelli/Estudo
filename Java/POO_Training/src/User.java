public class User {
    
    private boolean isLogged; // definindo propriedade do molde do objeto
    private String firstName; // definindo propriedade do molde do objeto
    private String lastName; // definindo propriedade do molde do objeto
    private int password; // definindo propriedade do molde do objeto

    //-----------------------SETTERS------------------------------------
    public void setLogged(boolean logged){ // definindo metodo setter
        isLogged = logged;
    }
    public void setFirstName(String firstName){
        this.firstName = firstName;
    }
    public void setLastName(String lastName){
        this.lastName = lastName;
    }
    public void setPassword(int password){
        this.password = password;
    }

    //-----------------------GETTERS------------------------------------

    public Boolean getLogged(){//definindo Getters. A substituição do void pelo tipo específico mostra que alem de um retorno a função tem um retorno especifico
        return isLogged;
    }
    public String getFirstName(){
        return firstName;
    }
    public String getLastName(){
        return lastName;
    }
    public int getPassword(){
        return password;
    }
    public String getFullName(){ 
        return firstName + " " + lastName;
    }
    
}

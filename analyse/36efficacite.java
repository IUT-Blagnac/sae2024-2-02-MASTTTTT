package iut.sae.algo;

// 36efficacite.java
// complexite : 
// RLE = O(n) car boucle for
// RLErec = O(2nk) car au pire chaine avec que caractère diff donc double de taille * nb iteration
// unRLE = O(9n/2) car limit de la 2eme boucle à 9 / 2 car parcours 2 en 2
// unRLErec = O((9n/2)*k)

// test10() 5-8ms
// test30() +=10ms
// index Out Of Range sur test40; 

public class Algo{
    public static String RLE(String in){

        if (in == null || in.isEmpty()){
            return "";
        }
    
        StringBuilder resultat = new StringBuilder();
        char nouv_char = in.charAt(0);
        short compteur = 1;
    
        for (int i = 1; i < in.length(); i++) {
            if (nouv_char != in.charAt(i) || compteur == 9) {
                resultat.append(compteur).append(nouv_char);
                nouv_char = in.charAt(i);
                compteur = 1;
            } else {
                compteur++;
            }
        }

        resultat.append(compteur).append(nouv_char);
        return resultat.toString();
    }

    public static String RLE(String in, int iteration) throws AlgoException{
        String resultat = RLE(in);
        for (short i = 0; i < iteration-1; i++){
            resultat = RLE(resultat);
        }
        return resultat;
    }

    public static String unRLE(String in) throws AlgoException{

        if (in == null || in.length() == 0){
            return "";
        }

        StringBuilder resultat = new StringBuilder();
        short nb_ite = (short)(in.length());
        
        for (short i = 0; i < nb_ite; i+=2){
            short jMax = (short) Character.getNumericValue(in.charAt(i));
            for (short j = 0; j < jMax ;j++){
                resultat.append(in.charAt(i+1));
            }
        }

        return resultat.toString();
    }

    public static String unRLE(String in, int iteration) throws AlgoException{
        String resultat = unRLE(in);
        for (short i = 0; i < iteration-1; i++){
            resultat = unRLE(resultat);
        }
        return resultat;
    }

}
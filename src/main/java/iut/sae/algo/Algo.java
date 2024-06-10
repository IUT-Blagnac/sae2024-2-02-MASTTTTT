package iut.sae.algo;


public class Algo{
    public static String RLE(String chaine){
        // Utilisation d'un StringBuilder (pour améliorer le temps d'execution) car l'object String ne concatène pas simplement plusieurs chaine.
        // Initialisation d'un compteur et d'un indice
         StringBuilder dBuilder = new StringBuilder();
        int cptChar;
        int i = 0;

        while(i < chaine.length()){
            // Compteur à 1 pour le caractère courant
            cptChar = 1;

            // Tant que le suivant est égale au courant et qu'il existe dans la chaine, et que le compteur ne dépasse pas 9...
            while (i+cptChar < chaine.length() && chaine.charAt(i) == chaine.charAt(i+cptChar) && cptChar < 9){
                //...on incrémente le compteur 
                cptChar++;
            }
            // On ajoute au builder le compteur et le caractère
            dBuilder.append("" + cptChar + chaine.charAt(i));
            // On passe au prochain caractère différent
            i += cptChar;
        }
        // On retourne la méthode toString() du builder qui renvoie la chaîne compressée
        return dBuilder.toString();
    }

    public static String RLE(String chaine, int iteration) throws AlgoException{
        if (iteration == 0){
            return chaine;
        }
        else{
            return RLE(chaine, iteration-1);
        }
        
    }

    public static String unRLE(String chaine) throws AlgoException{
        //Initialisation d'une chaine
        String chaineDecompress = "";
        int cptChar;

        // On parcourt la chaine de 2 en 2 (pour chaque couple compteur/caractère)
        for (int i = 0; i < chaine.length(); i+=2) {
            // On récupère le compteur devant le caractère...
            cptChar = Character.getNumericValue(chaine.charAt(i));
            // ... et on ajoute le caractère le nombre de fois nécessaire (=compteur)
            for(int j = cptChar; i > 0; i--)
            chaineDecompress += chaine.charAt(i+1);
        }
    return chaineDecompress;

    }

    public static String unRLE(String in, int iteration) throws AlgoException{
        // Provide your algo here
        return "NotYetImplemented";

    }

    public static void main(String[] args) {
        try {
            System.out.println(unRLE("1a1b1c"));
        } catch (AlgoException e) {
            e.printStackTrace();
        }
    }
}


package iut.sae.algo;


public class Algo{
    public static String RLE(String chaine){
        StringBuilder dBuilder = new StringBuilder();
        int cptChar;
        int i = 0;

        while(i < chaine.length()){
            cptChar = 1;

            while (i+1 < chaine.length() && chaine.charAt(i) == chaine.charAt(i+1) && cptChar < 9){
            cptChar++;
            i++;
            }

        dBuilder.append("" + cptChar + chaine.charAt(i));
        }

        return dBuilder.toString();
    }

    public static String RLE(String in, int iteration) throws AlgoException{
        // Provide your algo here
        return "NotYetImplemented";
    }

    public static String unRLE(String in) throws AlgoException{
        // Provide your algo here
        return "NotYetImplemented";

    }

    public static String unRLE(String in, int iteration) throws AlgoException{
        // Provide your algo here
        return "NotYetImplemented";

    }
}


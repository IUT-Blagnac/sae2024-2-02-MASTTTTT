package iut.sae.algo;

//17efficacite.java
// passe les tests
// complexite tempo = O(n)
// complexite spatiale = O()

//abc = 66300ns
//abbccc = 56700ns
//WWWWWWWWWWWWW = 66000ns

public class Algo {
    public static String RLE(String chaineEntree) {
        if (chaineEntree == null || chaineEntree.isEmpty()) {
            return "";
        }
        
        StringBuilder chaineCompressee = new StringBuilder();
        int compteur = 1;
        char caractereCourant = chaineEntree.charAt(0);

        for (int i = 1; i < chaineEntree.length(); i++) {
            char caractere = chaineEntree.charAt(i);
            if (caractere == caractereCourant) {
                compteur++;
                if (compteur == 10) {  // Diviser en blocs de 9 max
                    chaineCompressee.append("9").append(caractereCourant);
                    compteur = 1;
                }
            } else {
                chaineCompressee.append(compteur).append(caractereCourant);
                caractereCourant = caractere;
                compteur = 1;
            }
        }

        chaineCompressee.append(compteur).append(caractereCourant);
        return chaineCompressee.toString();
    }
    public static void main(String[] args) {
        String chaineEntree = "WWWWWWWWWWWWW";

        long startTime = System.nanoTime();
        String chaineCompressee = RLE(chaineEntree);
        long endTime = System.nanoTime();

        long duration = endTime - startTime;
        
        System.out.println("Chaine compressée: " + chaineCompressee);
        System.out.println("Temps d'exécution: " + duration + " nanosecondes");
    }
}
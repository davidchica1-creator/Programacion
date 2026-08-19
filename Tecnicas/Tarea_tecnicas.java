/**
 *
 
@author david Chica Lopez, Salome Garcia, Emanuel Garcia, Jaider Ariza*/

import java.util.Scanner;
public class Tarea_tecnicas {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        boolean centinela = true;
        int suma = 0;

        while (centinela) {

            System.out.print("Ingrese un número ( negativo para terminar ): ");

            int numero = entrada.nextInt();

            if (numero < 0){
                centinela = false;
                System.out.println("La suma total es: " + suma);
            }

            suma += numero;
        
        }

    }
}
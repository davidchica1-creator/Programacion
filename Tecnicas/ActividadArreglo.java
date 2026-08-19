/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.tecnicasprogramacion;
import java.util.Random;
import java.util.Arrays;
        

/**
 *
 * @author david
 */


public class ActividadArreglo {

    public static void main(String[] args) {
        int[] arreglo = new int[5];
        
        Random random = new Random();
        
        
        for(int i = 0; i < 5; i++){
            
            int enteroAleatorio = random.nextInt(100);
            
            arreglo[i] = enteroAleatorio;
            
        }
        
        System.out.println("--Arreglo--");
        System.out.println(Arrays.toString(arreglo));
        
        int suma = 0;
        
        for (int i = 0; i < 5; i++){
            
            suma += arreglo[i];
            
        }
        
        System.out.println("La suma de los elementos: " + suma);
        
        
    }
}

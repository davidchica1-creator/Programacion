package com.mycompany.examplemenu;

import java.util.ArrayList;
import java.util.Scanner;

//Integrantes:Jaider Steven Ariza Durango,Samuel Betancur Correa ,david Chica Lopez, Salome Garcia, Emanuel Garcia


public class ExampleMenu {

    public static void main(String[] args) {
        // 1. El estudiante debe tener Nombre, Apellido, Carrera
        // 2. Asignatura debe tener Nombre y Código

        // Regla de Negocio: 
        // 1. Un estudiante Puede tener muchas Asignaturas.
        // 2. Un Asignatura Puede tener muchos Estudiantes.
        // Instancia nuevo objeto
        ArrayList<Student> students = new ArrayList<>();
        ArrayList<Subject> subjects = new ArrayList<>();
        int option = 0;

        subjects.add(new Subject("Tec. de Programacion", "Sb1"));
        subjects.add(new Subject("Logica 2", "Sb2"));
        subjects.add(new Subject("Mat. Discretas II", "Sb3"));
        subjects.add(new Subject("Bases de Datos", "Sb4"));

        do {
            System.out.println("+++++++++++++++++++++++");
            System.out.println("University of Antioquia");
            System.out.println("+++++++++++++++++++++++");
            System.out.println("1. Create Student");
            System.out.println("2. Show all Students");
            System.out.println("3. Show available subjects");
            System.out.println("4. Assign subject");
            System.out.println("5. Show Student with Subjects");
            System.out.println("6. Exit");

            Scanner scan = new Scanner(System.in);

            int optionUser = scan.nextInt();
            scan.nextLine();

            switch (optionUser) {
                case 1 -> {
                    option = 1;
                    Student student = new Student();

                    System.out.println("Set the name of the new Student:");
                    student.setName(scan.nextLine());

                    System.out.println("Set the last name of the new Student:");
                    student.setLastName(scan.nextLine());
 
                    System.out.println("Set the career of the new Student:");
                    student.setCareer(scan.nextLine());

                    students.add(student);
                }
                case 2 -> {
                    option = 2;
                    System.out.println("The total students are: " + students.size());

                    for (Student s : students) {
                        System.out.println("+++++++++++++");
                        System.out.println("The full name of the student is: " + s.getName() + " " + s.getLastName());
                        System.out.println("Career: "+ s.getCareer());
                    } 
                }
                //Esto cumple el requerimiento de mostrar las Materias disponibles
                case 3 ->{
                    option = 3;
                    System.out.println("Avalible Subjects");
                    
                    for (Subject s : subjects){
                        System.out.println("++++++++++++++");
                        System.out.println("The name of the Subject is: " + s.getName() + " Code: " + s.getCode());
                    }
                }
                
                //Esto cumple el requerimiento de asginar una asignatura a la vez a un estudiante
                case 4 ->{
                    option = 4;
                    
                    if (students.size() == 0){
                        System.out.println("There is not Students");
                    }else{
                        System.out.println("List of Students");
                        System.out.println("+++++++++++++");
                        int contador = 1;
                        for (Student s : students) {
                            System.out.println(contador + ". " + s.getName() + " " + s.getLastName());
                            contador += 1;
                    } 
                    
                    System.out.println("Select one student of the list to asign a Subject");
                        
                    int student_lista = scan.nextInt();

                    scan.nextLine();

                    Student estudiante_guardado = students.get(student_lista - 1);
                    
                    System.out.println("Avalible Subjects");
                    
                    int contador_2 = 1;
                            
                    for (Subject s : subjects){
                        System.out.println("++++++++++++++");
                        System.out.println(contador_2 + ". " + s.getName() + " Code: " + s.getCode());
                        contador_2 += 1;
                    }
                    
                    int materia_seleccionada = scan.nextInt();
                    
                    scan.nextLine();
                    
                    Subject materia = subjects.get(materia_seleccionada - 1);
                    
                    if ( estudiante_guardado.getSubjectCuantity() < 3){
                        boolean yaExiste = false;

                        for (Subject s: estudiante_guardado.getSubjects()){
                            if (s == materia){
                                System.out.println("The student already has that subject");
                                yaExiste = true;
                                break;
                            }
                        }
                        if (!yaExiste){
                            estudiante_guardado.getSubjects().add(materia);
                            estudiante_guardado.setSubjectCuantity();
                            
                            System.out.println("Subject added successfully");
                        }
                         
                        
                    }else{
                        System.out.println("The Student has the maximum of three Subjects");
                    }
                    
                    }
                }
                
                case 5 ->{
                    option = 5;
                    
                    if (students.size() == 0){
                        System.out.println("There is not Students");
                    }else{
                        System.out.println("List of Students");
                        System.out.println("+++++++++++++");
                        int contador = 1;
                        for (Student s : students) {
                            System.out.println(contador + ". " + s.getName() + " " + s.getLastName());
                            contador += 1;
                    } 
                    
                    System.out.println("Select one student of the list to asign a Subject");
                        
                    int student_lista = scan.nextInt();

                    scan.nextLine();

                    Student estudiante_guardado = students.get(student_lista - 1);
                    
                    ArrayList<Subject> materias_estudiante = estudiante_guardado.getSubjects();
                    
                    System.out.println("Subjects of the student " + estudiante_guardado.getName());
                    int counter_3 = 1;
                    
                    for(Subject s: materias_estudiante){
                        
                        System.out.println(counter_3 + "." + s.getName());
                        counter_3 += 1;
                    }
                }
                }
                
                
                default -> option = -1;
            }

        } while (option > 0);
    }
}

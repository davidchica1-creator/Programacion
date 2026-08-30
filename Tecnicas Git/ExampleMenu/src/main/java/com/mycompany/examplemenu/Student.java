package com.mycompany.examplemenu;

import java.util.ArrayList;

public class Student {
    private String name;
    private String lastName;
    private String career;
    private ArrayList<Subject> subjects;
    private int subjectCuantity;

    public Student(String name, String lastName, String career, ArrayList<Subject> subjects) {
        this.name = name;
        this.lastName = lastName;
        this.career = career;
        this.subjects = subjects;
        this.subjectCuantity = 0;
    }
    
    public Student(){
        this.subjects = new ArrayList<>();
        this.subjectCuantity = 0;
    }

    public ArrayList<Subject> getSubjects() {
        return subjects;
    }

    public void setSubjects(ArrayList<Subject> subjects) {
        this.subjects = subjects;
    }
    
    public void setName(String name) {
        this.name = name;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setCareer(String career) {
        this.career = career;
    }

    public String getName() {
        return name;
    }

    public String getLastName() {
        return lastName;
    }

    public String getCareer() {
        return career;
    }

    public int getSubjectCuantity() {
        return subjectCuantity;
    }

    public void setSubjectCuantity() {
        this.subjectCuantity += 1;
    }
    
    
}

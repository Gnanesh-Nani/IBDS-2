package com.example;

import com.google.gson.Gson;

public class App {
    public static void main(String[] args) {
        Gson gson = new Gson();
        String json = gson.toJson(new Person("Ravi", 22));

        System.out.println("JSON Output from Gson:");
        System.out.println(json);
    }
}

class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

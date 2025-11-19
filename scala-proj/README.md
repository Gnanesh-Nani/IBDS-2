````markdown
# Scala & Scala-CLI Installation + Functional Programming Exercises  
**EXP.NO: 5(a) – Functional Programming with Lists, Sets, and Maps in Scala**

---

##  1) Install Scala & Check Version

```bash
sudo apt-get update
sudo apt-get install scala
scala -version
````

---

##  2) Download & Install Scala-CLI

```bash
curl -fLo scala-cli.deb https://github.com/Virtuslab/scalacli/releases/latest/download/scala-cli-x86_64-pc-linux.deb
sudo dpkg -i scala-cli.deb



curl -fL https://github.com/Virtuslab/scala-cli/releases/latest/download/scala-cli-x86_64-pc-linux.gz | gzip -d > scala-cli  
chmod +x scala-cli  
sudo mv scala-cli /usr/local/bin/

# Verify
scala-cli version
```

---

##  3) Verify Scala-CLI Installation

```bash
scala-cli --version
```

---

##  4) Create a Scala File

```bash
nano test.sc
```

---

##  5) Run Scala Program

```bash
scala-cli run test.sc
```

---

#  Exercise 1 — Functional Programming Basics

Create a script named **`studentData.sc`** that:

* Stores a list of marks for 5 students
* Uses **map** to calculate square of each mark
* Uses **filter** to find marks > 50
* Uses **foldLeft** to find the sum

---

##  **Code: `studentData.sc`**

```scala
val marks = List(45, 67, 89, 32, 76)

// Square of each mark
val squaredMarks = marks.map(m => m * m)

// Marks greater than 50
val above50 = marks.filter(_ > 50)

// Sum of marks
val total = marks.foldLeft(0)(_ + _)

println(s"Original Marks: $marks")
println(s"Squared Marks: $squaredMarks")
println(s"Marks > 50: $above50")
println(s"Total Marks: $total")
```

---

## ▶ Run Exercise 1

```bash
scala-cli run studentData.sc
```

---

#  Exercise 2 — Sets & Maps in Scala

Modify the script to include:

* A **Set** of unique subjects
* A **Map** storing names with marks
* Print **highest & lowest** marks

---

##  **Updated Code: `studentData.sc`**

```scala
val subjects = Set("Math", "Science", "English", "Math") // duplicates removed

val studentMarks = Map(
  "Alice" -> 67,
  "Bob" -> 45,
  "Charlie" -> 89,
  "David" -> 32,
  "Eve" -> 76
)

// Highest and lowest marks
val highest = studentMarks.values.max
val lowest = studentMarks.values.min

println(s"Subjects: $subjects")
println(s"Student Marks: $studentMarks")
println(s"Highest Mark: $highest")
println(s"Lowest Mark: $lowest")
```

---

##  Run Exercise 2

```bash
scala-cli run studentData.sc
```

---

#  Completed!

You now have:

* Scala installed
* Scala-CLI installed
* Commands to run scripts
* Two exercises solved using functional programming in Scala

```


// File: Program.scala

object CollectionProgram {
  def main(args: Array[String]): Unit = {

    println("===== Immutable List Operations =====")
    val numbers = List(10, 25, 45, 60, 5)

    val doubled = numbers.map(_ * 2)
    val above20 = numbers.filter(_ > 20)
    val sum = numbers.reduce(_ + _)
    val sorted = numbers.sorted

    println(s"Original List: $numbers")
    println(s"Doubled List: $doubled")
    println(s"Filtered (>20): $above20")
    println(s"Sum (reduce): $sum")
    println(s"Sorted List: $sorted")

    println("\n===== Immutable Set Operations =====")
    val subjects = Set("Math", "Science", "English", "Math") // duplicate auto-removed

    val upperCaseSubjects = subjects.map(_.toUpperCase())

    println(s"Original Set: $subjects")
    println(s"Uppercase Set: $upperCaseSubjects")
    println(s"Contains 'Math'? ${subjects.contains("Math")}")

    println("\n===== Immutable Map Operations =====")
    val studentMarks = Map(
      "Alice" -> 67,
      "Bob" -> 45,
      "Charlie" -> 89,
      "David" -> 32,
      "Eve" -> 76
    )

    val passedStudents = studentMarks.filter(_._2 > 50)
    val increasedMarks = studentMarks.mapValues(_ + 5)
    val totalMarks = studentMarks.values.foldLeft(0)(_ + _)
    val highest = studentMarks.values.max
    val lowest = studentMarks.values.min

    println(s"Student Marks Map: $studentMarks")
    println(s"Passed Students (>50): $passedStudents")
    println(s"Marks +5 Curve: $increasedMarks")
    println(s"Total Marks (foldLeft): $totalMarks")
    println(s"Highest Mark: $highest")
    println(s"Lowest Mark: $lowest")

    println("\n===== Conclusion =====")
    println(
      "Scala's immutable collections and higher-order functions like map, filter, and reduce\n" +
      "make transformations easy, expressive, and safe. Instead of writing loops and mutable\n" +
      "variables, developers can apply concise functional operations that automatically handle\n" +
      "iteration, transformation, and combination. This leads to cleaner, more reliable, and\n" +
      "more maintainable code."
    )
  }
}

// To run the program, use the following command in the terminal:
// scalac Program.scala && scala CollectionProgram

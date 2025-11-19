// File: ShapeProgram.scala

// 1. Abstract class
abstract class Shape {
  def area(): Double                 // abstract method
  def shapeName: String              // abstract attribute
}

// 2. Trait for displaying info
trait DisplayInfo {
  def displayInfo(): Unit = {
    println(s"Displaying shape information...")
  }
}

// 3. Concrete class: Circle
class Circle(val radius: Double) extends Shape with DisplayInfo {
  override def area(): Double = Math.PI * radius * radius
  override def shapeName: String = "Circle"

  override def displayInfo(): Unit = {
    super.displayInfo()
    println(s"Shape: $shapeName")
    println(s"Radius: $radius")
    println(f"Area: ${area()}%.2f")
    println("----------------------------------")
  }
}

// 4. Concrete class: Rectangle
class Rectangle(val length: Double, val width: Double) 
  extends Shape with DisplayInfo {

  override def area(): Double = length * width
  override def shapeName: String = "Rectangle"

  override def displayInfo(): Unit = {
    super.displayInfo()
    println(s"Shape: $shapeName")
    println(s"Length: $length, Width: $width")
    println(f"Area: ${area()}%.2f")
    println("----------------------------------")
  }
}

// 5. Main program
object ShapeProgram {
  def main(args: Array[String]): Unit = {
    val circle = new Circle(5.0)
    val rect = new Rectangle(10.0, 4.0)

    // Display details
    circle.displayInfo()
    rect.displayInfo()
  }
}


// To run the program, use the following command in the terminal:
// scalac Program.scala && scala ShapeProgram
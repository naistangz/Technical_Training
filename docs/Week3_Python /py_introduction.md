# Week 3.2 Python Introduction: 

## Python Characteristics 
1. Python is an interpreted language meaning it goes through an interpreter, which turns code you write into the **language** understood by your computer's processor
2. Python supports **object-oriented programming** and concepts of classes, objects encapsulation, etc.
3. We do not need to declare the type of variable because it is a dynamically typed language. 
4. It is a **portable language** meaning we can run python on different platforms such as Linux, Unix, and Mac.
5. Python has a **large standard library** which provides a rich set of module and functions so you do not have to write your own code for every single thing e.g. regular expressions, unit-testing, web browsers, etc.
6. It is **dynamically-typed** meaning the type e.g. int, double, long for a variable is determined at **run time** not in **advance** so we do not need to specify the type of variable. 

**Python (Dynamically Typed):**
```python
num = 5
```

**Java (Statically Typed):**
```java
int num;
num = 5;
```

**Interpreted** vs **Compiled Programming Languages:**

*Extracted from* [FreeCodeCamp](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/)
*Every program is a set of instructions, whether it's to add two numbers or send a request over the internet. Compilers and interpreters take human-readable code and convert it to computer-readable machine code. 

**What is an assembler?**
- Translates assembly language into machine code. 

**What is a compiler?**
- A special program that processes computer code written in one programming language (source language) or high-level code into another language (target language)
or lower-level machine language.

**High-Level Code** vs **Low-Level Code**
- **High Level Languages** are written in a form that is close to the human language
- They are called *high-level* as they are far removed from the **[machine code](https://www.techopedia.com/definition/8179/machine-code-mc)** instructions understood by the computer.
- **High Level Languages** do not deal with memory management and feature abstraction. 
- **Low Level Languages** are used to write programs that relate to specific architecture and hardware of a particular type of computer. 
- **Low Level Languages** are closer to the native language of a computer (binary), making them harder for programmers to understand.
- **Low level languages** do not feature abstraction and involve memory management.

**Machine Code:**

``` 169 1 160 0 153 0 128 153 0 129 153 130 153 0 131 200 208 241 96```


**High-Level Programming Languages (Python):**

```python
def addNumbers(num1, num2):
    return num1 + num2

addNumbers(4,5) # returns 9 
```

**High-level abstraction**
- High-level language is abstracted further away from the computer itself, and focuses more on programming logic rather than on basic hardware elements like memory address and register usage.  

**Compiled Language:**
- In a compiled language, the target machine directly translates the program.
- A compiler translates the whole program into machine code before the program is run.
- It can be difficult to test individual lines of compiled code.  
- Compiled languages are converted directly into machine code that the processor can execute. 
- They tend to be faster and more efficient to execute than interpreted languages. 
- They give the developer more control over hardware aspects, such as memory management and CPU usage.
- Compilation errors prevent the code from compiling.

> Examples of pure compiled languages: C, C++, Erlang, Haskell, Rust and Go 

**Interpreted Language:**
- The source code is not directly translated by the target machine. 
- Instead, a **different** program, the interpreter reads and executes the code. 
- The CPU executes each instruction before the interpreter moves on to translate the next instruction.
- Interpreted code will show an error as soon as it hits a problem, so it is easier to debug than compiled code. 

> Examples of interpreted languages: PHP, Ruby, Python and Javascript 

> Common Python Interview Questions [HERE](https://www.guru99.com/python-interview-questions-answers.html)
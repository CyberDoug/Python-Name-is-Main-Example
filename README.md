# Python-Name-is-Main-Example

This reposity is designed to teach students how the following Python expression works:

```
if __name__ == "__main__":
    main()
``` 
 
Two files are present: 1) myProgram, which is the primary program and 2) dougsLibrary, which is the library that I created.
We import dougsLibrary into myProgram in order to use the functions within it. When we do this, dougsLibrary isn't executed in its entirety. Only the functions we call on from dougsLibrary are executed. Why? Because when we call on dougsLibrary, the if statement "if __name__ == '__main__':" inside of dougsLibrary is checking to see if the code has been imported OR if it is being executed directly.

# Dynamic Typing: Type is determined at runtime

# Step 1: Assign an integer
x = 10  # `x` is an integer
print(x, type(x))  # Output: 10 <class 'int'>

# Step 2: Reassign to a string
x = "Dynamic Typing"  # `x` is now a string
print(x, type(x))  # Output: Dynamic Typing <class 'str'>

# Step 3: Reassign to a list
x = [1, 2, 3]  # `x` is now a list
print(x, type(x))  # Output: [1, 2, 3] <class 'list'>

# NOTE: Variable `x` can change its type anytime (flexible but risky)

# // Static Typing: Type is determined at compile-time
#
# public class StaticTypingExample {
#     public static void main(String[] args) {
#         // Step 1: Declare and assign an integer
#         int x = 42;  // `x` is an integer
#         System.out.println(x);  // Output: 42
#
#         // Step 2: Attempting to assign a string (ERROR!)
#         // x = "Static Typing";  // Compile-time error: incompatible types
#
#         // Step 3: Declare and assign a string
#         String y = "Static Typing";  // `y` is a string
#         System.out.println(y);  // Output: Static Typing
#
#         // NOTE: Variables cannot change type after declaration (strict but safe)
#     }
# }

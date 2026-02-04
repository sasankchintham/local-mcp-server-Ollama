from fastmcp import FastMCP
import json
# MCP Instance
mcp=FastMCP("Math Calculator")

#Tools : [1. Add two number, 2. Subtract two numbers, 3.Multiply two numbers, 4.Divide two numbers, 5.Square of a number]

#Tool 1 . Add two numbers

@mcp.tool
def add(a:int, b:int)->int:
    """Sum of two numbers given Numbers

    Args:
        a (int): First Number
        b (int): Second Number

    Returns:
        int: Returns SUM of Two given Numbers
    """
    return a+b
#Tool 2 . Subtract two numbers

@mcp.tool
def subtract(a:int,b:int)->int:
    """Subtraction of the given numbers

    Args:
        a (int): First Number
        b (int): Second Number

    Returns:
        int: Returns Subtraction Second Number from First Number [a-b]
    """
    return a-b

#Tool 3. Multiply two numbers
@mcp.tool
def multiply(a:int, b:int)->int:
    """Multipy given numbers

    Args:
        a (int): first Number
        b (int): Second number

    Returns:
        int: Returns product of two numbers
    """
    return a*b

#Tool 4. Division of two numbers
@mcp.tool
def division(a:int,b:int)->float:
    """Divide the number a by b [a/b]

    Args:
        a (int): Numerator
        b (int): Denominator
    Returns:
        float: Returns Division of two numbers a/b
    """
    return a/b

#Tool5. Square of given number
@mcp.tool
def square(a:int)->int:
    """Square of Given number

    Args:
        a (int): Given Number

    Returns:
        int: Return the square of Given Number
    """
    return a**2

@mcp.resource("info://server")
def server_info()->str:
    """Get Information about this server"""
    info={
        "name":"Math Claculator",
        "Description":"Basic Math Claculator which performs Addition, Subtraction, Multiplication, Division and Square of a number",
        "tools":["add","subtract","multiply","divide","square of a number"]
    }
    return json.dumps(info,indent=2)
if __name__=="__main__":
    mcp.run()

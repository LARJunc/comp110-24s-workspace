"""My first program for COMP110."""

__author__ = "730711502"

print("Hello, World.")


cheese: dict[str, dict[str,str]] = {"key": {"cheese": "pony"}}
print(len(cheese))
cheese.pop("key")
print(len(cheese))
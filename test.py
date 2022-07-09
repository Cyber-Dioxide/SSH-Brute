
import sys

print(f"sys.srgv = {len(sys.argv)}")
print(f"argv[1] = {sys.argv[1]}")
name , host = sys.argv[1].split("@")
print(f"Name = {name} , Host = {host}")
# Sample output with added comments

[[source]](snakes_and_ladders.py)

```
1: dice(4) -> 5     # throw 4 on first move, ending up at 5
2: dice(4) -> 9
3: dice(2) -> 11
4: dice(1) -> 12
4: jump -> 33       # jumped from 12 to 33, thus a ladder
5: dice(1) -> 34
6: dice(3) -> 37
7: dice(2) -> 39
8: dice(3) -> 42
8: jump -> 61
9: dice(4) -> 65
10: dice(6) -> 71
11: dice(1) -> 72
12: dice(3) -> 75
12: jump -> 44      # jumped from 75 to 44, thus a snake
13: dice(2) -> 46
14: dice(5) -> 51
15: dice(4) -> 55
15: jump -> 74
16: dice(4) -> 78
17: dice(4) -> 82
17: jump -> 98
18: dice(2) -> 100  # landed directly on 100, but not required to win
game over
```
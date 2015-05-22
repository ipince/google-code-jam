# Problem B: Cookie Clicker Alpha

Problem statement [here](https://code.google.com/codejam/contest/2974486/dashboard#s=p1).

**NOTE: Spoilers below!**

---

Here are the main ideas to solve this problem:
* The time needed to reach a goal, whether it's the end of the game or the cookies necessary
to buy a new farm is easy to calculate. It's just `goal - current / rate`.
* Given a state in the game, we need to decide: is it better to stay put and wait until we
reach the cookie goal at our current rate, or is it better to invest and buy more farms?
Let's call these decisions "stay" or "buy". We can then think of the game as a series of
stay/buy decisions.

* Key idea: it never makes sense to make a "buy" decision after having made a "stay" one.

So, we're really comparing "stay" vs. "buy-stay" vs. "buy-buy-stay", "buy-buy-buy-stay", etc.

Only need to compare "stay-forever" vs. "buy-and-then-stay-forever".

if "buy-buy-stay" is better than "buy-stay", then "buy-stay" is better than "stay".

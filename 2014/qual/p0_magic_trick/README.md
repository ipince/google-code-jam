# Problem A: Magic Trick

Problem statement [here](https://code.google.com/codejam/contest/2974486/dashboard#s=p0).

**NOTE: Spoilers below!**

---

This problem was very simple: the idea is to put the numbers of each guess's row into a set, and
then take the intersection between the resulting two sets. If the intersection only contains 1
card, then that must be the volunteer's card. If it contains more than 1 card, that means the
magician was sloppy and did not re-arrange the cards properly to prevent this scenario. Lastly,
if the intersection is empty, then the volunteer must have lied (by definition, if the volunteer
pointed to the rows where the chosen card was in, then the card *must* be in both sets).


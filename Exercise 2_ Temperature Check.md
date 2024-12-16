### Exercise: Temperature Check

Write a program that asks the user for the temperature (as an integer). Based on the temperature, the program should print warnings or messages according to the following conditions:  
- If the temperature is below **0**, print **"It's freezing!"**.  
- If the temperature is below **10**, print **"It's cold!"**.  
- If the temperature is below **20**, print **"It's cool!"**.  

After printing all the applicable warnings or messages, end with **"Stay safe!"**.

#### Sample Output 1:
```
Please type in the temperature: -5
It's freezing!
It's cold!
It's cool!
Stay safe!
```

#### Sample Output 2:
```
Please type in the temperature: 8
It's cold!
It's cool!
Stay safe!
```

#### Sample Output 3:
```
Please type in the temperature: 15
It's cool!
Stay safe!
```

#### Sample Output 4:
```
Please type in the temperature: 25
Stay safe!
```

---

This exercise practices:
1. Conditional execution to check multiple ranges.
2. Cumulative messaging based on progressively tighter conditions.  
3. Input and output handling in Python. 
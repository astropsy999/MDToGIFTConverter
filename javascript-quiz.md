## JavaScript

#### Q1. Which operator returns true if the two compared values are not equal?

- [ ] `<>`
- [ ] `~`
- [ ] `==!`
- [x] `!==`

[Reference Javascript Comparison Operators](https://www.w3schools.com/js/js_operators.asp)

#### Q2. How is a forEach statement different from a for statement?

- [ ] Only a for statement uses a callback function.
- [x] A for statement is generic, but a forEach statement can be used only with an array.
- [ ] Only a forEach statement lets you specify your own iterator.
- [ ] A forEach statement is generic, but a for statement can be used only with an array.

[Reference Differences between forEach and for loop](https://www.geeksforgeeks.org/difference-between-foreach-and-for-loop-in-javascript/)

#### Q3. Review the code below. Which statement calls the addTax function and passes 50 as an argument?

```js
function addTax(total) {
  return total * 1.05;
}
```

- [ ] `addTax = 50;`
- [ ] `return addTax 50;`
- [x] `addTax(50);`
- [ ] `addTax 50;`

[Reference functions in javascript](https://www.w3schools.com/js/js_functions.asp)

#### Q4. Which statement is the correct way to create a variable called rate and assign it the value 100?

- [x] `let rate = 100;`
- [ ] `let 100 = rate;`
- [ ] `100 = let rate;`
- [ ] `rate = 100;`

[Reference Javascript Assignment operators](https://www.w3schools.com/js/js_operators.asp)

#### Q5. Which statement creates a new object using the Person constructor? Which statement creates a new Person object called "student"?

- [x] `var student = new Person();`
- [ ] `var student = construct Person;`
- [ ] `var student = Person();`
- [ ] `var student = construct Person();`

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)

#### Q6. When would the final statement in the code shown be logged to the console? When would 'results shown' be logged to the console?

```js
let modal = document.querySelector('#result');
setTimeout(function () {
  modal.classList.remove('hidden');
}, 10000);
console.log('Results shown');
```

- [ ] after 10 second
- [ ] after results are received from the HTTP request
- [ ] after 10000 seconds
- [x] immediately

[Reference Javascript is synchronous and single threaded](https://stackoverflow.com/a/2035662/15067394)

#### Q7. Which snippet could you add to this code to print "food" to the console?

```js
class Animal {
  static belly = [];
  eat() {
    Animal.belly.push('food');
  }
}
let a = new Animal();
a.eat();
console.log(/* Snippet Here */); //Prints food
```

- [ ] `a.prototype.belly[0]`
- [ ] `Object.getPrototype0f (a).belly[0]`
- [x] `Animal.belly[0]`
- [ ] `a.belly[0]`

[Reference Javascript Class static Keyword](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)

#### Q8. You've written the code shown to log a set of consecutive values, but it instead results in the value 5, 5, 5, and 5 being logged to the console. Which revised version of the code would result in the value 1, 2, 3 and 4 being logged?

- [ ] `A`

```js
for (var i = 1; i <= 4; i++) {
  setTimeout(function () {
    console.log(i);
  }, i * 10000);
}
```

- [ ] `B`

```js
for (var i = 1; i <= 4; i++) {
  (function (i) {
    setTimeout(function () {
      console.log(j);
    }, j * 1000);
  })(j);
}
```

- [ ] `C`

```js
for (var i = 1; i <= 4; i++) {
  setTimeout(function () {
    console.log(i);
  }, i * 1000);
}
```

- [x] `D`

```js
for (var i = 1; i <= 4; i++) {
  (function (j) {
    setTimeout(function () {
      console.log(j);
    }, j * 1000);
  })(i);
}
```

- [ ] `E`

```js
for (var j = 1; j <= 4; j++) {
  setTimeout(function () {
    console.log(j);
  }, j * 1000);
}
```

1. [Reference setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)
2. [Reference immediately invoked anonymous functions](https://www.javascripttutorial.net/javascript-anonymous-functions/)

#### Q9. How does a function create a closure?

- [ ] It reloads the document whenever the value changes.
- [x] It returns a reference to a variable in its parent scope.
- [ ] It completes execution without returning.
- [ ] It copies a local variable to the global scope.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)

#### Q10. Which statement creates a new function called discountPrice?

- [x] `A`

```js
let discountPrice = function (price) {
  return price * 0.85;
};
```

- [ ] `B`

```js
let discountPrice(price) {
  return price * 0.85;
};
```

- [ ] `C`

```js
let function = discountPrice(price) {
  return price * 0.85;
};
```

- [x] `D`

```js
discountPrice = function (price) {
  return price * 0.85;
};
```

[Reference defining javascript functions](https://www.w3schools.com/js/js_functions.asp)

#### Q11. What is the result in the console of running the code shown?

```js
var Storm = function () {};
Storm.prototype.precip = 'rain';
var WinterStorm = function () {};
WinterStorm.prototype = new Storm();
WinterStorm.prototype.precip = 'snow';
var bob = new WinterStorm();
console.log(bob.precip);
```

- [ ] Storm()
- [ ] undefined
- [ ] 'rain'
- [x] 'snow'

[Reference prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

#### Q12. You need to match a time value such as 12:00:32. Which of the following regular expressions would work for your code?

- [ ] `/[0-9]{2,}:[0-9]{2,}:[0-9]{2,}/`
- [x] `/\d\d:\d\d:\d\d/`
- [ ] `/[0-9]+:[0-9]+:[0-9]+/`
- [ ] `/ : : /`

**NOTE**: The first three are all partially correct and will match digits, but the **second option is the most correct** because it will **only** match **2 digit** time values (12:00:32). The first option would have worked if the repetitions range looked like `[0-9]{2}`, however because of the **comma** `[0-9]{2,}` it will select 2 **or more** digits (120:000:321). The third option will any range of time digits, single _and_ multiple (meaning `1:2:3` will also match).

**More resources:**

1. [Repeating characters](https://regexone.com/lesson/repeating_characters)
2. [Kleene operators](https://regexone.com/lesson/kleene_operators)
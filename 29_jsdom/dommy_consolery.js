// Team AZ :: Angela Zhang, Annabel Zhang
// SoftDev pd2
// K29 -- DOMfoolery++ and buttons
// 2022-02-09
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          // function can stored in dictionary object, be returned with
          // o[funcName], and a parameter can be passed into it
          func : function(x) {
            return x+30;
          }
        };


// adds new items to the end of the lists with parameter
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

// removes items by item index
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


// turns items red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


// alternates red and blue when giving items color (by odds and evens)
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//fib
var fib = function(n) {
  if(n <= 1) return n ;
  else return (fib(n-1) + fib(n-2)) ;
};

//fact
var fact = function(n) {
  if(n == 1) return 1 ;
  else return (n * fact(n-1)) ;
};

//gcd
var gcd = function(a,b) {
  if(a < b) return gcd(b,a) ;
  if(a % b == 0) return b ;
  else return gcd(b,a%b) ;
};




var fibing = function () {
  addItem("fib(5) " + fib(5));
}
var facting = function () {
  addItem("fact(5) " + fact(5));
}
var gcding = function () {
  addItem("gcd(10,8) " + gcd(10, 8));
}

var btn1 = () => {
  document.getElementById("a").innerHTML = fib(5);
}
a.addEventListener('click', fibing);
var btn2 = document.getElementById("b")
b.addEventListener('click', facting);
var btn3 = document.getElementById("c")
c.addEventListener('click', gcding);

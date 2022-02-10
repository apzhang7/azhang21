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



function fibing() {
  document.getElementById("text").innerHTML = "fib " + fib(getRandom(10));
}
function facting() {
  document.getElementById("text2").innerHTML = "fact " + fact(getRandom(5));
}
function gcding() {
  document.getElementById("text3").innerHTML = "gcd " + gcd(getRandom(10),getRandom(10));
}

var b1 = document.getElementById("b1");
b1.addEventListener('click', fibing);

var b2 = document.getElementById("b2");
b2.addEventListener('click', facting);

var b3 = document.getElementById("b3");
b3.addEventListener('click', gcding);

function getRandom(n) {
  return Math.floor(Math.random() * n);
}
const body = document.querySelector("body"),
  nav = document.querySelector("nav"),
  searchToggle = document.querySelector(".searchToggle"),
  sidebarOpen = document.querySelector(".sidebarOpen"),
  siderbarClose = document.querySelector(".siderbarClose");

// js code to toggle search box
searchToggle.addEventListener("click", () => {
  searchToggle.classList.toggle("active");
});

//   js code to toggle sidebar
sidebarOpen.addEventListener("click", () => {
  nav.classList.add("active");
});

body.addEventListener("click", (e) => {
  let clickedElm = e.target;

  if (
    !clickedElm.classList.contains("sidebarOpen") &&
    !clickedElm.classList.contains("menu")
  ) {
    nav.classList.remove("active");
  }
});

//cart supTotal
var total = 0;
   //get the price
    var price = [];
    var divElements = document.getElementsByClassName("cart-amount");
 for (var i = 0; i < divElements.length; i++) {
      var text = divElements[i].textContent;
     var number = parseInt(text.replace(/\$/g, ""));
     price.push(number);
     
 }

 //get the quantity
 var quantity = [];
  var quaElements = document.getElementsByClassName("cart-count");
 for (var i = 0; i < quaElements.length; i++) {
      var text = quaElements[i].value;
     var quanumber = parseInt(text);
     quantity.push(quanumber);
   
 }
 //Sub-Total Account
  for (var i = 0; i < quaElements.length; i++) {
   var j = 0;
   total = total + (price[i] * quantity[i]);
 }

 document.getElementById('cart-total-amount').textContent = total + " S.P";
 
 //even Change number In form
 document.querySelector('.CartContainer').addEventListener('input', function() {
   var total = 0;
   //price
    var price = [];
    var divElements = document.getElementsByClassName("cart-amount");
 for (var i = 0; i < divElements.length; i++) {
      var text = divElements[i].textContent;
     var number = parseInt(text.replace(/\$/g, ""));
     price.push(number);
 }

 //quantity
 var quantity = [];
    var quaElements = document.getElementsByClassName("cart-count");
 for (var i = 0; i < quaElements.length; i++) {
      var text = quaElements[i].value;
     var quanumber = parseInt(text);
     quantity.push(quanumber);
 }
  //Sub-Total Account
 for (var i = 0; i < quaElements.length; i++) {
    total = total + (price[i] * quantity[i]) ;
 }
 document.getElementById('cart-total-amount').textContent = total+" S.P";
 });
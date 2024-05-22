money = 0;
moneyup = 1;
msec = 0;
upcost = 1;
upown = 0;

function addcomma(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}

//what happens when button is clicked
function clicked() {
  money += moneyup;
  document.getElementById("total").innerHTML = "Mash: " + addcomma(money);
}

//upgrade function
function upgrade() {
  if (money >= Math.round(upcost)) {
    moneyup += 1;
    money -= Math.round(upcost);
    upown += 1;
    upcost = upcost * 1.1;
    document.getElementById("upgrade").innerHTML =
      "Clicker Upgrade: " + addcomma(Math.round(upcost)) + " mash";
  }

  document.getElementById("click").innerHTML =
    "mash/click: " + addcomma(moneyup);
  document.getElementById("total").innerHTML = "Mash: " + addcomma(money);
}

function flag() {
  $.ajax({
    type: "post",
    url: '/flag',
    dataType: 'json',
    data: {
      mash: money
    },
    success: function(data) {
      document.getElementById("message").innerHTML = data["message"]
    }
  });
}
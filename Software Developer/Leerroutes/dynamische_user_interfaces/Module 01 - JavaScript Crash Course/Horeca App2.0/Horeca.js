const drinken = {
    bier: 2.50,
    fris: 3.00,
    wijn: 3.50
};

let order = {};

function toevoegen(order, choice, quantity){
    if (order[choice]) {
        order[choice] += parseInt(quantity);
    }else {
        order[choice] = parseInt(quantity);
    }
}



bestellen = true;


while (bestellen) {
    
    let choice = prompt("Wat wilt u bestellen? (Toets 'stop' om de bon uit te printen)");

    if (choice == 'stop') {
        bestellen = false;
        break    
    }else if (choice in drinken){
        let quantity = prompt("Hoeveel wilt u van " + choice + "?");
        toevoegen(order, choice, quantity);
    }else if (!(choice in drinken)) {
        alert("Dit ken ik niet!");
    }

}

function bon(){
    let total = 0
    let bon = ""
    for (let drink in order) {
        let price = drinken[drink];
        let quantity = order[drink];
        let subtotal = price * quantity;
        bon += order[drink] + "x " + drink + ' = ' + subtotal.toFixed(2) + " euro<br>";
        total += subtotal;  
    }
    document.getElementById('bon').innerHTML = bon;
    document.getElementById('eindprijs').innerHTML = 'Het totaal bedrag is: ' + total.toFixed(2) + ' euro';
}


bon()

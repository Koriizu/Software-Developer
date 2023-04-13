var drank ={"bier": {name: "bier",price: 2.50, amount:0}, "wijn": {name: "wijn",price: 2.80, amount:0}, "fris": {name: "fris",price: 2.05, amount:0}}
const bestelling = {};

herhaal = true;
while (herhaal){
    Item = prompt("Wat wilt u bestellen?");
    if (drank.includes(Item)){
        hoeveel = parseInt(prompt("Hoeveel" + Item + "wilt u hebben?"));

        meer = prompt("Wilt u nog meer bestellen? y/n");
        if (meer == 'y') {
            herhaal = false;
        }}
    else {
        console.log("Dit heb ik niet!");
    };
}


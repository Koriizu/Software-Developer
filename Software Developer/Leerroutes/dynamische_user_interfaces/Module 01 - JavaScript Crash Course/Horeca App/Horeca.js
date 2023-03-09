dranken = [wijn, fris, bier]

herhaal = true
while (herhaal){
    Item = prompt("Wat wilt u bestellen?")
    if (dranken.includes(Item)){
        hoeveel = prompt("Hoeveel" + Item + "wilt u hebben?")
        meer = prompt("Wilt u nog meer bestellen? y/n")
        if (meer == 'y') {
            herhaal = false
        }}
    else {
        console.log("Dit heb ik niet!")
    };
}


function calcfloors(){
    console.log("Function")
    let uitleg = "In een parkeergarage passen 80 auto's op de begane grond en 120 op een verdieping.\n"+
    "Vraag het gewenste aantal auto's in de garage en bereken het aantal verdiepingen wat je nodig hebt.";

    alert(uitleg);
    let gewenste_aantal_autos = parseInt(prompt("Hoeveel autos wilt u kwijt in de parkeergarage?"));
    // Berekenen hier het aantal verdiepingen
    let floors = (gewenste_aantal_autos+40)/120
    floors = Math.ceil(floors);

    let antwoord = floors.toString()+ " verdiepingen heb je nodig";
    document.getElementById("antwoord").innerText = antwoord;

    console.log("Om het gewenste aantal autos kwijt te kunnen heb ik " + floors.toString() + " verdiepingen nodig.");
    documentwrite("Om het gewenste aantal autos kwijt te kunnen heb ik " + floors.toString() + " verdiepingen nodig.");
    alert("Om het gewenste aantal autos kwijt te kunnen heb ik " + floors.toString() + " verdiepingen nodig.")
}

function documentwrite(text){
    Element = document.createElement("H2");
    Element.innerText = text;
    body = document.getElementsByTagName("BODY")[0];
    body.appendChild(Element)
}
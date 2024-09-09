persons = [
    {id: 12, name: 'Eren Yeager', role: 'manager', gender: 'female', age: 26},
    {id: 45, name: 'Ash Ketchup', role: 'client', gender: 'male', age: 11},
    {id: 3, name: 'Anthony van de Leuv', role: 'designer', gender: 'female', age: 21},
]

function showPerson(person){
    console.dir(person);
    let personWindow = document.getElementById('person');
    personWindow.innerText = `name: ${person.name}\nrole: ${person.role}\nage: ${person.age} `;
}

// Server
getPersonButtonServer = document.getElementById('get-person-serverside');

function load(event){
    person = this.response;
    showPerson(person)
}

function getPersonButtonServerClicked(event){
    console.log('second button clicked');
    let request = new XMLHttpRequest();
    request.open('GET','persons.php');
    request.responseType = "json";
    request.onload = load;

    request.send();

    //showPerson(persons[1]);
} 

getPersonButtonServer.onclick = getPersonButtonServerClicked;

// Client
getPersonButton = document.getElementById('get-person');

function getPersonButtonClicked(event){
    console.log('clicked');
    showPerson(persons[1])
} 

getPersonButton.onclick = getPersonButtonClicked;
<?php
$persons = [
    ["id"=>10, "name"=>"Eren Yeager", "role"=>"developer", "gender"=>"male", "age"=>34],
    ["id"=>15, "name"=>"Ash Ketchup", "role"=>"administrator", "gender"=>"male", "age"=>41],
    ["id"=>21, "name"=>"Anthony van de Leuv", "role"=>"tester", "gender"=>"female", "age"=>38],
  ];

  $person = $persons[1];
  $response = json_encode($person);
  header("Content-type:application/json");
  echo $response;
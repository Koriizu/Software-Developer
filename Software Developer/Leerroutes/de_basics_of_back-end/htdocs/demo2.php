<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>kebab calculator</h1>
    <?php ?> 
    <form action="demo2.php" method="get">
        Choose a number: <input type="number" name="num1">
        <br>
        Choose a second number: <input type="number" name="num2">
        <input type="submit">
    </form>
    <br>
    The number that you have chosen is: <?php echo $_GET["num1"] ?>
    <br>
    The second  number that you have chosen is: <?php echo $_GET["num2"] ?>
    <br>
    The answer = <?php echo $_GET["num1"] * $_GET["num2"] ?>
    
</body>
</html>



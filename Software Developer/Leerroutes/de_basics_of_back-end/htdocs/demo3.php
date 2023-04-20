<?php
if (isset($_GET['nr'])) {
    if(is_numeric($_GET['nr'])) {
        $getal = $_GET['nr'];
        for ($i = 1; $i <= 10; $i++) {
            echo "$i x $getal = " . ($i * $getal) . "<br/>";
        }
        echo '<a href="demo3.php">Terug</a';
    } else {
        echo "Geen getal gegeven";
    }
} else {
    ?>
    <form method="get">
    Kies een getal: <input type="number" name="nr"><br/>
        <input type="submit">
    </form>
    <?php
}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
        echo("<h1>Hello World</h1>");
        echo "<hr>";
        echo "<p>This is my site</p>";

        echo "<h1> Variables </h1>";
        echo "<hr>";

        $characterName = "John";
        $characterAge = 32;
        
        echo "There once was a man named $characterName <br>";
        echo "He was $characterAge years old <br>";
        echo "He really liked the name $characterName <br>";
        echo "But he didn't like being $characterAge <br>";
    
    ?>
</body>
</html>
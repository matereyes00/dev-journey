<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php error_reporting(0); ?>
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

        echo "<h1> Data Types </h1>";
        echo "<hr>";
        // string
        $phrase = "to be or not to be";
        // numbers: whole and decimal (float)
        $age = 22;
        $gpa = 3.23;
        // booleans
        $isMale = false;
        echo $phrase;

        echo "<h1> Using Strings </h1>";
        echo "<hr>";
    
        // storing inside variable
        $phrase2 = "Giraffe Academy <br>";
        echo $phrase2;

        // using functions to do special things with strings in the program
        // echo strtolower($phrase2);
        echo strtoupper($phrase2);
        echo strlen($phrase2);
        echo $phrase2[0];
        echo str_replace("Giraffe", "Panda", $phrase2);
        echo substr($phrase2, 8); // index where we want to grab substring from
        echo substr($phrase2, 8, 3); // index where we want to grab substring from

        echo "<h1> Working with Numbers </h1>";
        echo "<hr>";
        echo 10 % 3;
        echo "<br>";
        $num = 30;
        $num += 24;
        echo "$num <br>";
        // more advanced, functions to get stuff like square roots n all
        echo abs(-102);
        echo "<br>";
        echo max(2,10);
        echo "<br>";
        echo min(2,10);
        echo "<br>";
        echo round(2.10);
        echo "<br>";
        echo ceil(2.10);
        echo "<br>";
        echo floor(2.10);
        
        echo "<h1> Getting user input </h1>";
        echo "<hr>";
        // setting up a form - allows user to input information, passes it to the php
        // middleman between html and php
    ?>

    <form action="site.php" method="get">
        Name: <input type="text" name="username">
        <br>
        Age: <input type="number" name="age">
        <input type="submit">
    </form>
    <br>
    Your name is <?php echo $_GET["username"] ?>
    <br>
    Your age is <?php echo $_GET["age"] ?>
</body>
</html>
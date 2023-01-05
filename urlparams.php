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
        echo $_GET["name"]; 
        echo $_GET["age"];

        echo("<h1>GET vs. POST </h1>");
    ?>

    <form action="urlparams.php" method="post">
        Password: <input type="password" name="password">
        <input type="submit">
    </form>

    <?php 
        echo $_POST["password"];
    ?>
</body>
</html>
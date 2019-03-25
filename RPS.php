<?php
/*
Created on Mar 7, 2019
Created for: ICS3U
@author: Francesca Berkoh
Daily Assignment - 3-03
This program plays rock paper or scissors
*/
?>


<form action="" method="POST">
<br><br>
<input type="submit" name="submitrock" value="Rock"/><br><br>
<input type="submit" name="submitpaper" value="Paper"/><br><br>
<input type="submit" name="submitscissors" value="Scissors"/><br><br>
</form>

<?php
$rockbutton= $_POST['submitrock'];
$paperbutton= $_POST['submitpaper'];
$scissorsbutton= $_POST['submitscissors'];

if ($rockbutton){
    $computer= mt_rand(1,3);
    if ($computer == 1){
        echo "Congrats!, Comupter chose: Scissors";
    }
    if ($computer == 2){
            echo "Aww too bad!, Computer chose: Paper"; 
    }
    if ($computer == 3){
        echo "It's a draw!, Computer chose: Rock";
    }
}

if ($paperbutton){
    $computer= mt_rand(1,3);
    if ($computer == 1){
        echo "Congrats!, Comupter chose: Rock";
    }
    if ($computer == 2){
        echo "Aww too bad!, Computer chose: Sissors";
    }
    if ($computer == 3){
        echo "It's a draw!, Computer chose: Paper";
    }
}

if ($scissorsbutton){
    $computer= mt_rand(1,3);
    if ($computer == 1){
        echo "Congrats!, Comupter chose: Paper";
    }
    if ($computer == 2){
        echo "Aww too bad!, Computer chose: Rock";
    }
    if ($computer == 3){
        echo "It's a draw!, Computer chose: Scissors";
    }
}


?>

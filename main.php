<?php

//Main script that calls the python file

function Redirect($url, $permanent = false)
{
    if (headers_sent() === false) {
        header('Location: ' . $url, true, ($permanent === true) ? 301 : 302);
    }

    exit();
}

function getCurrentSkips()
{
    $filename = "./counter.txt";

    $handler = fopen($filename, 'r+') or die("Couldnt find the file, are you in the right dir");

    $contents = fread($handler, filesize($filename));

    fclose($handler);

    return $contents;

}

function voteSkip()
{
    $currentvotes = getCurrentSkips();
    $currentvoteswith1 = $currentvotes + 1;
    $filename = "./counter.txt";
    if( $currentvoteswith1 == 5)
    {
        $filewriter = fopen($filename, "w+") or die("Couldnt find the file, are you in the right dir");
        echo( "<b> You are the last vote, skipping. You might have to wait a few seconds.</b>" );
        fwrite($filewriter, $currentvoteswith1);
        Redirect("/SeshMan");

    }
    else {
        $filewriter = fopen($filename, "w+") or die("Couldnt find the file, are you in the right dir");
        echo("<b>You are vote number" . $currentvoteswith1 ."</b>");
        fwrite($filewriter, $currentvoteswith1);
        Redirect("/SeshMan");
    }


}

voteSkip();

//Redirect("/SeshMan");




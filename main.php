<?php
//Main script that calls the python file
function skipSong(){
    system('python ./Skip.py');
}
function Redirect($url, $permanent = false)
{
    if (headers_sent() === false)
    {
        header('Location: ' . $url, true, ($permanent === true) ? 301 : 302);
    }

    exit();
}
function readCounter(){
    $filename = "./counter.txt";

    $handler = fopen($filename,'r');

    $contents = fread($handler, filesize($filename));

    return $contents;
}
skipSong();
Redirect("/SeshMan");



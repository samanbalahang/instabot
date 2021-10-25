<?php
$my_command = escapeshellcmd('python D:/xampp/htdocs/instabot/test.py');
$command_output = shell_exec($my_command);
echo $command_output;
?>
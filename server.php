<?php
$data = file_get_contents("data/future_forecast.csv");
echo nl2br($data);
?>
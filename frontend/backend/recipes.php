<?php

require_once('recipes.inc');

function path($user, $what) {
	return "data/$what.json";	
}

function get(){
	$user = "xtofl";
	$what = $_GET["what"];
	$content = file_get_contents(path($user, $what));
	print($content);
};

function post(){
	$user = "xtofl";
	$data = json_decode(file_get_contents("php://input"));
	$key = $data->what;
	$content = json_encode($data->content);
	file_put_contents(path($user, $key), $content);
};

switch($_SERVER['REQUEST_METHOD']){
	case 'POST': post(); break;
	case 'GET': get(); break;
	default: break;
}

?>
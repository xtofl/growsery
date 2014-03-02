<?php

require_once('recipes.inc');

function path($user) {
	return "data/recipes.json";	
}

function get(){
	$user = "xtofl";
	$content = file_get_contents(path($user));
	print($content);
};

function post(){
	$user = "xtofl";
	$data = file_get_contents("php://input");
	file_put_contents(path($user), $data);
};

switch($_SERVER['REQUEST_METHOD']){
	case 'POST': post(); break;
	case 'GET': get(); break;
	default: break;
}

?>
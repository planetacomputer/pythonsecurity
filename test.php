<?php
	$numeroAula = $_REQUEST['numeroAula'];
	$accion = $_REQUEST['accion'];
	echo "Hola PHP ".$numeroAula."<br>";
	echo $accion;
	if($accion == "add"){
		echo "Se anyade una ip pq se prohibe";
		echo exec('python /etc/squid/python1.py '.$numeroAula).'<br>';
	}
	else{
		echo "Se elimina una ip pq se permite lo que previamente se anyadio";
		echo exec('python /etc/squid/python2.py '.$numeroAula).'<br>';
	}
?>
<a href="urls.php">Volver</a>
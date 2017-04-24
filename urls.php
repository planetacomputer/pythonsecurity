<!DOCTYPE html>
<html>
<body>

<form action="test.php" method="POST">
  Numero de aula:<br>
  <input name="numeroAula" type="number" value="">
  <br>
  <input type="radio" name="accion" value="delete"> Permitir (suprimir)<br>
  <input type="radio" name="accion" value="add"> Prohibir (anadir)<br>

  <input type="submit" value="Submit">
</form> 
<pre>
<?php echo file_get_contents("/etc/squid/aulas-prohibidas.txt"); ?>
</pre>
</body>
</html>
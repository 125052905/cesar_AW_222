<?php

/*incluye  la informacion del archivo conexion*/
include("conexion.php");

/*dame todo lo que tengas en la tabla alumnos*/
$con = conectar();
$sql = "SELECT * FROM alumnos";
$query =mysqli_query($con, $sql);


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD DE ALUMNOS</title>
</head>
</body>    
    <h1>TABLA DE ALUMNOS</h1>
    <table border ="2">
        <thead>
        <tr>
       <th>Matricula</th>
       <th>NOMBRE</th>
       <th>apellido_p</th>
        <th>apellido_m</th>
         <th>EDAD</th>
       <th>ACCIONES</th>

          </tr>
</thead>
<tbody>
  <?php
  while($row=mysqli_fetch_array($query)){
    ?>
    <tr>
 <td><?php echo $row['matricula']?></td>
 <td><?php echo $row['nombre']?></td>
   <td><?php echo $row['apellido_p']?></td>
  <td><?php echo $row['apellido_m']?></td>
      <td><?php echo $row['edad']?></td>
</tr>
<?php
  }
  ?>

    
</tbody>
</table>
<h1>FORMULARIO</h1>
<form action ="insertar.php" method="POST">
    <div style ="display: flex; gap: 10px;">
        <input type ="text"
        class= "form-control"
        name= ""
        placeholder ="matricula">

          <input type ="text"
        class= "form-control"
        name= ""
        placeholder ="nombre">
          <input type ="text"
        class= "form-control"
        name= ""
        placeholder ="apellido_p">
  <input type ="text"
        class= "form-control"
        name= ""
        placeholder ="apellido_p">
          <input type ="text"
        class= "form-control"
        name= ""
        placeholder ="edad">
        <button type= "submit">Guardar</button>

</div>
</form>
</head>
</body>
</html>
